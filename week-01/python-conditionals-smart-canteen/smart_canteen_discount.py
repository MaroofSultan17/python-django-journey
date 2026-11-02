# 1 condition - if statement
# 1 condition, 2 outputs - if-else statement
# 2 conditions, 3 outputs - if-elif-else statement

# Topic 1: Conditional Statements 
# Program 1: Smart Canteen Discount System
# Topic: if, elif, else, comparison operators, and logical thinking.
# Real-World Scenario
# Imagine a college canteen where students receive discounts based 
# on their total bill.

# The canteen follows these rules:
# - If the bill is Rs. 3,000 or more, the student receives a 
# 20% discount.
# - If the bill is Rs. 2,000 or more but less than Rs. 3,000, 
# the student receives a 10% discount.
# - If the bill is Rs. 1,000 or more but less than Rs. 2,000, 
# the student receives a 5% discount.
# - If the bill is less than Rs. 1,000, no discount is provided.
# - The program must display the original bill, discount amount,
# and final payable amount.

print("================================")
print("         SMART CANTEEN          ")
print("================================")

# Student Challenge 1: Input validation for positive bill amount
while True:
    try:
        bill_amount = float(input("Enter your total bill amount (Rs.): "))
        if bill_amount <= 0:
            print("Invalid bill amount! Please enter an amount greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Student Challenge 2: Ask for membership card with validation
while True:
    membership_input = input("Do you have a membership card? (yes/no): ").strip().lower()
    if membership_input in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

has_membership = membership_input == "yes"

# Standard tiered discount logic
if bill_amount >= 3000:
    discount_rate = 20
elif bill_amount >= 2000:
    discount_rate = 10
elif bill_amount >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount_amount = bill_amount * discount_rate / 100
amount_after_standard = bill_amount - discount_amount

# Student Challenge 2: 5% additional discount on remaining amount for members
if has_membership:
    membership_discount = amount_after_standard * 5 / 100
else:
    membership_discount = 0.0

total_savings = discount_amount + membership_discount
final_amount = bill_amount - total_savings

print("\n================================")
print("          BILL SUMMARY          ")
print("================================")
print(f"Original Bill:                 Rs. {bill_amount:.2f}")
print(f"Standard Discount ({discount_rate}%):       Rs. {discount_amount:.2f}")

if has_membership:
    print(f"Membership Discount:           Rs. {membership_discount:.2f}")

print(f"Total Savings:                 Rs. {total_savings:.2f}")
print(f"Final Payable Amount:          Rs. {final_amount:.2f}")

# Student Challenge 3: Congratulatory message when discount is applied
if total_savings > 0:
    print(f"Congratulations! You saved Rs. {total_savings:.2f}.")
else:
    print("No discount applied on this order.")
