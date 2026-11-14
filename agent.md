# AGENT INSTRUCTIONS & WORKSPACE RULES

---

### STRICT AGENT POLICY: GIT IS STRICTLY READ-ONLY

- Do NOT execute any Git write, modification, branching, or pushing commands.
- Never run:
  * `git commit`
  * `git push`
  * `git checkout -b` or `git branch`
  * `git merge` or `git rebase`
  * `git tag` or `git reset`
- Allowed Commands (Read-Only inspection ONLY):
  * `git status`
  * `git log`
  * `git diff`
- All staging (`git add`), committing, branch management, and remote pushes MUST be handled manually by the developer via local terminal.
- After making code/file changes, summarize what was modified and stop. Do not attempt to commit.

---

## 1. Documentation & Knowledge Source
- **Primary Source of Truth**: Obsidian Vault located in local `Documents/Obsidian Vault/Python Django Journey/` (refer to the PSEB DEPLOY documentation files).
- Always verify rules, grading rubrics, and project guidelines against the Obsidian notes before generating architecture or code.

## 2. Technical Environment & Stack
- **Environment**: Local Python development inside PyCharm using standard virtual environment (`.venv` running Python 3.9.6).
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

---

## 6. Python Coding & Assessment Standards (Strictly Enforced)

- **Zero AI Boilerplate Policy**:
  - Never write `if __name__ == "__main__": main()` or artificial `def main():` wrappers for foundational or console scripts.
  - Procedural code must execute naturally top-to-bottom: helper functions defined at the top, followed by sequential logic.
- **Teaching-First Code Simplicity**:
  - Code must be concise, clean, and easy to explain to beginner students in class.
  - Keep functions short (10–15 lines per function) and focused on a single task. Avoid convoluted nested while loops.
- **PEP 8 Lowercase Functions (`snake_case` Only)**:
  - All function and variable names MUST be lowercase `snake_case` (e.g., `format_name`, `get_valid_marks`, `add_expense`, `process_sale`).
  - **Never use `camelCase` for Python functions**: It triggers PyCharm / Flake8 warnings (`Function name should be lowercase`).
- **Input Validation Without `try/except`**:
  - For basic inputs (marks, roll numbers, quantities, amounts, menu choices), do not use `try-except` blocks.
  - Use `while True` loops with string methods like `.isdigit()` and `if/else` checks matching `student_scholarship_system.py` and `pharmacy_inventory_system.py`.
- **Python 3.9 Runtime Compatibility (No `match-case`)**:
  - The project runs on Python 3.9.6. `match-case` (switch) was introduced in Python 3.10 and causes `SyntaxError: invalid syntax` on Python 3.9.
  - Always use standard `if-elif-else` for menu branching so scripts run universally on all student machines and LMS servers.
- **Compound Data Structures (Lists of Dictionaries)**:
  - In Week 2, represent multi-attribute entities using a list of dictionaries (`products = [{"id": 101, ...}]`) and transactional ledgers in `sales_records`.
  - Mutate dictionary keys directly in-place (`p["stock"] -= qty`).
- **Pakistani Educational Context (BISE / Board Standards)**:
  - Academic result card and grade calculation modules must adhere to Pakistani Board (BISE / FBISE) examination rules.
  - If any subject score is below 40 (or total below 50%), **withhold aggregate percentage and letter grade** (`---`).
  - Set status to **`RE-APPEAR`** and provide an explicit notice listing the failed subjects for the supplementary exam.
- **Hours Log & 100% Viva Defensibility (e.g. 5.0h / 6.0h)**:
  - Every day worked must have an entry in `hours-log.md` with date, hours, technical description, and the matching commit hash.
  - Any logged effort **must be defended in the project `README.md`** with an Engineering Hours Breakdown & Defense table justifying each phase for the viva checkpoint.
