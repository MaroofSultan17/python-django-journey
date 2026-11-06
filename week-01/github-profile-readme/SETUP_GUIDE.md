# GitHub Profile README Setup & 3-Commit Submission Guide

This guide provides step-by-step instructions for creating your special GitHub profile repository (`MaroofSultan17`) and fulfilling the mandatory **3 separate commits with clear messages** requirement.

---

## 📋 Assessment Requirements Checklist
- [x] Repository name is exactly your GitHub username: `MaroofSultan17`
- [x] Heading with your name (`Maroof Sultan`)
- [x] Short "About me" section
- [x] "Skills" list
- [x] "Projects" section linking Week 1 repositories
- [x] Contact section with email and LinkedIn (**strictly no phone number**)
- [x] Markdown elements: Headings (`#`, `##`), Lists (`-`), Links (`[text](url)`), and Code Block (` ```python `)
- [x] Minimum 3 separate Git commits with descriptive messages

---

## 🚀 Step-by-Step Instructions

### Step 1: Create the Special Repository on GitHub
1. Open [GitHub](https://github.com/new).
2. Set **Repository name** to: `MaroofSultan17`.
   *(GitHub will display a banner: "You found a secret! MaroofSultan17 is a ✨special ✨ repository that you can use to add a README.md to your GitHub profile.")*
3. Set visibility to **Public**.
4. Check **Add a README file** (or leave unchecked if initializing from local terminal).
5. Click **Create repository**.

---

### Step 2: Fulfill the 3-Commit Requirement Locally

Open your local terminal and execute the following commands step by step:

```bash
# 1. Clone your new special profile repository
cd ~/public
git clone git@github.com:MaroofSultan17/MaroofSultan17.git
cd MaroofSultan17

# --- COMMIT 1: Base Profile & About Me ---
# Create initial README with name and about me
cat << 'EOF' > README.md
# Hi there, I'm Maroof Sultan 👋

Software Engineer specializing in Python, Django, and modern backend systems. Currently enrolled in the **PSEB DEPLOY - Python & Django Journey**.

## 👨‍💻 About Me
- 🔭 Passionate about backend architecture, clean code, and developer tooling.
- 📚 Currently mastering: Core Python, Django, SQLite, and REST APIs.
- ⚡ Development Philosophy: Smallest complete change, test-driven logic, and offline-first reliability.
EOF

git add README.md
git commit -m "docs: initialize profile README with bio and about me section"

# --- COMMIT 2: Skills & Featured Week 1 Projects ---
# Append technical skills, project links, and Python code block
cat << 'EOF' >> README.md

## 🛠️ Technical Skills
- **Languages**: Python (Core, OOP, Data Structures), JavaScript / TypeScript, SQL, HTML5 / CSS3.
- **Frameworks & Libraries**: Django, Django REST Framework.
- **Tools & Platforms**: Git, GitHub, PyCharm, Linux / macOS CLI, SQLite.

## 🚀 Featured Projects & Week 1 Milestones
- 🌟 [Python & Django Journey Repository](https://github.com/MaroofSultan17/python-django-journey)
- 📊 [Python Functions & Lists Assessment](https://github.com/MaroofSultan17/python-django-journey/tree/main/week-01/python-functions-lists-assessment)
- 💰 [Personal Expense Tracker CLI](https://github.com/MaroofSultan17/python-django-journey/tree/main/week-01/python-expense-tracker-cli)
- ⚡ [Smart Canteen & Electricity Billing Drills](https://github.com/MaroofSultan17/python-django-journey/tree/main/week-01)

## 💻 Developer Quick Bio (Python)
```python
class Developer:
    def __init__(self):
        self.name = "Maroof Sultan"
        self.role = "Python & Django Software Engineer"
        self.program = "PSEB DEPLOY Fellowship"
        self.core_stack = ["Python", "Django", "SQL", "Git"]

    def current_mission(self):
        return "Writing clean, resilient code and building real-world web apps."


dev = Developer()
print(f"{dev.name} | {dev.role} -> {dev.current_mission()}")
```
EOF

git add README.md
git commit -m "feat: add technical skills, featured week-01 projects, and bio code block"

# --- COMMIT 3: Contact Details & LMS Footer ---
# Append contact information and footer
cat << 'EOF' >> README.md

## 📬 Connect With Me
- **Email**: [maroofsultan17@gmail.com](mailto:maroofsultan17@gmail.com)
- **GitHub**: [@MaroofSultan17](https://github.com/MaroofSultan17)
- **LinkedIn**: [linkedin.com/in/maroof-sultan](https://www.linkedin.com)

---
*Generated as part of PSEB DEPLOY Week 01 Assessment.*
EOF

git add README.md
git commit -m "docs: add contact information and complete profile README"

# --- Push to Remote ---
git push origin main
```

---

## 🌐 Verify Your Public Profile
Navigate to `https://github.com/MaroofSultan17` in your browser. Your new customized README will be displayed at the top of your GitHub profile page!
