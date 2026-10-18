# Dual Track: Networking + AI Automation Roadmap

An interactive study roadmap for two careers at once:

- **Network engineer**: CCNA with Jeremy's IT Lab and Cisco NetAcad, through to senior level
- **AI automation builder**: n8n, Python, LangChain, agents and client work, using CodeWithHarry, CampusX, Krish Naik and Gen AI Unplugged

## Features

- Two-track timeline planner based on your weekly hours
- CCNA video course: all 63 Jeremy's IT Lab Days, played on the page with watch tracking
- Videos mark themselves done at 90% watched, and tick the CCNA topics they cover
- Student and admin accounts (Firebase): admins see every student's progress, daily watch time and videos
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
| `firestore.rules` | Database security rules to paste into Firebase |
| `CCNA-Flashcards/` | Anki decks (`.apkg`), one or more per Day |
| `CCNA-Labs/` | Packet Tracer labs (`.pkt`), one or more per Day |

Upload both folders next to `index.html`, keeping the file names exactly as they are. The site links to each file by name. If you add or rename a deck or lab, update the `ANKI` or `LABF` list near the end of `index.html` to match.

Without Firebase settings in `config.js`, the site still works: everyone's progress is saved in their own browser, with no accounts.
