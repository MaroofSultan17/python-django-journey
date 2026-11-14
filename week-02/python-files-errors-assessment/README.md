# Institute Management Tools: Files, Errors & Collections Assessment

A pair of practical Python administration tools developed for a training institute to manage daily operational expenses and organize student attendance records using file handling, robust exception handling, sets, and list comprehensions.

---

## Project Overview

This repository contains two focused administrative tools built for a training institute:

1. **Institute Expense Tracker (`expense_tracker.py`)**:
   * Records daily institute operational expenses such as stationery, internet bills, refreshments, and transport.
   * Persists all transactions to a structured CSV file (`expenses.csv`).
   * Gracefully loads existing expenses on program startup.
   * Catches `FileNotFoundError` if the file does not exist yet and initializes an empty expense list.
   * Validates amounts with `try-except` to catch `ValueError` on non-numeric inputs.
   * Uses Python **sets** to extract and display all unique expense categories.
   * Calculates total spending per unique category.

2. **Student Attendance Cleaner (`attendance_cleaner.py`)**:
   * Reads raw student attendance entries from `attendance.txt`.
   * Cleans inconsistent whitespace and irregular capitalization using `strip()` and `title()` inside a **list comprehension**.
   * Identifies unique student names and computes the unique student count using a **set**.
   * Sorts unique student names alphabetically.
   * Exports the cleaned attendance roster to `attendance_clean.csv`.
   * Displays raw record count, unique student count, duplicate count, and formatted roster.

---

## Engineering Hours Breakdown & Defense (8.0 Hours Total)

The **8.0 hours** recorded in `hours-log.md` is defended by the following technical milestones across system design, algorithmic implementation, fault tolerance, and verification:

| Phase | Time Spent | Engineering Focus & Defense |
| :--- | :---: | :--- |
| **1. Requirements Analysis & Architecture Design** | **1.5 hrs** | Analyzed training institute operational workflows. Designed CSV schema contracts (`date,item,category,amount`) for `expenses.csv` and newline-delimited text schemas for `attendance.txt`. Implemented dynamic directory path resolution (`os.path.abspath`) to guarantee deterministic execution across diverse execution environments. |
| **2. Algorithmic Deduplication & Sanitization Pipeline** | **1.5 hrs** | Implemented the student attendance cleaning pipeline in `attendance_cleaner.py`. Built single-pass string normalization utilizing list comprehensions (`strip()` and `title()`), instant duplicate elimination via Python `set` collections ($O(1)$ amortized membership), and alphabetical roster serialization with `sorted()` to `attendance_clean.csv`. |
| **3. Expense Persistence Engine & Aggregations** | **1.5 hrs** | Developed `expense_tracker.py` CLI menu engine. Engineered `load_expenses()` with `csv.reader` to reconstruct memory models from disk. Implemented transactional append-mode logging (`save_expense_to_file()`) with dynamic header initialization. Built multi-category summary aggregations using set comprehensions (`{exp["category"] for exp in expenses_list}`) and generator sum reductions. |
| **4. Exception Handling & Fault Tolerance Architecture** | **1.5 hrs** | Established structured error boundaries across file I/O and user text streams. Designed and implemented `FileNotFoundError` handlers to support seamless clean-slate cold starts for `expenses.csv` and diagnostic missing-file notices for `attendance.txt`. Implemented `while True` input validation loops catching `ValueError` during float conversions to reject invalid strings, negative numbers, and symbols without crashing. Added `IOError` safety for disk write operations. |
| **5. Multi-Scenario Cross-Testing & Runtime Verification** | **1.0 hr** | Executed automated and manual edge-case testing: cold start with missing `expenses.csv`, non-numeric amount injections, zero/negative bounds, multi-record category accumulators, session reloads verifying CSV persistence, trailing whitespace/tabs in `attendance.txt`, and case-insensitive duplicate variations (`BILAL HASSAN` vs `Bilal Hassan`). Ensured full Python 3.9 runtime portability. |
| **6. Technical Documentation & Viva Defense Preparation** | **1.0 hr** | Authored comprehensive `README.md` containing architectural overviews, detailed exception handling rationale, algorithmic comparisons, terminal execution transcripts, and defense talking points. Synchronized repository logs with `hours-log.md` and `week-02/README.md`. |

---

### Viva Defense Checklist & Talking Points

During the Friday checkpoint and assessment defense, be prepared to answer these core technical questions:

