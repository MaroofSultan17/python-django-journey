# Python Conditions & Loops Assessment

A practical assessment covering conditional decision-making, loop structures, accumulators, counters, and input validation in Python.

---

## Project Overview

This repository / assessment folder contains two separate Python console applications developed as part of Week 01 practical evaluation:
1. **Student Scholarship Evaluation System (`student_scholarship_system.py`)**: Evaluates a student's eligibility for academic scholarships using multi-condition branching.
2. **Smart Pharmacy Inventory & Sales Management System (`pharmacy_inventory_system.py`)**: Tracks medicine sales, updates stock levels, alerts on low inventory, and accumulates daily revenue using loop structures.

---

## Required Project Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

---

## 1. Description of Both Applications

### Task 1: Student Scholarship Evaluation System (`student_scholarship_system.py`)
An educational institution automates its scholarship evaluation based on merit and financial need:
- **Eligibility Conditions**:
  - Academic marks must be at least 80% (assuming max score is 100).
  - Attendance must be at least 85% (assuming max attendance is 100%).
  - Monthly family income must be Rs. 50,000 or less.
- **Scholarship Tiers (if eligible)**:
  - Marks $\ge$ 90%: **Full Scholarship**.
  - Marks between 80% and 89%: **Partial Scholarship**.
- **Ineligibility Handling**:
  - Gathers all specific criteria that were not met into a list and presents clear feedback.
- **Complete Report**:
  - Prints student name, academic marks, attendance, family income, status, and congratulatory or reason messages.

### Task 2: Smart Pharmacy Inventory & Sales Management System (`pharmacy_inventory_system.py`)
A pharmacy console program that processes sales transactions and manages medicine inventory:
- Asks how many medicines need to be processed.
- Uses a `for` loop with `range()` to process each medicine sequentially.
- Collects medicine name, available stock, unit price, and quantity sold with validation.
- Verifies stock availability (`quantity_sold <= available_stock`):
  - If available: calculates sale amount, updates remaining stock, and adds to total revenue accumulator.
  - If insufficient: rejects transaction and preserves current stock.
- Checks for low stock (`remaining_stock < 10`), displays a warning, and increments restock counter.
- Generates a final summary report showing total processed, total daily revenue, and medicines requiring restock.

---

## 2. Python Concepts & Programming Techniques Used

- **Conditional Branching (`if`, `elif`, `else`)**:
  - Evaluating scholarship tiers and validating business criteria.
  - Comparing requested sales quantity against available stock.
- **Loop Structures (`for` & `while`)**:
  - `while True` loops with `if-else` for input validation.
  - `for` loop with `range(1, total_medicines + 1)` for batch processing items.
- **Accumulators & Running Totals**:
  - `total_revenue = total_revenue + sale_amount` to accumulate sales across loop iterations.
- **Counters**:
  - `restock_count = restock_count + 1` to track low-stock items.
- **Comparison & Logical Operators**:
  - `>=`, `<=`, `<`, `>`, `==`, `and`, `or`.
- **Data Collections**:
  - Python `list` to track and report multiple ineligibility reasons dynamically.
- **Input & Formatting**:
  - `input()`, `int()`, `float()`, string methods (`.strip()`), and formatted f-strings.

---

## 3. Instructions for Running Both Programs

### Prerequisites
- Python 3.8 or higher installed on your computer.

### Step-by-Step Execution

1. Open your terminal or PyCharm terminal.
2. Navigate to the project directory:
   ```bash
   cd week-01/python-conditions-loops-assessment
   ```
3. Run Task 1 (Student Scholarship System):
   ```bash
   python student_scholarship_system.py
   ```
4. Run Task 2 (Pharmacy Inventory System):
   ```bash
   python pharmacy_inventory_system.py
   ```

*(Note: On macOS or Linux systems, use `python3` instead of `python` if needed).*

---

## 4. Example Input / Output & Sample Execution Details

### Task 1: Sample Execution (Eligible — Full Scholarship)
```text
--- Student Scholarship System ---
Enter student name: Ali Khan
Enter academic marks (0-100): 94
Enter attendance percentage (0-100): 90
Enter monthly family income (Rs.): 42000

--- Scholarship Evaluation Report ---
Student Name: Ali Khan
Academic Marks: 94.0%
Attendance: 90.0%
Monthly Income: Rs. 42000.0
Eligibility Status: Full Scholarship

Result: Congratulations Ali Khan! You are awarded a Full Scholarship.
```

### Task 1: Sample Execution (Ineligible — Multiple Reasons)
```text
--- Student Scholarship System ---
Enter student name: Bilal Ahmed
Enter academic marks (0-100): 75
Enter attendance percentage (0-100): 80
Enter monthly family income (Rs.): 60000

--- Scholarship Evaluation Report ---
Student Name: Bilal Ahmed
Academic Marks: 75.0%
Attendance: 80.0%
Monthly Income: Rs. 60000.0
Eligibility Status: Not Eligible

Result: Sorry Bilal Ahmed, you are not eligible for a scholarship.
Reasons for Ineligibility:
- Academic marks (75.0%) are below the required 80%.
- Attendance (80.0%) are below the required 85%.
- Monthly income (Rs. 60000.0) exceeds Rs. 50,000.
```

### Task 2: Sample Execution (Pharmacy Inventory System)
```text
--- Pharmacy Inventory & Sales System ---
Enter number of medicines to process: 2

--- Medicine 1 of 2 ---
Enter medicine name: Panadol
Enter available stock for Panadol: 50
Enter price per unit for Panadol (Rs.): 5
Enter quantity sold for Panadol: 10

Sale Successful for Panadol!
Units Sold: 10 @ Rs. 5.0 each
Total Sale Amount: Rs. 50.0
Remaining Stock: 40 units

--- Medicine 2 of 2 ---
Enter medicine name: Augmentin
Enter available stock for Augmentin: 12
Enter price per unit for Augmentin (Rs.): 250
Enter quantity sold for Augmentin: 5

Sale Successful for Augmentin!
Units Sold: 5 @ Rs. 250.0 each
Total Sale Amount: Rs. 1250.0
Remaining Stock: 7 units
Warning: Low stock! This medicine requires restocking.

--- Final Pharmacy Summary Report ---
Total Medicines Processed: 2
Total Pharmacy Revenue: Rs. 1300.0
Medicines Requiring Restocking: 1
```
