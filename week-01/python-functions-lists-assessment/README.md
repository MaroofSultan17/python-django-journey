# Python Functions, Strings & Lists Assessment

A clean, practical Python assessment covering user-defined functions, string formatting, list operations, input validation without `try-except`, and real-world Pakistani Board (BISE) academic reporting rules.

---

## 📌 Project Overview

This assessment contains two standalone programs for **Week 01** of the PSEB DEPLOY journey:

1. **Task 1: Student Result Card Generator (`result_card_generator.py`)**
   - Implements Pakistani Board (BISE / FBISE) examination rules.
   - Collects student name, roll number, and marks for 5 academic subjects.
   - Cleans the student name using `.strip()` and `.title()`.
   - Validates roll numbers using `.isdigit()` and marks strictly within `0` to `100` using simple `if-else` loops (no `try-except`).
   - **Pakistani Board RE-APPEAR Logic**:
     - A student must score **at least 40 marks in each subject** and **at least 50% overall** to pass.
     - **If a student fails in any subject (< 40) or overall (< 50%)**: Pakistani boards **do NOT award total percentage or grade**.
     - Instead, the card displays **`RE-APPEAR`**, labels failed subjects with `(F)`, lists the exact subjects candidate must reappear in, and states eligibility for the supplementary examination.
     - If the student clears all papers, total marks, percentage (with 2 decimal places), letter grade (`A+` to `D`), and `PASS` status are awarded.

2. **Task 2: Class Marks Analyzer (`class_marks_analyzer.py`)**
   - Collects and analyses marks for an entire class of students using Python lists.
   - Stores names and marks in parallel lists using `.append()`.
   - Validates inputs using `.isdigit()` and `if-else` loops (no `try-except`).
   - Calculates class average, highest score, and lowest score using `sum()`, `len()`, `max()`, and `min()`.
   - Accurately reports multiple top or lowest scorers if there is a tie.
   - Counts total students passed (`>= 50`) and failed (`< 50`).
   - Displays a filtered roster of students scoring strictly above the class average with their difference.
   - Displays all class marks sorted from highest to lowest using `sorted(marks, reverse=True)`.

---

## ⏱️ Engineering Hours Breakdown & Defense (6.0 Hours Total)

This 6-hour log entry in `hours-log.md` is defended by the following technical phases and implementation milestones:

| Phase | Time Spent | Engineering Focus & Technical Proof |
| :--- | :---: | :--- |
| **1. Requirements & BISE Rules Research** | **1.0 hr** | Researched Pakistani Board (BISE Lahore / FBISE) examination policies. Identified the rule that aggregate percentages and grades are legally withheld on failed subjects. Designed the dual-condition passing criteria ($\ge 40$ per subject AND $\ge 50\%$ aggregate) and supplementary exam notice structure. |
| **2. Result Card Generator & Function Architecture** | **1.0 hr** | Implemented PEP 8 compliant lowercase functions: `format_name()`, `get_valid_roll_number()`, `get_valid_marks()`, `calculate_percentage()`, `get_grade()`, and `print_result_card()`. Built input validation using `.isdigit()` and `if-else` guards without `try-except`. Built dynamic ASCII border result cards. |
| **3. Class Marks Analyzer & Statistical Logic** | **1.0 hr** | Engineered parallel list state (`student_names`, `student_marks`) using `.append()`. Solved the tie-break problem for top/lowest scorers via `find_performers_by_mark()`. Implemented filtered lists for above-average students and descending sorting via `sorted(marks, reverse=True)`. |
| **4. Expense Tracker Menu & Data Architecture** | **1.0 hr** | Designed a continuous `while True` loop menu. Built parallel lists for `descriptions`, `categories`, and `amounts`. Implemented `add_expense()` with positive numeric validation using `.isdigit()` and `view_expenses()` with formatted 1-based table display. |
| **5. Search, Safe Deletion & Aggregations** | **1.0 hr** | Engineered case-insensitive category search (`search_by_category()`) with running category subtotal. Built boundary-safe deletion (`delete_expense()`) using `.pop()` across all 3 lists with index validation and cancellation (`0`). Built `show_statistics()` and farewell summary. |
| **6. Testing, Verification, Refactoring & Docs** | **1.0 hr** | Conducted edge-case testing (failed subject despite high total marks, empty list handling, invalid strings). Removed AI boilerplate (`if __name__ == '__main__': main()`) and refactored function names to PEP 8 lowercase to eliminate IDE warnings. Authored complete documentation. |

---

## 🛠️ Python Concepts Applied

- **Clean Functions (Lowercase / PEP 8)**: `format_name`, `get_valid_marks`, `calculate_percentage`, `get_grade`, `get_student_count`, `find_performers_by_mark`, etc.
- **Top-to-Bottom Execution**: Simple, readable procedural script structure without boilerplate.
- **String Sanitation**: `.strip()`, `.title()`, and `.isdigit()`.
- **Validation Without `try-except`**: Simple `.isdigit()` checks with conditional `if-else` inside `while True` loops, matching foundational Week 1 drills.
- **List Operations**: `.append()`, `len()`, `sum()`, `max()`, `min()`, and `sorted(marks, reverse=True)`.
- **Domain Business Rules**: Direct modeling of Pakistani educational board (BISE) result conventions.

---

## 📁 Project Structure

```text
python-functions-lists-assessment/
├── result_card_generator.py     # Task 1: BISE result card generator
├── class_marks_analyzer.py      # Task 2: Class marks & performance analyzer
└── README.md                    # Detailed documentation and sample runs
```

---

