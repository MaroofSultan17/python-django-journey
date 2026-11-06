# Assessment: Mini CLI App and GitHub Profile README - Task 1
# Personal Expense Tracker CLI Application
# Topic: While loop menu, conditionals, functions, strings, lists, and input validation


def display_menu():
    # Displays the main numbered menu options to the user
    print("\n" + "=" * 50)
    print("             PERSONAL EXPENSE TRACKER             ")
    print("=" * 50)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Show Total and Average")
    print("  4. Search by Category")
    print("  5. Delete an Expense")
    print("  6. Exit")
    print("=" * 50)


def add_expense(descriptions, categories, amounts):
    # Asks for expense details, validates positive amount without try-except, and adds to lists
    print("\n--- Add New Expense ---")

    # Get description (cannot be empty)
    while True:
        desc = input("Enter expense description (e.g., Lunch, Bus Fare): ").strip()
        if desc == "":
            print("  Description cannot be empty. Please try again.")
        else:
            break

    # Get category (cannot be empty)
    while True:
        cat = input("Enter expense category (e.g., Food, Travel, Utilities): ").strip()
        if cat == "":
            print("  Category cannot be empty. Please try again.")
        else:
            clean_cat = cat.title()
            break

    # Get positive amount (validated with isdigit, no try-except)
    while True:
        amount_input = input("Enter expense amount in PKR (Rs.): ").strip()
        if amount_input.isdigit():
            amt = int(amount_input)
            if amt > 0:
                break
            else:
                print("  Amount must be a positive number greater than 0.")
        else:
            print("  Invalid amount! Please enter a valid number greater than 0.")

    descriptions.append(desc)
    categories.append(clean_cat)
    amounts.append(amt)

    print(f"  [Added] {desc} ({clean_cat}) - Rs. {amt:,.2f}")


def view_expenses(descriptions, categories, amounts):
    # Shows all recorded expenses in a neat table
    if len(descriptions) == 0:
        print("\n  No expenses recorded yet. Choose Option 1 to add one.")
        return

    print("\n" + "-" * 62)
    print(f" {'No.':<4} | {'Description':<24} | {'Category':<14} | {'Amount (Rs.)':>12}")
    print("-" * 62)
    for i in range(len(descriptions)):
        print(f" {i + 1:<4} | {descriptions[i]:<24} | {categories[i]:<14} | {amounts[i]:>12,.2f}")
    print("-" * 62)
    print(f" Total Entries: {len(descriptions)} | Grand Total: Rs. {sum(amounts):,.2f}")


def show_statistics(amounts):
    # Calculates and displays total spent, average, and highest expense
    if len(amounts) == 0:
        print("\n  No expenses recorded yet to show statistics.")
        return

    total_spent = sum(amounts)
    avg_expense = total_spent / len(amounts)
    biggest_expense = max(amounts)

    print("\n" + "=" * 45)
    print("         EXPENSE SUMMARY & STATISTICS         ")
    print("=" * 45)
    print(f" Total Expenses Recorded : {len(amounts)}")
    print(f" Total Amount Spent      : Rs. {total_spent:,.2f}")
    print(f" Average Expense Amount  : Rs. {avg_expense:,.2f}")
    print(f" Biggest Single Expense  : Rs. {biggest_expense:,.2f}")
    print("=" * 45)


def search_by_category(descriptions, categories, amounts):
    # Searches expenses by category without caring about uppercase or lowercase
    if len(descriptions) == 0:
        print("\n  No expenses recorded yet to search.")
        return

    query = input("\nEnter category name to search: ").strip()
    if query == "":
        print("  Search query cannot be empty.")
        return

    query_lower = query.lower()
    matches = []
    category_total = 0.0

    for i in range(len(categories)):
        if query_lower in categories[i].lower():
            matches.append(i)
            category_total += amounts[i]

    if len(matches) == 0:
        print(f"\n  No expenses found in category: '{query}'.")
    else:
        print(f"\n--- Search Results for Category: '{query}' ---")
        print("-" * 62)
        print(f" {'No.':<4} | {'Description':<24} | {'Category':<14} | {'Amount (Rs.)':>12}")
        print("-" * 62)
        for idx in matches:
            print(f" {idx + 1:<4} | {descriptions[idx]:<24} | {categories[idx]:<14} | {amounts[idx]:>12,.2f}")
        print("-" * 62)
        print(f" Matches: {len(matches)} | Subtotal: Rs. {category_total:,.2f}")


def delete_expense(descriptions, categories, amounts):
    # Deletes an expense by its number with isdigit and boundary check, no try-except
    if len(descriptions) == 0:
        print("\n  No expenses recorded yet. Nothing to delete.")
        return

    view_expenses(descriptions, categories, amounts)

    choice_input = input("\nEnter expense number to delete (or 0 to cancel): ").strip()
    if choice_input == "0":
        print("  Deletion cancelled.")
        return

    if choice_input.isdigit():
        expense_number = int(choice_input)
        if 1 <= expense_number <= len(descriptions):
            remove_index = expense_number - 1
            deleted_desc = descriptions.pop(remove_index)
            deleted_cat = categories.pop(remove_index)
            deleted_amt = amounts.pop(remove_index)
            print(f"  [Deleted] Expense #{expense_number}: '{deleted_desc}' ({deleted_cat}) - Rs. {deleted_amt:,.2f}")
        else:
            print(f"  Invalid expense number! Please choose a number between 1 and {len(descriptions)}.")
    else:
        print("  Invalid input! Please enter a whole number.")


def print_goodbye_summary(descriptions, amounts):
    # Prints a polite exit summary when the user leaves the program
    total_spent = sum(amounts) if len(amounts) > 0 else 0.0
    count = len(descriptions)

    print("\n" + "=" * 50)
    print("       THANK YOU FOR USING EXPENSE TRACKER        ")
    print("=" * 50)
    print(f" Total Expenses Tracked : {count}")
    print(f" Grand Total Amount     : Rs. {total_spent:,.2f}")
    if count > 0:
        print(f" Average Per Expense    : Rs. {(total_spent / count):,.2f}")
    print(" Goodbye and keep managing your daily finances wisely!")
    print("=" * 50 + "\n")


# ----------------------------------------------------
# Main Program Execution
# ----------------------------------------------------

descriptions = []
categories = []
amounts = []

while True:
    display_menu()
    user_choice = input("Enter your choice (1-6): ").strip()

    if user_choice == "1":
        add_expense(descriptions, categories, amounts)
    elif user_choice == "2":
        view_expenses(descriptions, categories, amounts)
    elif user_choice == "3":
        show_statistics(amounts)
    elif user_choice == "4":
        search_by_category(descriptions, categories, amounts)
    elif user_choice == "5":
        delete_expense(descriptions, categories, amounts)
    elif user_choice == "6":
        print_goodbye_summary(descriptions, amounts)
        break
    else:
        print("  Invalid menu choice! Please select an option between 1 and 6.")
