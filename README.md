# Dual Track: Networking + AI Automation Roadmap

An interactive study roadmap for two careers at once:

- **Network engineer**: CCNA with Jeremy's IT Lab and Cisco NetAcad, through to senior level
- **AI automation builder**: n8n, Python, LangChain, agents and client work, using CodeWithHarry, CampusX, Krish Naik and Gen AI Unplugged

## Features

- Two-track timeline planner based on your weekly hours
- CCNA video course: all 63 Jeremy's IT Lab Days, played on the page with watch tracking
- Videos mark themselves done at 90% watched, and tick the CCNA topics they cover
- Student and admin accounts (Firebase): admins see every student's progress, daily watch time and videos
- Skill map showing how the two tracks connect
- Export and import progress backups

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app |
| `config.js` | Your Firebase settings, admin emails and optional video links |
| `firestore.rules` | Database security rules to paste into Firebase |

Without Firebase settings in `config.js`, the site still works: everyone's progress is saved in their own browser, with no accounts.
