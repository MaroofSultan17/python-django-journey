# Institute Expense Tracking System
# Topic: File Handling (CSV), Exception Handling, Sets, and Comprehensions

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSE_FILE = os.path.join(BASE_DIR, "expenses.csv")


def load_expenses():
    # Loads previously saved expenses from expenses.csv
    # Catches FileNotFoundError if the file does not exist
    expenses_list = []
    try:
        with open(EXPENSE_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if len(row) >= 4:
                    expenses_list.append({
                        "date": row[0].strip(),
                        "item": row[1].strip(),
                        "category": row[2].strip(),
                        "amount": float(row[3].strip())
                    })
        print(f"Loaded {len(expenses_list)} existing expense record(s) from expenses.csv.")
    except FileNotFoundError:
        print("Notice: 'expenses.csv' not found. Starting with an empty expense list.")
    return expenses_list


def save_expense_to_file(expense):
    # Saves a newly added expense dictionary to expenses.csv
    file_exists = os.path.isfile(EXPENSE_FILE)
    with open(EXPENSE_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists or os.path.getsize(EXPENSE_FILE) == 0:
            writer.writerow(["date", "item", "category", "amount"])
        writer.writerow([
            expense["date"],
            expense["item"],
            expense["category"],
            expense["amount"]
        ])


def get_valid_amount():
    # Prompts for expense amount and catches ValueError if input is not a number
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


def add_expense(expenses_list):
    # Prompts user for date, item name, category, and amount, then saves to file
    print("\n--- Add New Expense ---")

    while True:
        date = input("Enter expense date (YYYY-MM-DD): ").strip()
        if date != "":
            break
        print("Expense date cannot be empty.")

    while True:
        item = input("Enter item name (e.g., Stationery, Internet): ").strip().title()
        if item != "":
            break
        print("Item name cannot be empty.")

    while True:
        category = input("Enter category (e.g., Office Supplies, Utilities): ").strip().title()
        if category != "":
            break
        print("Category cannot be empty.")

    amount = get_valid_amount()

    new_expense = {
        "date": date,
        "item": item,
        "category": category,
        "amount": amount
    }

    expenses_list.append(new_expense)
    save_expense_to_file(new_expense)
    print(f"Expense '{item}' for Rs. {amount:,.2f} recorded and saved to expenses.csv.")


def show_all_expenses(expenses_list):
    # Displays all recorded expenses in a clean formatted table
    if len(expenses_list) == 0:
        print("\nNo expenses recorded yet. Choose Option 1 to add one.")
        return

    print("\n" + "=" * 65)
    print("                     ALL RECORDED EXPENSES                        ")
    print("=" * 65)
    print(f"{'No.':<4} {'Date':<12} {'Item':<22} {'Category':<15} {'Amount (Rs.)':>10}")
    print("-" * 65)
    total_amount = 0.0
    for idx, exp in enumerate(expenses_list, 1):
        print(f"{idx:<4} {exp['date']:<12} {exp['item']:<22} {exp['category']:<15} {exp['amount']:>10.2f}")
        total_amount += exp["amount"]
    print("-" * 65)
    print(f"Total Records: {len(expenses_list)} | Grand Total: Rs. {total_amount:,.2f}")
    print("=" * 65)


def calculate_expenses_by_category(expenses_list):
    # Uses a set to identify unique categories and calculates totals for each
    if len(expenses_list) == 0:
        print("\nNo expenses recorded yet. Nothing to calculate.")
        return

    # Use a set to extract unique categories
    unique_categories = {exp["category"] for exp in expenses_list}

    print("\n" + "=" * 55)
    print("            TOTAL EXPENSES BY CATEGORY            ")
    print("=" * 55)
    print(f"Unique Categories ({len(unique_categories)}):")
    print(", ".join(sorted(unique_categories)))
    print("-" * 55)
    print(f"{'Category':<22} {'Records':<10} {'Total (Rs.)':>18}")
    print("-" * 55)

    grand_total = 0.0
    for cat in sorted(unique_categories):
        cat_total = sum(exp["amount"] for exp in expenses_list if exp["category"] == cat)
        cat_count = sum(1 for exp in expenses_list if exp["category"] == cat)
        grand_total += cat_total
        print(f"{cat:<22} {cat_count:<10} {cat_total:>18,.2f}")

    print("-" * 55)
    print(f"{'Grand Total':<22} {len(expenses_list):<10} {grand_total:>18,.2f}")
    print("=" * 55)


# ----------------------------------------------------
# Main Program Execution
# ----------------------------------------------------

print("\n========================================")
print("   INSTITUTE EXPENSE TRACKING SYSTEM    ")
print("========================================")

expenses = load_expenses()

while True:
    print("\n----------------------------------------")
    print("Main Menu:")
    print("1. Add New Expense")
    print("2. Show All Expenses")
    print("3. Calculate Total Expenses by Category")
    print("4. Exit")
    print("----------------------------------------")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_all_expenses(expenses)
    elif choice == "3":
        calculate_expenses_by_category(expenses)
    elif choice == "4":
        print("\nThank you for using Institute Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice! Please select an option between 1 and 4.")
