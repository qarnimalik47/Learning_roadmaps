# Dual Track: Networking + AI Automation Roadmap

An interactive study roadmap for two careers at once:

- **Network engineer**: CCNA with Jeremy's IT Lab and Cisco NetAcad, through to senior level
- **AI automation builder**: n8n, Python, LangChain, agents and client work, using CodeWithHarry, CampusX, Krish Naik and Gen AI Unplugged

## Features

- Two-track timeline planner based on your weekly hours
- CCNA video course: all 63 Jeremy's IT Lab Days as one continuous series, played on the page with watch tracking
  - A line for the whole course shows every video watched, part watched or not started, and the next one up
  - Every video has a tracking line beneath it: how much you've watched and how much is left (for example "40% · 12:00 watched · 18:00 left")
  - The player is large, and only its × closes it (clicking the space around it doesn't). It has previous and next buttons (Shift+P and Shift+N), and the next video plays automatically when one ends (that can be switched off).
  - **Open notes** opens that Day's notes beside the video while it keeps playing: on the right on a computer, below the video on a phone.
  - A video picks up where you left off when you open it again, even after closing it by accident or leaving the page. "Start from the beginning" restarts it.
- Ticked items always stay in view, with a tick and a line through them.
  - Under the video, the tracking line fills in the parts you've actually played and leaves gaps for the parts still left. Select any point on it to jump there.
- Videos mark themselves done at 90% watched, and tick the CCNA topics they cover
- **Revision tab:** all 2,135 flashcards from the 70 Anki decks, revised right on the page with no download and no Anki app
  - Flip a card, then choose "Not yet" or "I knew it" (Space, then 1 or 2). Cards you miss come back the same day, and cards you knew come back after 1, 3, 7, 16, 35 and then 75 days.
  - "Read all" lists a whole deck with the answers filled in, or hides them so you can test yourself
  - Search every card, filter decks (watched Days, not finished, due for review), a "due for review" session and a shuffled mixed review
  - The Anki buttons on Networking topics, in the notes reader, in Practice > Anki and labs and next to each video all open the cards here. Packet Tracer labs still download as before.
  - Progress is saved with the rest of your progress (and to your account when accounts are on), and revision time counts toward your daily goal
- **Slides (Revision > Slides):** the class slides for all six CCNA modules, 436 slides in 63 short topics, shown right on the page
  - Pick a module, then a topic. Each topic card shows how many slides it has and how many you have seen.
  - **Quick revision** shows only the 223 key slides: definitions, comparisons, summaries and the main commands. It skips title slides, photos, repeated worked examples, the extra routers in a lab, and assignments.
  - The viewer moves with the arrow keys, Space, a tap or a swipe, shows a strip of the topic's slides, zooms (Z), goes full screen (F), switches to quick revision (Q), and carries on to the next topic at the end of one
  - Search the words on every slide, and download each module's original PowerPoint file
  - A **Slides** chip on each matching CCNA topic, and a **Module N slides** link under each exam domain, open the right slides
  - Slides you have seen are saved with the rest of your progress, and time on slides counts toward your daily goal
  - Slides 1 to 4 of modules 2 to 6 repeat the title and course outline, so they appear once, in Module 1. Four blank slides in Module 1 are left out.
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
- Light and dark modes: light grey and white with calm blue (Networking) and soft pink (AI) accents, Archivo type, wide pages, and chart colors checked for colour-blind readability.
- Easy-to-read text sizes, and a top bar that always fits every tab: on narrower screens it first shows Search and the account as icons, then moves the tabs to their own row, then shortens long tab names.
- **Leaderboard (every student):** XP for every video (100), lab (75), notes read (25), quiz card known (10), exam topic ticked (15), practice question answered (2) and day studied (20), with ten levels from Cable Rookie to Network Engineer.
  - Rank the class by **This week**, **All time** or **Course progress**, with a top-3 podium, your rank and level, and how far you are behind the next person.
  - Classmates see only each other's name, XP, level and progress counts, never emails. Anyone can untick **Show me on the leaderboard**.
  - XP is worked out in each student's browser from their own saved work.
- Study notes for every CCNA Day, linked from each topic, with quiz cards
- Anki flashcard decks (70, revised in the Revision tab) and Packet Tracer labs (48, downloaded) on every CCNA topic, in the notes reader, and in Practice > Anki and labs, with a "lab done" tick that counts as progress
- Skill map showing how the two tracks connect
- Export and import progress backups

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app |
| `notes.js` | CCNA study notes for Days 1–63, opened from topics, videos and search |
| `flashcards.js` | Every card from the Anki decks, for the Revision tab. Built from `CCNA-Flashcards/` |
| `tools/build_flashcards.py` | Rebuilds `flashcards.js` from the decks (`pip install zstandard`, then `python tools/build_flashcards.py`) |
| `config.js` | Your Supabase project URL and public key, and optional video links |
| `supabase/setup.sql` | The PostgreSQL tables and security rules. Run it once in Supabase's SQL Editor |
| `CCNA-Flashcards/` | Anki decks (`.apkg`), one or more per Day |
| `CCNA-Labs/` | Packet Tracer labs (`.pkt`), one or more per Day |
| `slides/` | The six CCNA module decks (`.pptx`), every slide as a web image (`m1/` to `m6/`, thumbnails in `t/`), and `text.js`, the words on each slide for search |
| `tools/export_slides.ps1`, `tools/build_slides.py` | Rebuild `slides/` after a deck changes (see below) |

Upload both folders and `flashcards.js` next to `index.html`, keeping the file names exactly as they are. The site links to each file by name. If you add or rename a deck or lab, update the `ANKI` or `LABF` list near the end of `index.html` to match. After changing a deck, run `python tools/build_flashcards.py` to rebuild `flashcards.js`.

To update the slides after editing a deck, save the new `.pptx` into `slides/` with the same name, then run these two commands. The first needs Microsoft PowerPoint and the second needs `pip install pillow`:

```
powershell -ExecutionPolicy Bypass -File tools\export_slides.ps1 -Decks slides -Out C:\temp\slide-png
python tools/build_slides.py --png C:/temp/slide-png --decks slides --out slides
```

If slides were added, removed or moved, update the topic list (`SLIDE_MODULES`) near the end of `index.html` so every topic still points at the right slides.

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
- **More admins:** have them create an account, then run `insert into public.admins (email) values ('their-email@example.com');` (lowercase) in the SQL Editor. Admins show the title **Admin** on the leaderboard and in their profile instead of a level.
