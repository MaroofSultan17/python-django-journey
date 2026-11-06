# Personal Expense Tracker CLI Application

A simple, user-friendly command-line application in Python that helps manage daily expenses, calculate real-time totals and averages, search by category, and delete items using simple `if-else` validation (no `try-except`).

---

## 📌 Project Overview

The **Personal Expense Tracker CLI** is built for **Week 01** of the PSEB DEPLOY journey. It brings together all core concepts learned in the first week:
- Menu loops using `while True`.
- PEP 8 compliant lowercase function naming (`display_menu`, `add_expense`, `view_expenses`, `show_statistics`, `search_by_category`, `delete_expense`, `print_goodbye_summary`).
- Parallel lists (`descriptions`, `categories`, `amounts`) for simple data management.
- Complete input validation using `.isdigit()` and `if-else` statements (no `try-except`).
- Case-insensitive category search (`.lower()`).
- Deletion by line number with index checking and cancellation support (`0`).

---

## ⏱️ Engineering Hours Breakdown & Defense (6.0 Hours Total)

The 6.0 hours logged in `hours-log.md` is defended by the following technical phases and implementation milestones:

| Phase | Time Spent | Engineering Focus & Technical Proof |
| :--- | :---: | :--- |
| **1. Requirements & System Design** | **1.0 hr** | Planned the menu structure, parallel list state representation (`descriptions`, `categories`, `amounts`), and defensive validation requirements. Designed positive numeric checks and empty-string protections without `try-except`. |
| **2. Result Card Generator & Functions (Assessment 1)** | **1.0 hr** | Built Pakistani Board (BISE) result card with `format_name`, `get_valid_marks`, `calculate_percentage`, `get_grade`, and `RE-APPEAR` logic. |
| **3. Class Marks Analyzer (Assessment 1)** | **1.0 hr** | Implemented list operations (`sum`, `len`, `max`, `min`, `sorted`), tie-breaker detection for top performers, and above-average student filtering using lowercase functions. |
| **4. Expense Tracker Menu & Entry Workflows** | **1.0 hr** | Built continuous `while True` loop menu with choices 1–6. Coded `add_expense()` with positive amount constraints and title-cased categories. Implemented `view_expenses()` with formatted tabular display and running totals. |
| **5. Search, Safe Deletion & Aggregations** | **1.0 hr** | Implemented case-insensitive category filtering (`search_by_category()`) with category subtotal summation. Built index-validated deletion (`delete_expense()`) with cancellation (`0`) and parallel list popping (`pop()`). Implemented `show_statistics()` and exit summary. |
| **6. Verification, PEP 8 Refactoring & Docs** | **1.0 hr** | Validated zero runtime warnings by converting function names to lowercase (`snake_case`). Replaced `try-except` blocks with simple `.isdigit()` checks matching earlier Week 1 drills. Authored full README documentation and sample runs. |

---

## 🚀 Menu Features

1. **Add Expense**:
   - Asks for description (cannot be empty).
   - Asks for category (formatted with `.title()`).
   - Asks for amount in PKR (must be positive number, validated with `.isdigit()`).
2. **View All Expenses**:
   - Shows all items in a formatted table with item numbers and total spent.
3. **Show Total and Average**:
   - Calculates total spent, average expense, and highest single expense.
4. **Search by Category**:
   - Searches regardless of capital or small letters (`.lower()`).
   - Shows matching expenses and their subtotal.
5. **Delete an Expense**:
   - Deletes an item by its number with safety checks.
6. **Exit**:
   - Exits the loop and displays a goodbye summary of expenses tracked.

---

## 🛠️ Python Concepts Applied

- **Functions (Lowercase / PEP 8)**: `display_menu`, `add_expense`, `view_expenses`, `show_statistics`, `search_by_category`, `delete_expense`, `print_goodbye_summary`.
- **Procedural Scripting**: Simple top-to-bottom execution that is straightforward for anyone to read and explain.
- **Lists**: Storing and managing data using `.append()` and `.pop()`.
- **String Methods**: `.strip()`, `.title()`, and `.lower()`.
- **Math Built-ins**: `sum()`, `len()`, and `max()`.
- **Validation Without `try-except`**: Clean `.isdigit()` checks with conditional `if-else` guards inside `while True` loops.

---

## 📁 Project Structure