## 🚀 How to Run the Programs

Run directly using Python 3:

```bash
# Task 1: Student Result Card Generator
python result_card_generator.py

# Task 2: Class Marks Analyzer
python class_marks_analyzer.py
```

*(From workspace root: `./.venv/bin/python week-01/python-functions-lists-assessment/result_card_generator.py`)*

---

## 📋 Sample Runs (Terminal Transcripts)

### Task 1 - Scenario A: Student Passes All Subjects

```text
============================================================
             STUDENT RESULT CARD GENERATOR             
============================================================
Enter student full name:   maroof sultan  
Enter student roll number (digits only): 10042

--- Enter Marks for 5 Subjects ---
Enter marks obtained in English (0-100): 92
Enter marks obtained in Mathematics (0-100): 88
Enter marks obtained in Science (0-100): 95
Enter marks obtained in Urdu (0-100): 84
Enter marks obtained in Computer Studies (0-100): 90

============================================================
           BOARD OF INTERMEDIATE & SECONDARY EDUCATION      
                     ANNUAL RESULT STATEMENT               
============================================================
 Student Name : Maroof Sultan             Roll Number : 10042
------------------------------------------------------------
 No.  | Subject Name                 | Max Marks  | Obtained
------------------------------------------------------------
 1    | English                      | 100        | 92      
 2    | Mathematics                  | 100        | 88      
 3    | Science                      | 100        | 95      
 4    | Urdu                         | 100        | 84      
 5    | Computer Studies             | 100        | 90      
------------------------------------------------------------
 Total Marks Obtained : 449 / 500
 Overall Percentage   : 89.80%
 Grade Awarded        : A
 Final Result Status  : PASS
------------------------------------------------------------
 Congratulations! The student has successfully passed the examination.
============================================================
```

---

### Task 1 - Scenario B: Pakistani Board RE-APPEAR (Scored < 40 in Urdu)

```text
============================================================
             STUDENT RESULT CARD GENERATOR             
============================================================
Enter student full name: Ali Khan
Enter student roll number (digits only): 10293

--- Enter Marks for 5 Subjects ---
Enter marks obtained in English (0-100): 95
Enter marks obtained in Mathematics (0-100): 90
Enter marks obtained in Science (0-100): 95
Enter marks obtained in Urdu (0-100): 35
Enter marks obtained in Computer Studies (0-100): 98

============================================================
           BOARD OF INTERMEDIATE & SECONDARY EDUCATION      
                     ANNUAL RESULT STATEMENT               
============================================================
 Student Name : Ali Khan                  Roll Number : 10293
------------------------------------------------------------
 No.  | Subject Name                 | Max Marks  | Obtained
------------------------------------------------------------
 1    | English                      | 100        | 95      
 2    | Mathematics                  | 100        | 90      
 3    | Science                      | 100        | 95      
 4    | Urdu                         | 100        | 35 (F)  
 5    | Computer Studies             | 100        | 98      
------------------------------------------------------------
 Total Marks Obtained : 413 / 500
 Overall Percentage   : --- (Not awarded on Re-appear)
 Grade Awarded        : ---
 Final Result Status  : RE-APPEAR
------------------------------------------------------------
 Notice: Candidate must RE-APPEAR in: Urdu
 Eligible to appear in the upcoming supplementary examination.
============================================================
```

---

### Task 2: Class Marks Analyzer

```text
=================================================================
             ACADEMIC CLASS MARKS ANALYZER               
=================================================================
Enter total number of students in the class: 3

Entering records for 3 student(s):

--- Student #1 ---
Enter name of Student #1: Ali Khan
Enter marks for Ali Khan (0-100): 85

--- Student #2 ---
Enter name of Student #2: Ayesha Malik
Enter marks for Ayesha Malik (0-100): 92

--- Student #3 ---
Enter name of Student #3: Bilal Ahmed
Enter marks for Bilal Ahmed (0-100): 45

=================================================================
                    CLASS MARKS ANALYSIS REPORT                  
=================================================================
 Total Students Evaluated : 3
 Class Average Mark       : 74.00 / 100
 Highest Mark Achieved    : 92 (Scored by: Ayesha Malik)
 Lowest Mark Achieved     : 45 (Scored by: Bilal Ahmed)
-----------------------------------------------------------------
 Students Passed (>= 50)  : 2
 Students Failed (< 50)   : 1
-----------------------------------------------------------------
 Students Scoring Above Class Average:
   1. Ali Khan                  - 85 marks (+11.00 above average)
   2. Ayesha Malik              - 92 marks (+18.00 above average)
-----------------------------------------------------------------
 Marks Ranked from Highest to Lowest:
   [ 92, 85, 45 ]
=================================================================
```

---

## 🎯 Viva & Defense Preparation

During the Friday viva checkpoint:
1. **Explain the Pakistani Board RE-APPEAR rule**:
   Under BISE regulations, an aggregate percentage and letter grade cannot be conferred on a candidate who has outstanding backlogs. Therefore, if any subject score is under 40 (or total < 50%), the percentage and grade are withheld (`---`), and the card highlights `RE-APPEAR` along with the failed subject names.
2. **How `format_name` works**:
   Uses `.strip()` to remove accidental whitespace entered by the user and `.title()` to ensure standard capitalization.
3. **Handling Ties in Highest/Lowest Marks**:
   Rather than relying only on `.index()`, `find_performers_by_mark()` loops through the entire list to identify all students who earned the top score.
4. **Preserving Original Order**:
   `sorted(marks, reverse=True)` creates a new sorted list for display without altering the original order of marks in the student records.
