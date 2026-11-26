# Library sectors

The knowledge library behind this engine holds **1,165 entries** (1,146 books, counting duplicates once). Every book belongs to one sector. Sectors are the engine's map: when a project problem arrives, the sector tells the engine where the next techniques will come from as more books are read page by page.

Book titles stay out of this public file by design; only the sectors and their sizes are published.

| Sector | Books | What it feeds |
| --- | ---: | --- |
| Red Team, Pentesting & Offensive Operations | 213 | Attack paths the defenses must survive |
| Network Security & Protocols | 195 | Traffic, protocols, and network controls |
| Web & Application Security | 144 | Application flaws and their fixes |
| Programming Languages | 88 | Code-level hardening in every stack |
| Linux & Unix | 88 | Host hardening and administration |
| General & Reference | 83 | Cross-cutting reference material |
| Malware, Reverse Engineering & Exploitation | 64 | How hostile code works, and how to stop it |
| Security Fundamentals & General | 62 | Core concepts every project inherits |
| OSINT, Social Engineering & Human Factors | 41 | The human layer of every system |
| Certification & Career | 38 | Structured curricula and exam depth |
| Windows & Microsoft | 31 | Windows and Active Directory hardening |
| Mobile & Embedded / IoT | 29 | Phones, firmware, and devices |
| Blue Team, Defense & Governance | 16 | Detection, governance, and risk |
| Wireless & Radio | 15 | Wi-Fi, radio, and signal security |
| Forensics & Incident Response | 15 | Evidence, response, and recovery |
| Cloud & Containers | 12 | Cloud and container controls |
| Cryptography | 11 | Encryption done right |
| Blockchain & Cryptocurrencies | 8 | Ledger and contract security |
| AI & Machine Learning | 6 | Models, data, and AI systems |
| Databases & Data | 6 | Data protection and database controls |

## Reading order

Books are read one at a time, page by page, in the order that maximizes the projects under fire: network and defense first, then the sectors each active project touches. Each finished book adds its technique cards to `corpus.json` and its export to `data/techniques.dmp`.