```text
python-expense-tracker-cli/
├── expense_tracker.py       # Main CLI application
└── README.md                # Documentation and sample run
```

---

## 💻 How to Run

```bash
python expense_tracker.py
```

*(From workspace root: `./.venv/bin/python week-01/python-expense-tracker-cli/expense_tracker.py`)*

---

## 📋 Sample Run (Terminal Transcript)

```text
==================================================
             PERSONAL EXPENSE TRACKER             
==================================================
  1. Add Expense
  2. View All Expenses
  3. Show Total and Average
  4. Search by Category
  5. Delete an Expense
  6. Exit
==================================================
Enter your choice (1-6): 1

--- Add New Expense ---
Enter expense description (e.g., Lunch, Bus Fare): Biryani Lunch
Enter expense category (e.g., Food, Travel, Utilities): Food
Enter expense amount in PKR (Rs.): 450
  [Added] Biryani Lunch (Food) - Rs. 450.00

==================================================
             PERSONAL EXPENSE TRACKER             
==================================================
  1. Add Expense
  2. View All Expenses
  3. Show Total and Average
  4. Search by Category
  5. Delete an Expense
  6. Exit
==================================================
Enter your choice (1-6): 1

--- Add New Expense ---
Enter expense description (e.g., Lunch, Bus Fare): Metro Card Recharge
Enter expense category (e.g., Food, Travel, Utilities): Travel
Enter expense amount in PKR (Rs.): 500
  [Added] Metro Card Recharge (Travel) - Rs. 500.00

==================================================
             PERSONAL EXPENSE TRACKER             
==================================================
  1. Add Expense
  2. View All Expenses
  3. Show Total and Average
  4. Search by Category
  5. Delete an Expense
  6. Exit
==================================================
Enter your choice (1-6): 2

--------------------------------------------------------------
 No.  | Description              | Category       | Amount (Rs.)
--------------------------------------------------------------
 1    | Biryani Lunch            | Food           |       450.00
 2    | Metro Card Recharge      | Travel         |       500.00
--------------------------------------------------------------
 Total Entries: 2 | Grand Total: Rs. 950.00

==================================================
             PERSONAL EXPENSE TRACKER             
==================================================
  1. Add Expense
  2. View All Expenses
  3. Show Total and Average
  4. Search by Category
  5. Delete an Expense
  6. Exit
==================================================
Enter your choice (1-6): 3

=============================================
         EXPENSE SUMMARY & STATISTICS         
=============================================
 Total Expenses Recorded : 2
 Total Amount Spent      : Rs. 950.00
 Average Expense Amount  : Rs. 475.00
 Biggest Single Expense  : Rs. 500.00
=============================================

==================================================
             PERSONAL EXPENSE TRACKER             
==================================================
  1. Add Expense
  2. View All Expenses
  3. Show Total and Average
  4. Search by Category
  5. Delete an Expense
  6. Exit
==================================================
Enter your choice (1-6): 4

Enter category name to search: food

--- Search Results for Category: 'food' ---
--------------------------------------------------------------
 No.  | Description              | Category       | Amount (Rs.)
--------------------------------------------------------------
 1    | Biryani Lunch            | Food           |       450.00
--------------------------------------------------------------
 Matches: 1 | Subtotal: Rs. 450.00

==================================================
             PERSONAL EXPENSE TRACKER             
==================================================
  1. Add Expense
  2. View All Expenses
  3. Show Total and Average
  4. Search by Category
  5. Delete an Expense
  6. Exit
==================================================
Enter your choice (1-6): 6

==================================================
       THANK YOU FOR USING EXPENSE TRACKER        
==================================================
 Total Expenses Tracked : 2
 Grand Total Amount     : Rs. 950.00
 Average Per Expense    : Rs. 475.00
 Goodbye and keep managing your daily finances wisely!
==================================================
```

---

## 🎯 Viva & Defense Preparation

1. **Parallel Lists**: `descriptions`, `categories`, and `amounts` all share the exact same index `i`.
2. **Deleting Safely**: Subtract `1` from user input to get the 0-based Python index, then call `.pop(index)` on all three lists.
3. **Case-Insensitive Search**: Both the search term and the category are converted with `.lower()` before checking with `in`.
4. **Validation Without `try-except`**: Clean `.isdigit()` checks with conditional `if-else` guards to prevent crashes.
