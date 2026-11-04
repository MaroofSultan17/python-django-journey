# Assessment Task 2: Smart Pharmacy Inventory & Sales Management System
# Topic: Loop Structures (for loop, range(), conditions inside loops, counters and accumulators)

# Problem Statement:
# A pharmacy needs a console application to manage daily medicine sales and inventory.
#
# Requirements:
# 1. Ask how many different medicines need to be processed.
# 2. Use a for loop to process each medicine one by one.
# 3. Collect medicine name, available stock, price per unit, and quantity sold.
# 4. Check whether requested sales quantity is available in stock.
# 5. Calculate the total sales amount for each successful sale.
# 6. Calculate and display remaining stock after each sale.
# 7. Display a low-stock warning if remaining stock is below 10 units.
# 8. Maintain total pharmacy revenue using an accumulator.
# 9. Count how many medicines require restocking using a counter.
# 10. Generate a final summary report at the end.

print("--- Pharmacy Inventory & Sales System ---")

# ----------------------------------------------------
# Step 1: Ask how many medicines need to be processed
# ----------------------------------------------------

# Validate that medicine count is greater than 0
while True:
    total_medicines = int(input("Enter number of medicines to process: "))
    if total_medicines <= 0:
        print("Invalid number! Please enter a number greater than 0.")
    else:
        break

# ----------------------------------------------------
# Initialize Accumulator and Counter
# ----------------------------------------------------

# Accumulator: Starts at 0.0 and accumulates total sales revenue from each medicine
total_revenue = 0.0

# Counter: Starts at 0 and increments by 1 whenever a medicine has less than 10 stock
restock_count = 0

# ----------------------------------------------------
# Step 2: Process each medicine using a for loop
# ----------------------------------------------------

for i in range(1, total_medicines + 1):
    print(f"\n--- Medicine {i} of {total_medicines} ---")

    # Step 3: Collect medicine details with simple if-else validation

    # Validate medicine name (cannot be empty)
    while True:
        med_name = input("Enter medicine name: ").strip()
        if med_name == "":
            print("Medicine name cannot be empty! Please try again.")
        else:
            break

    # Validate available stock (must be 0 or positive)
    while True:
        available_stock = int(input(f"Enter available stock for {med_name}: "))
        if available_stock < 0:
            print("Stock cannot be negative! Please try again.")
        else:
            break

    # Validate price per unit (must be greater than 0)
    while True:
        unit_price = float(input(f"Enter price per unit for {med_name} (Rs.): "))
        if unit_price <= 0:
            print("Price must be greater than 0! Please try again.")
        else:
            break

    # Validate quantity sold (must be 0 or positive)
    while True:
        quantity_sold = int(input(f"Enter quantity sold for {med_name}: "))
        if quantity_sold < 0:
            print("Quantity sold cannot be negative! Please try again.")
        else:
            break

    # Step 4: Check if requested sales quantity is available in stock
    if quantity_sold <= available_stock:
        # Step 5: Sale is successful, calculate total sale amount
        sale_amount = quantity_sold * unit_price

        # Step 6: Deduct sold quantity from stock to get remaining stock
        remaining_stock = available_stock - quantity_sold

        # Step 8: Add this sale amount to the total pharmacy revenue accumulator
        total_revenue = total_revenue + sale_amount

        print(f"\nSale Successful for {med_name}!")
        print(f"Units Sold: {quantity_sold} @ Rs. {unit_price} each")
        print(f"Total Sale Amount: Rs. {sale_amount}")
        print(f"Remaining Stock: {remaining_stock} units")
    else:
        # When requested quantity is greater than available stock
        remaining_stock = available_stock
        print(f"\nSale Failed: Not enough stock for {med_name}!")
        print(f"Requested: {quantity_sold}, but available stock is only {available_stock}.")
        print(f"Remaining Stock: {remaining_stock} units")

    # Step 7 & Step 9: Low stock check and restock counter
    # If remaining stock drops below 10 units, show warning and increment counter
    if remaining_stock < 10:
        print("Warning: Low stock! This medicine requires restocking.")
        restock_count = restock_count + 1

# ----------------------------------------------------
# Step 10: Final Pharmacy Summary Report
# ----------------------------------------------------

print("\n--- Final Pharmacy Summary Report ---")
print(f"Total Medicines Processed: {total_medicines}")
print(f"Total Pharmacy Revenue: Rs. {total_revenue}")
print(f"Medicines Requiring Restocking: {restock_count}")
