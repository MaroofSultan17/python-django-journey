# Python & Django Journey

This repository houses the individual weekly coding drills, exercises, and project milestones for the PSEB DEPLOY program.

---

## Project Overview

- **Stack:** Python 3.10+ / Django 5.x
- **Database:** SQLite
- **Environment:** Local Virtual Environment (`.venv`) managed via PyCharm
- **Architecture:** Offline-First with rule-based mock adapters

---

## Local Setup with PyCharm

### 1. Virtual Environment Setup
Open your terminal in the project root and create the local virtual environment:
```bash
python3 -m venv .venv
```

### 2. Configure Interpreter in PyCharm
1. Open PyCharm and select the `python-django-journey` folder.
2. Navigate to **Settings / Preferences** -> **Project: python-django-journey** -> **Python Interpreter**.
3. Click **Add Interpreter** -> **Add Local Interpreter...**
4. Choose **Existing** or **Virtualenv Environment** pointing to `.venv/bin/python`.
5. Apply and save.

### 3. Environment Variables
Create your local environment file from the template:
```bash
cp .env.example .env
```

---

## Weekly Progress & Layout

```text
python-django-journey/
├── hours-log.md                  # Master daily hours & commit verification log (root)
├── pull-request-template.md      # 3-line Pull Request format
├── .env.example                  # Environment template (no secrets)
├── .gitignore                    # Python, .venv, .idea, and .env exclusions
├── week-01/                      # Python Core Drills, Git SOP & Environment Setup
├── week-02/                      # Django Fundamentals, URL Routing & Basic Views
├── week-03/                      # Django Models, SQLite Migrations & Admin Panel
├── week-04/                      # Service Layer & Rule-Based Offline Mock Adapters
├── week-05/                      # User Authentication, RBAC & Sensitive Data Security
├── week-06/                      # Automated Testing, SQL Optimization & Code Review
└── week-07/                      # Capstone Project Polish, Documentation & Viva Prep
```

---

## Daily Workflow & Git Governance

1. **Daily Commit:** Make at least 1 meaningful commit on every class day and every home day.
2. **Hours Tracking:** Log daily entries in `hours-log.md`. Commit timestamp must strictly match the logged date.
3. **Pull Requests:** All PRs must adhere strictly to the 3-line format:
   1. What changed
   2. How it was tested
   3. Who reviewed it
4. **Zero-Leak Security:** Never commit `.env` or live credentials to version control.
