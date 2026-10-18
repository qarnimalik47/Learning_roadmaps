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
  - **With accounts (Firebase):** every student appears live, and coach notes and class messages show at the top of their Progress page.
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
| `config.js` | Your Firebase settings, admin emails and optional video links |
| `firestore.rules` | Database security rules to paste into Firebase (includes coach notes) |
| `CCNA-Flashcards/` | Anki decks (`.apkg`), one or more per Day |
| `CCNA-Labs/` | Packet Tracer labs (`.pkt`), one or more per Day |

Upload both folders next to `index.html`, keeping the file names exactly as they are. The site links to each file by name. If you add or rename a deck or lab, update the `ANKI` or `LABF` list near the end of `index.html` to match.

Without Firebase settings in `config.js`, the site still works: everyone's progress is saved in their own browser, with no accounts.
