# Smart Grocery Store Management System
# Topic: Lists of Dictionaries, Data Validation, Stock Management, and Sales Reporting

# 1. Product Inventory (List of Dictionaries)
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Rice", "category": "Grains", "price": 380, "stock": 40},
    {"id": 103, "name": "Cooking Oil", "category": "Oil", "price": 520, "stock": 15},
    {"id": 104, "name": "Eggs", "category": "Poultry", "price": 320, "stock": 4},
]

# 2. Sales Records (List of Dictionaries)
sales_records = []


def add_product():
    # Adds a new product dictionary to products list
    print("\n--- Add New Product ---")
    p_id = input("Enter Product ID: ").strip()
    if not p_id.isdigit():
        print("Invalid ID! Please enter numbers only.")
        return

    p_id = int(p_id)
    # Check if ID already exists
    for p in products:
        if p["id"] == p_id:
            print("Product ID already exists! Please use a unique ID.")
            return

    name = input("Enter Product Name: ").strip().title()
    category = input("Enter Category: ").strip().title()
    price = input("Enter Price (Rs.): ").strip()
    stock = input("Enter Stock Quantity: ").strip()

    if price.isdigit() and stock.isdigit():
        products.append({
            "id": p_id,
            "name": name,
            "category": category,
            "price": int(price),
            "stock": int(stock)
        })
        print(f"Product '{name}' added successfully!")
    else:
        print("Invalid price or stock! Must be whole numbers.")


def view_products():
    # Displays all products in the store
    if len(products) == 0:
        print("\nNo products available.")
        return

    print("\n--- Product List ---")
    print(f"{'ID':<6} {'Name':<15} {'Category':<12} {'Price (Rs.)':<12} {'Stock':<6}")
    print("-" * 55)
    for p in products:
        print(f"{p['id']:<6} {p['name']:<15} {p['category']:<12} {p['price']:<12} {p['stock']:<6}")


def search_product():
    # Searches product by ID or Name
    query = input("\nEnter Product ID or Name to search: ").strip()
    found = False

    for p in products:
        if (query.isdigit() and p["id"] == int(query)) or (query.lower() in p["name"].lower()):
            print(f"\nFound: ID {p['id']} - {p['name']} ({p['category']}) | Price: Rs.{p['price']} | Stock: {p['stock']} units")
            found = True

    if not found:
        print("Product not found!")


def update_stock():
    # Adds stock to an existing product
    p_id = input("\nEnter Product ID to update stock: ").strip()
    if not p_id.isdigit():
        print("Invalid ID! Numbers only.")
        return

    p_id = int(p_id)
    for p in products:
        if p["id"] == p_id:
            add_qty = input(f"Current stock of {p['name']} is {p['stock']}. Enter quantity to add: ").strip()
            if add_qty.isdigit() and int(add_qty) > 0:
                p["stock"] += int(add_qty)
                print(f"Updated! New stock for {p['name']} is {p['stock']} units.")
            else:
                print("Invalid quantity! Enter a positive number.")
            return

    print("Product not found!")


def process_sale():
    # Processes customer purchase and deducts stock
    p_id = input("\nEnter Product ID to buy: ").strip()
    if not p_id.isdigit():
        print("Invalid ID! Numbers only.")
        return

    p_id = int(p_id)
    for p in products:
        if p["id"] == p_id:
            qty = input(f"Enter quantity to buy (Available: {p['stock']}): ").strip()
            if not qty.isdigit() or int(qty) <= 0:
                print("Invalid quantity! Enter a number greater than 0.")
                return

            qty = int(qty)
            if qty > p["stock"]:
                print(f"Insufficient stock! Only {p['stock']} units available.")
                return

            total_bill = qty * p["price"]
            p["stock"] -= qty

            # Save sale record
            sales_records.append({
                "id": p["id"],
                "name": p["name"],
                "quantity": qty,
                "total_amount": total_bill
            })

            print("\n--- Purchase Receipt ---")
            print(f"Item: {p['name']} | Qty: {qty} | Total Bill: Rs.{total_bill}")
            print(f"Remaining Stock: {p['stock']} units")
            return

    print("Product not found!")


def view_sales():
    # Displays all completed sales records
    if len(sales_records) == 0:
        print("\nNo sales recorded yet.")
        return

    print("\n--- Sales Records ---")
    print(f"{'ID':<6} {'Name':<15} {'Quantity':<10} {'Total (Rs.)':<12}")
    print("-" * 45)
    for s in sales_records:
        print(f"{s['id']:<6} {s['name']:<15} {s['quantity']:<10} {s['total_amount']:<12}")


def generate_report():
    # Generates a clear store summary report
    if len(products) == 0:
        print("\nNo products in store.")
        return

    total_products = len(products)
    total_stock = sum(p["stock"] for p in products)
    total_sales = len(sales_records)
    total_revenue = sum(s["total_amount"] for s in sales_records)

    highest = max(products, key=lambda p: p["price"])
    lowest = min(products, key=lambda p: p["price"])

    print("\n--- Store Report ---")
    print(f"Total Products in Store : {total_products}")
    print(f"Total Available Stock   : {total_stock} units")
    print(f"Total Sales Completed   : {total_sales}")
    print(f"Total Revenue Generated : Rs.{total_revenue}")
    print(f"Highest Priced Product  : {highest['name']} (Rs.{highest['price']})")
    print(f"Lowest Priced Product   : {lowest['name']} (Rs.{lowest['price']})")

    print("\nProducts with Low Stock (< 5 units):")
    low_stock = [p for p in products if p["stock"] < 5]
    if low_stock:
        for p in low_stock:
            print(f"- {p['name']} (Only {p['stock']} left!)")
    else:
        print("None. All items have sufficient stock.")


# ----------------------------------------------------
# Main Program Loop
# ----------------------------------------------------

while True:
    print("\n====================================")
    print("    SMART GROCERY STORE SYSTEM      ")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ").strip()

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        process_sale()
    elif choice == "6":
        view_sales()
    elif choice == "7":
        generate_report()
    elif choice == "8":
        print("\nThank you for using Smart Grocery Store! Goodbye.")
        break
    else:
        print("Invalid choice! Please choose an option between 1 and 8.")
