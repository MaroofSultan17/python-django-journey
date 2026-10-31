# Python & Django Journey

Individual engineering repository for PSEB DEPLOY program.

---

## 1. Setup Instructions (PyCharm & Virtualenv)

This project runs locally in Python using a standard virtual environment inside PyCharm. **No Docker or containers are used.**

### PyCharm Setup Steps:
1. Open PyCharm -> **Open** -> Select `python-django-journey`.
2. Configure Python Interpreter:
   - Go to **Settings/Preferences** -> **Project: python-django-journey** -> **Python Interpreter**.
   - Click **Add Interpreter** -> **Add Local Interpreter...**
   - Select **Virtualenv Environment** -> **New** -> Location: `.venv` (Base Python: Python 3.10+ / 3.12).
   - Click **OK**.
3. Create local `.env`:
   ```bash
   cp .env.example .env
   ```
4. Install dependencies:
   ```bash
   pip install django
   ```

---

## 2. Repository Layout

```text
python-django-journey/
├── hours-log.md        <-- Master daily hours & commit verification log (MUST be at root)
├── week-01/            <-- Python core drills & algorithms
├── week-02/            <-- Django fundamentals & SQLite setup
├── week-03/            <-- Models, migrations & CRUD operations
├── week-04/            <-- Offline mock adapters & business logic
├── week-05/            <-- User auth, RBAC & sensitive data security
├── week-06/            <-- Testing, query optimization & bug fixes
├── week-07/            <-- Capstone preparation & final polish
├── .github/
│   └── pull_request_template.md
├── .env.example
├── .gitignore
└── README.md
```

---

## 3. Daily Commit Rules
- **Individual Repo**: At least 1 meaningful commit on **every class day** and **every home day**.
- **Hours Log**: Update `hours-log.md` daily. Commit timestamp MUST match the logged date.
- **Group Repo**: At least 3 meaningful commits and 1 reviewed PR per week.
- **Zero Secrets**: Never commit `.env` or API credentials.