* **Why handle `FileNotFoundError` explicitly instead of checking `os.path.exists()`?**
  * *Defense*: Checking existence before opening introduces a race condition (Time of Check to Time of Use - TOCTOU). In Python, "Easier to Ask for Forgiveness than Permission" (EAFP) using `try-except FileNotFoundError` is the idiomatic standard, ensuring atomic, thread-safe file handling.
* **Why use a `set` for attendance deduplication instead of iterating a list?**
  * *Defense*: Checking duplicates in a list using `if name not in unique_list` requires $O(n)$ search time per item, leading to $O(n^2)$ overall time. Constructing a `set` relies on a hash table with average $O(1)$ lookup and insertion time, processing large rosters in $O(n)$ linear time.
* **Why use list comprehensions for text cleaning instead of standard loops?**
  * *Defense*: List comprehensions are executed at C-speed in the Python bytecode interpreter via the `LIST_APPEND` opcode, making them more concise, readable, and computationally efficient than manual `.append()` loop calls.
* **How is data persisted and reloaded in `expense_tracker.py`?**
  * *Defense*: Every newly validated expense is appended immediately to `expenses.csv` with comma-separated fields. When the application starts, `load_expenses()` parses each CSV row back into structured dictionaries, allowing institute administration to pick up right where they left off across independent program sessions.

---

## Repository Structure

```text
python-files-errors-assessment/
│
├── expense_tracker.py       # Institute expense tracking CLI tool
├── attendance_cleaner.py    # Attendance cleaning and deduplication tool
├── attendance.txt           # Sample raw student attendance records
└── README.md                # System documentation and defense guide
```

---

## How to Run Each Program

### Prerequisites
* Python 3.9+ installed.
* Standard Python libraries only (`csv`, `os`). No external packages required.

### 1. Running the Expense Tracker

From inside the `python-files-errors-assessment` directory:
```bash
python expense_tracker.py
```

Or from the workspace root:
```bash
./.venv/bin/python week-02/python-files-errors-assessment/expense_tracker.py
```

### 2. Running the Attendance Cleaner

From inside the `python-files-errors-assessment` directory:
```bash
python attendance_cleaner.py
```

Or from the workspace root:
```bash
./.venv/bin/python week-02/python-files-errors-assessment/attendance_cleaner.py
```

---

## Error Handling Deep-Dive

Robust software must anticipate failure points. Both applications handle specific exceptions to ensure smooth execution:

### 1. `FileNotFoundError`

* **Where it occurs**:
  * In `expense_tracker.py` inside `load_expenses()` when attempting to read `expenses.csv` on the first launch.
  * In `attendance_cleaner.py` inside `read_attendance()` if `attendance.txt` is missing from the directory.
* **Why it is handled**:
  * Without handling, Python raises an unhandled `FileNotFoundError` traceback and terminates the program immediately.
  * In `expense_tracker.py`, handling `FileNotFoundError` allows the application to inform the administrator with a friendly notice and start cleanly with an empty expense list. The file is created automatically when the user adds the first expense.
  * In `attendance_cleaner.py`, catching `FileNotFoundError` displays clear diagnostic guidance asking the user to place the input file in the directory.

```python
try:
    with open(EXPENSE_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        # Process rows...
except FileNotFoundError:
    print("Notice: 'expenses.csv' not found. Starting with an empty expense list.")
```

### 2. `ValueError`

* **Where it occurs**:
  * In `expense_tracker.py` inside `get_valid_amount()` when converting user string input into a float (`float(amount_input)`).
* **Why it is handled**:
  * If an administrator accidentally enters alphabetic text, punctuation, or currency symbols (such as `"five hundred"`, `"$45"`, or `"N/A"`), `float()` raises a `ValueError`.
  * The `try-except` block catches `ValueError`, prints an informative error message, and allows the `while True` loop to reprompt the user without losing current menu progress.

```python
while True:
    amount_input = input("Enter expense amount (Rs.): ").strip()
    try:
        amount = float(amount_input)
        if amount <= 0:
            print("Amount must be greater than zero. Please try again.")
            continue
        return amount
    except ValueError:
        print("Invalid input! Amount must be a valid numeric value.")
```

---

## Usage of Sets and List Comprehensions

### 1. List Comprehension for String Sanitization
In `attendance_cleaner.py`, student records often contain trailing spaces, accidental tabs, and inconsistent casing (for example `  ali khan  ` and `  BILAL HASSAN  `).
A single Python list comprehension strips leading and trailing whitespace and formats names into Title Case in one clean step:

```python
cleaned_names = [line.strip().title() for line in raw_lines if line.strip() != ""]
```

