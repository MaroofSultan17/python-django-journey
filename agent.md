# AGENT INSTRUCTIONS & WORKSPACE RULES

## 1. Documentation & Knowledge Source
- **Primary Source of Truth**: Obsidian Vault located in local `Documents/Obsidian/` (refer to the PSEB DEPLOY documentation files).
- Always verify rules, grading rubrics, and project guidelines against the Obsidian notes before generating architecture or code.

## 2. Technical Environment & Stack
- **Environment**: Local Python development inside PyCharm using standard virtual environment (`.venv`).
- **DO NOT** use Docker, Docker Compose, or containerization.
- **DO NOT** create over-engineered layers (no unsolicited enterprise services or repository patterns). Keep solutions clean, modular, and strictly aligned with the PDF requirements.

## 3. Mandatory Daily Git Protocol
- Individual repo requires at least 1 meaningful commit every class and home day.
- A day counts as worked **ONLY** when the commit timestamp strictly matches the entry in `hours-log.md`.
- Hours format:
  `| Date | Hours Worked | Work Completed | Commit Hash |`

## 4. Group & PR Protocol
- `main` branch is protected. No direct commits to `main`.
- All PRs must follow the strict 3-line template:
  1. What changed
  2. How it was tested
  3. Who reviewed it
- Never commit secrets or `.env`. Commit `.env.example` only.

## 5. Offline-First & Mock Fallback
- For any AI/Chatbot or external API integrations: Build local mock adapters and rule-based fallbacks **FIRST**. The feature must run 100% offline.
- Real API calls are treated strictly as an optional bonus. The mock adapter and offline fallback are the graded requirements.
