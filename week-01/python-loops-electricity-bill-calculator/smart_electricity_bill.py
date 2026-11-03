# Program 2: Smart Electricity Bill Calculator
# Topic: for loop, range(), accumulators, and conditional statements inside loops.

# Real-World Scenario
# Imagine an electricity company that wants to calculate the monthly electricity bills of multiple households.
# Instead of writing the same code repeatedly for every household, the company wants a program that:
# 1. Asks how many households need their bills calculated.
# 2. Takes the electricity units consumed by each household.
# 3. Calculates the bill using the following rates:
#    - First 100 units: Rs. 10 per unit.
#    - Next 100 units (101–200): Rs. 15 per unit.
#    - Units above 200: Rs. 20 per unit.
# 4. Calculates the total bill for every household.
# 5. Displays the combined electricity revenue collected from all households.
# Important: These rates are fictional and intended for programming practice, not actual electricity tariffs.

print("===== ELECTRICITY BILL SYSTEM =====")

# Student Challenge 1 & 2: Validate number of households (> 0 and valid integer)
while True:
    try:
        households = int(input("Enter the number of households: "))
        if households <= 0:
            print("Invalid number! Please enter a number of households greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

# Accumulators and tracking variables
# Challenge 7 Note: total_revenue must be initialized before the loop so it can accumulate
# values across all iterations without being reset or causing an UnboundLocalError.
total_revenue = 0
valid_households_count = 0
highest_bill = 0.0
highest_bill_household = None

# Process each household using a for loop
for household in range(1, households + 1):
    print(f"\n--- Household {household} ---")

    # Student Challenge 2: Handle non-numeric input using try and except
    try:
        units = int(input("Enter electricity units consumed: "))
    except ValueError:
        print("Invalid input! Please enter a valid non-negative integer.")
        # Challenge 8 Note: continue skips the remainder of this iteration and moves to the next household
        continue

    # Skip negative unit values
    if units < 0:
        print("Invalid units! Please enter a non-negative value.")
        continue

    # Progressive tiered bill calculation
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)
    else:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    print(f"Units Consumed: {units}")
    print(f"Electricity Bill: Rs. {bill}")

    # Accumulate total revenue and count valid calculations (Challenge 3)
    total_revenue += bill
    valid_households_count += 1

    # Student Challenge 4 & 6: Track highest bill and corresponding household
    if bill > highest_bill:
        highest_bill = bill
        highest_bill_household = household

# Final Monthly Summary Report
print("\n===== MONTHLY REVENUE REPORT =====")
print(f"Households Processed:          {households}")
print(f"Bills Successfully Calculated: {valid_households_count}")
print(f"Total Revenue:                 Rs. {total_revenue}")

# Student Challenge 5: Average bill calculation for valid entries
if valid_households_count > 0:
    average_bill = total_revenue / valid_households_count
    print(f"Average Household Bill:        Rs. {average_bill:.2f}")
    if highest_bill_household is not None:
        print(f"Highest Bill:                  Rs. {highest_bill} (Household {highest_bill_household})")
else:
    print("No valid bills were processed.")