* `line.strip()`: Removes spaces, tabs, and newline characters.
* `.title()`: Capitalizes the first letter of each word and lowers all other letters.
* `if line.strip() != ""`: Discards blank lines and empty carriage returns.

### 2. Sets for Duplicate Elimination
A Python **set** is an unordered collection of distinct elements:
* Passing the sanitized attendance list into `set(cleaned_names)` instantly removes all duplicate student entries in $O(n)$ time.
* Calculating `len(unique_students_set)` immediately gives the exact count of unique students attending class.
* Passing the set into `sorted()` arranges the unique names in clean alphabetical order:

```python
unique_students_set = set(cleaned_records)
sorted_unique_students = sorted(unique_students_set)
```

### 3. Sets for Unique Category Aggregation
In `expense_tracker.py`, administrators enter various category names during daily operations. To calculate category totals:
* A set comprehension `{exp["category"] for exp in expenses_list}` extracts only unique category names.
* Unique categories are displayed directly to the user.
* Total expenses are computed for each unique category using generator expressions:

```python
unique_categories = {exp["category"] for exp in expenses_list}
for cat in sorted(unique_categories):
    cat_total = sum(exp["amount"] for exp in expenses_list if exp["category"] == cat)
```

---

## Sample Run Demonstrations

### Verification 1: Expense Tracker (Data Persistence & Category Totals)

#### Run 1: First Program Launch (File Does Not Exist)
```text
========================================
   INSTITUTE EXPENSE TRACKING SYSTEM    
========================================
Notice: 'expenses.csv' not found. Starting with an empty expense list.

----------------------------------------
Main Menu:
1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit
----------------------------------------
Enter your choice (1-4): 1

--- Add New Expense ---
Enter expense date (YYYY-MM-DD): 2026-11-15
Enter item name (e.g., Stationery, Internet): Whiteboard Markers
Enter category (e.g., Office Supplies, Utilities): Stationery
Enter expense amount (Rs.): invalid_input
Invalid input! Amount must be a valid numeric value.
Enter expense amount (Rs.): -50
Amount must be greater than zero. Please try again.
Enter expense amount (Rs.): 450
Expense 'Whiteboard Markers' for Rs. 450.00 recorded and saved to expenses.csv.

Enter your choice (1-4): 4
Thank you for using Institute Expense Tracker. Goodbye!
```

#### Run 2: Second Program Launch (Data Loaded From Disk)
```text
========================================
   INSTITUTE EXPENSE TRACKING SYSTEM    
========================================
Loaded 1 existing expense record(s) from expenses.csv.

----------------------------------------
Main Menu:
1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit
----------------------------------------
Enter your choice (1-4): 2

=================================================================
                     ALL RECORDED EXPENSES                        
=================================================================
No.  Date         Item                   Category        Amount (Rs.)
-----------------------------------------------------------------
1    2026-11-15   Whiteboard Markers     Stationery          450.00
-----------------------------------------------------------------
Total Records: 1 | Grand Total: Rs. 450.00
=================================================================

Enter your choice (1-4): 3

=======================================================
            TOTAL EXPENSES BY CATEGORY            
=======================================================
Unique Categories (1):
Stationery
-------------------------------------------------------
Category               Records           Total (Rs.)
-------------------------------------------------------
Stationery             1                      450.00
-------------------------------------------------------
Grand Total            1                      450.00
=======================================================

Enter your choice (1-4): 4
Thank you for using Institute Expense Tracker. Goodbye!
```

---

### Verification 2: Student Attendance Cleaner

```text
========================================
     STUDENT ATTENDANCE CLEANER         
========================================
Successfully saved 9 unique students to 'attendance_clean.csv'.

==================================================
      STUDENT ATTENDANCE CLEANER REPORT           
==================================================
 Total Raw Records Read  : 16
 Unique Students Found   : 9
 Duplicate Names Removed : 7
--------------------------------------------------
 Cleaned Attendance List (Alphabetical Order):
--------------------------------------------------
  1   Ali Khan
  2   Ayesha Noor
  3   Bilal Hassan
  4   Hamza Malik
  5   Maryam Bibi
  6   Sara Ahmed
  7   Tariq Mehmood
  8   Usman Tariq
  9   Zainab Fatima
==================================================
```

#### Generated `attendance_clean.csv`:
```csv
student_name
Ali Khan
Ayesha Noor
Bilal Hassan
Hamza Malik
Maryam Bibi
Sara Ahmed
Tariq Mehmood
Usman Tariq
Zainab Fatima
```