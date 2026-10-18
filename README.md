# Dual Track: Networking + AI Automation Roadmap

An interactive study roadmap for two careers at once:

- **Network engineer**: CCNA with Jeremy's IT Lab and Cisco NetAcad, through to senior level
- **AI automation builder**: n8n, Python, LangChain, agents and client work, using CodeWithHarry, CampusX, Krish Naik and Gen AI Unplugged

## Features

- Two-track timeline planner based on your weekly hours
- CCNA video course: all 63 Jeremy's IT Lab Days, played on the page with watch tracking
- Videos mark themselves done at 90% watched, and tick the CCNA topics they cover
- **Progress page (every student):** CCNA readiness score with its breakdown, progress over the last 12 weeks, exactly what's done and what's left, mastery per exam domain, study streak, activity heatmap, hours per week, a 63-Day course map, practice-drill accuracy and personalised next steps. Students can download a progress report or print the page.
- **Class dashboard (admin)**, in six sections:
  - **Overview:** headline numbers, class study time with the most active students, and domain mastery across the class.
  - **Progress:** a progress-over-time chart for every student, with the class average and any student highlighted. A progress board shows each student's videos, labs, quiz cards, notes and exam topics.
  - **Work done:** a done-and-remaining grid of every student against every Day, lab or card set, plus where students drop off in the video course.
  - **Activity:** when the class studies (weekday × hour), each student's usual start time, and a feed of recent sessions with sign-in times, length and what was done.
  - **Students:** a roster with On track / Needs a push / Inactive status, last-seen times, search, sorting and CSV export, plus a message to the whole class.
  - **Reports:** report-file import, the live-accounts setup guide and video links.
  - Select any student for their full dashboard: progress over time, done and remaining, every sign-in and session, and a coach note.
- The site records study sessions (start time, last activity, length) so the admin can see when each student signs in. Sessions are recorded from the first visit after this update.
- The class dashboard works in two ways:
  - **Without accounts:** open `#admin` (there's a link in the footer) and drop in the report files students send you. Reports stay in that browser.
  - **With accounts (Supabase, PostgreSQL):** every student appears live, and coach notes and class messages show at the top of their Progress page.
- Light and dark modes in a premium theme: Archivo type, Arancio orange and Viola violet accents, chart colors checked for colour-blind readability.
- Study notes for every CCNA Day, linked from each topic, with quiz cards
- Anki flashcard decks (70) and Packet Tracer labs (48) on every CCNA topic, in the notes reader, and in Practice > Anki and labs, with a "lab done" tick that counts as progress
- Skill map showing how the two tracks connect
- Export and import progress backups

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app |
| `notes.js` | CCNA study notes for Days 1–63, opened from topics, videos and search |
| `config.js` | Your Supabase project URL and public key, and optional video links |
| `supabase/setup.sql` | The PostgreSQL tables and security rules. Run it once in Supabase's SQL Editor |
| `CCNA-Flashcards/` | Anki decks (`.apkg`), one or more per Day |
| `CCNA-Labs/` | Packet Tracer labs (`.pkt`), one or more per Day |

Upload both folders next to `index.html`, keeping the file names exactly as they are. The site links to each file by name. If you add or rename a deck or lab, update the `ANKI` or `LABF` list near the end of `index.html` to match.

Without Supabase settings in `config.js`, the site still works: everyone's progress is saved in their own browser, with no accounts.

## Accounts (PostgreSQL with Supabase)

GitHub Pages only serves files, so the site can't connect to a database by itself. Supabase hosts a real PostgreSQL database with email/password sign-in, and its row-level security rules let the page talk to it safely.

To turn accounts on (about 10 minutes, free):

1. Create a project at [supabase.com](https://supabase.com/dashboard). Signing in with GitHub works.
2. **SQL Editor > New query**: paste `supabase/setup.sql`, put your own email on the `ADMIN EMAIL` line, and press **Run**.
3. **Authentication > Sign In / Providers > Email**: turn off **Confirm email**.
4. **Authentication > URL Configuration**: set **Site URL** to `https://qarnimalik47.github.io/Learning_roadmaps/`.
5. **Project Settings > API**: copy the **Project URL** and the **anon public** key into `config.js` as `supabase: { url: "…", anonKey: "…" }`, then commit.
6. Open the site and create your own account with the admin email first.

What visitors see once accounts are on:

- **First visit:** the site opens on **Create account**, which asks only for an email and a password, with no confirmation email. Returning visitors on that browser see **Sign in**.
- **Account menu:** the name pill at the top right shows the user's name and role, with links to their progress (and the class dashboard for admins), **Switch account** and **Sign out**.
- **Names** come from the email address and can be changed on the Progress page.
- **Forgot password** sends a reset link that opens a "Set a new password" screen on the site.
- **Data:** students can only read and change their own data. Admins, listed in the `admins` table, see everyone and can write coach notes and the class message.
