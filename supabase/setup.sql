-- Dual Track: PostgreSQL database for student and admin accounts (Supabase).
-- Run once: Supabase dashboard > SQL Editor > New query > paste this file > Run.
-- Before running, put your own email on the line marked ADMIN EMAIL.
-- Safe to run again later: it only adds what is missing and refreshes the rules.

-- Admins: emails that can see every student. Kept in the database, not in the website.
create table if not exists public.admins (
  email text primary key check (email = lower(email))
);

-- Nothing is added while the line still has the example address, so nobody can sign up with it and become an admin.
insert into public.admins (email)
select e from (values ('your-email@example.com')) as v(e)  -- ADMIN EMAIL: your own email, in lowercase
where e <> 'your-email@example.com'
on conflict do nothing;

create or replace function public.is_admin() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.admins
    where email = lower(coalesce(auth.jwt() ->> 'email', ''))
  );
$$;

-- One row per student: name, email and the summary the class dashboard lists
create table if not exists public.profiles (
  id          uuid primary key references auth.users (id) on delete cascade,
  email       text not null,
  name        text,
  created_at  bigint,
  last_active bigint,
  summary     jsonb not null default '{}'::jsonb,
  daily       jsonb not null default '{}'::jsonb
);

-- Each student's full progress: ticks, videos, labs, quiz cards, sessions
create table if not exists public.progress (
  id         uuid primary key references auth.users (id) on delete cascade,
  state      jsonb not null default '{}'::jsonb,
  updated_at bigint
);

-- Coach notes: one per student, written by an admin, read by that student
create table if not exists public.notes (
  id         uuid primary key references auth.users (id) on delete cascade,
  text       text not null default '',
  by_name    text,
  updated_at bigint
);

-- Shared settings: video links and the message to the whole class
create table if not exists public.settings (
  key        text primary key,
  value      jsonb not null,
  updated_at bigint
);

-- Row level security: students reach only their own rows; admins reach everyone's
alter table public.admins   enable row level security;
alter table public.profiles enable row level security;
alter table public.progress enable row level security;
alter table public.notes    enable row level security;
alter table public.settings enable row level security;

drop policy if exists "profiles read"   on public.profiles;
drop policy if exists "profiles insert" on public.profiles;
drop policy if exists "profiles update" on public.profiles;
drop policy if exists "profiles delete" on public.profiles;
create policy "profiles read"   on public.profiles for select to authenticated using (id = auth.uid() or public.is_admin());
create policy "profiles insert" on public.profiles for insert to authenticated with check (id = auth.uid());
create policy "profiles update" on public.profiles for update to authenticated using (id = auth.uid()) with check (id = auth.uid());
create policy "profiles delete" on public.profiles for delete to authenticated using (public.is_admin());

drop policy if exists "progress read"   on public.progress;
drop policy if exists "progress insert" on public.progress;
drop policy if exists "progress update" on public.progress;
create policy "progress read"   on public.progress for select to authenticated using (id = auth.uid() or public.is_admin());
create policy "progress insert" on public.progress for insert to authenticated with check (id = auth.uid());
create policy "progress update" on public.progress for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists "notes read"   on public.notes;
drop policy if exists "notes insert" on public.notes;
drop policy if exists "notes update" on public.notes;
drop policy if exists "notes delete" on public.notes;
create policy "notes read"   on public.notes for select to authenticated using (id = auth.uid() or public.is_admin());
create policy "notes insert" on public.notes for insert to authenticated with check (public.is_admin());
create policy "notes update" on public.notes for update to authenticated using (public.is_admin()) with check (public.is_admin());
create policy "notes delete" on public.notes for delete to authenticated using (public.is_admin());

drop policy if exists "settings read"   on public.settings;
drop policy if exists "settings insert" on public.settings;
drop policy if exists "settings update" on public.settings;
create policy "settings read"   on public.settings for select to authenticated using (true);
create policy "settings insert" on public.settings for insert to authenticated with check (public.is_admin());
create policy "settings update" on public.settings for update to authenticated using (public.is_admin()) with check (public.is_admin());

-- The admins table has no policies: it is read only through is_admin()
revoke all on public.admins from anon, authenticated;
grant execute on function public.is_admin() to authenticated;
grant select, insert, update, delete on public.profiles, public.progress, public.notes, public.settings to authenticated;
revoke all on public.profiles, public.progress, public.notes, public.settings from anon;

-- Leaderboard: every signed-in student sees each classmate's name, XP, level and progress counts.
-- Nothing else (no emails, no detailed progress) leaves the database this way.
-- Students who untick "Show me on the leaderboard" are left out.
create or replace function public.lb_num(j jsonb, k text) returns integer
language sql immutable as $$
  select case when (j ->> k) ~ '^[0-9]{1,9}(\.[0-9]+)?$' then least((j ->> k)::numeric, 1000000000)::integer else 0 end;
$$;

-- is_admin lets the page show admins with the title "Admin" instead of a level.
-- The return type changed, so the old function is dropped first; the grants below are set again.
drop function if exists public.leaderboard();
create or replace function public.leaderboard()
returns table (id uuid, name text, xp integer, week_xp integer, level integer, videos integer, labs integer,
               cards integer, streak integer, ccna integer, is_me boolean, is_admin boolean)
language sql stable security definer set search_path = public as $$
  select p.id,
         coalesce(nullif(trim(p.name), ''), 'Student'),
         public.lb_num(p.summary, 'xp'),
         -- weekly XP only counts if it was saved in the last 7 days
         case when coalesce(p.summary ->> 'at', '') !~ '^[0-9]{1,15}$' then 0
              when (p.summary ->> 'at')::bigint > (extract(epoch from now()) * 1000)::bigint - 7 * 86400000
              then public.lb_num(p.summary, 'weekXp')
              else 0 end,
         greatest(public.lb_num(p.summary, 'level'), 1),
         public.lb_num(p.summary, 'videos'),
         public.lb_num(p.summary, 'labs'),
         public.lb_num(p.summary, 'cards'),
         public.lb_num(p.summary, 'streak'),
         least(public.lb_num(p.summary, 'ccna'), 100),
         p.id = auth.uid(),
         exists (select 1 from public.admins a where a.email = lower(p.email))
  from public.profiles p
  where auth.uid() is not null
    and coalesce(p.summary ->> 'lb', 'true') <> 'false'
  order by 3 desc
  limit 500;
$$;

revoke all on function public.leaderboard() from public, anon;
grant execute on function public.leaderboard() to authenticated;
