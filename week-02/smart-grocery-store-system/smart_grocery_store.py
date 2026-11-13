# Smart Grocery Store Management System
# Topic: Lists of Dictionaries, Data Validation, Stock Management, and Sales Reporting

# Initial Product Inventory (List of Dictionaries)
products = [
    {
        "id": 101,
        "name": "Milk (1L Pack)",
        "category": "Dairy",
        "price": 250,
        "stock": 25
    },
    {
        "id": 102,
        "name": "Basmati Rice (1kg)",
        "category": "Grains",
        "price": 380,
        "stock": 40
    },
    {
        "id": 103,
        "name": "Cooking Oil (1L)",
        "category": "Oil & Ghee",
        "price": 520,
        "stock": 15
    },
    {
        "id": 104,
        "name": "Farm Eggs (Dozen)",
        "category": "Poultry",
        "price": 320,
        "stock": 4
    },
    {
        "id": 105,
        "name": "Black Tea (450g)",
        "category": "Beverages",
        "price": 650,
        "stock": 8
    }
]

# List of Dictionaries to Record Completed Customer Sales
sales_records = []


def display_menu():
    # Displays the main grocery store operations menu
    print("\n" + "=" * 45)
    print("         SMART GROCERY STORE SYSTEM          ")
    print("=" * 45)
    print("  1. Add New Product")
    print("  2. View All Products")
    print("  3. Search Product")
    print("  4. Update Product Stock")
    print("  5. Process Customer Sale")
    print("  6. View Sales Records")
    print("  7. Generate Store Report")
    print("  8. Exit")
    print("=" * 45)


def add_product(products_list):
    # Adds a new product dictionary to the inventory with duplicate ID prevention
    print("\n--- Add New Product ---")

    # 1. Validate Product ID (digits only and unique)
    while True:
        id_input = input("Enter unique Product ID (numbers only): ").strip()
        if id_input.isdigit():
            product_id = int(id_input)
            if product_id <= 0:
                print("  Product ID must be greater than 0.")
                continue

            # Check for duplicate ID
            id_exists = False
            for item in products_list:
                if item["id"] == product_id:
                    id_exists = True
                    break

            if id_exists:
                print(f"  Error: Product ID {product_id} already exists! Please choose a different ID.")
            else:
                break
        else:
            print("  Invalid input! Please enter whole numbers only.")

    # 2. Validate Product Name (non-empty)
    while True:
        name_input = input("Enter Product Name: ").strip()
        if name_input == "":
            print("  Product name cannot be empty. Please enter a valid name.")
        else:
            product_name = name_input.title()
            break

    # 3. Validate Category (non-empty)
    while True:
        category_input = input("Enter Category (e.g., Dairy, Bakery, Beverages): ").strip()
        if category_input == "":
            print("  Category cannot be empty. Please enter a valid category.")
        else:
            category_name = category_input.title()
            break

    # 4. Validate Price (positive whole number)
    while True:
        price_input = input("Enter Unit Price in PKR (Rs.): ").strip()
        if price_input.isdigit():
            product_price = int(price_input)
            if product_price > 0:
                break
            else:
                print("  Price must be greater than 0.")
        else:
            print("  Invalid price! Please enter a valid positive number.")

    # 5. Validate Available Stock (non-negative number)
    while True:
        stock_input = input("Enter Initial Available Stock Quantity: ").strip()
        if stock_input.isdigit():
            product_stock = int(stock_input)
            if product_stock >= 0:
                break
            else:
                print("  Stock quantity cannot be negative.")
        else:
            print("  Invalid stock! Please enter a whole number (0 or more).")

    # Create new product dictionary and append to list
    new_product = {
        "id": product_id,
        "name": product_name,
        "category": category_name,
        "price": product_price,
        "stock": product_stock
    }
    products_list.append(new_product)
    print(f"\n  [Success] Added '{product_name}' (ID: {product_id}) to store inventory!")


def view_all_products(products_list):
    # Displays all stored products in a clean, aligned tabular format
    if len(products_list) == 0:
        print("\n  Inventory is currently empty. Use Option 1 to add products.")
        return

    print("\n" + "=" * 72)
    print(f"{'CURRENT STORE INVENTORY':^72}")
    print("=" * 72)
    print(f" {'ID':<6} | {'Product Name':<26} | {'Category':<15} | {'Price (Rs.)':>10} | {'Stock':>5}")
    print("-" * 72)

    for item in products_list:
        stock_display = f"{item['stock']}"
        # Add a low stock indicator if stock is below 5
        if item["stock"] < 5:
            stock_display += " (!)"
        print(f" {item['id']:<6} | {item['name']:<26} | {item['category']:<15} | {item['price']:>10,d} | {stock_display:>5}")

    print("-" * 72)
    print(f" Total Products Listed: {len(products_list)} | (!) Indicates low stock (< 5 units)")


def search_product(products_list):
    # Searches and displays product details by product ID or product name
    if len(products_list) == 0:
        print("\n  Inventory is empty. Nothing to search.")
        return

    query = input("\nEnter Product ID or Name to search: ").strip()
    if query == "":
        print("  Search query cannot be empty.")
        return

    query_lower = query.lower()
    found_products = []

    for item in products_list:
        # Match by ID (if query is a number) or match by name (case-insensitive)
        if query.isdigit() and item["id"] == int(query):
            found_products.append(item)
        elif query_lower in item["name"].lower():
            found_products.append(item)

    if len(found_products) == 0:
        print(f"\n  [Notice] No product found matching '{query}'.")
    else:
        print(f"\n--- Search Results ({len(found_products)} item(s) found) ---")
        for item in found_products:
            print("-" * 45)
            print(f"  Product ID      : {item['id']}")
            print(f"  Product Name    : {item['name']}")
            print(f"  Category        : {item['category']}")
            print(f"  Unit Price      : Rs. {item['price']:,d}")
            print(f"  Available Stock : {item['stock']} units")
        print("-" * 45)


def update_product_stock(products_list):
    # Allows updating or adding stock for an existing product
    if len(products_list) == 0:
        print("\n  Inventory is empty. No stock to update.")
        return

    id_input = input("\nEnter Product ID to update stock: ").strip()
    if not id_input.isdigit():
        print("  Invalid Product ID! Please enter numbers only.")
        return

    product_id = int(id_input)
    target_product = None

    for item in products_list:
        if item["id"] == product_id:
            target_product = item
            break

    if target_product is None:
        print(f"  [Error] Product with ID {product_id} does not exist.")
        return

    print(f"\n  Product Found: {target_product['name']} (Current Stock: {target_product['stock']} units)")
    print("  1. Add to existing stock")
    print("  2. Set new total stock quantity")
    choice = input("  Choose update type (1 or 2): ").strip()

    if choice == "1":
        while True:
            add_input = input("  Enter quantity to ADD to current stock: ").strip()
            if add_input.isdigit():
                add_qty = int(add_input)
                if add_qty > 0:
                    target_product["stock"] += add_qty
                    print(f"\n  [Success] Added {add_qty} units. New available stock: {target_product['stock']} units.")
                    break
                else:
                    print("  Quantity must be greater than 0.")
            else:
                print("  Invalid input! Please enter a whole number.")

    elif choice == "2":
        while True:
            new_input = input("  Enter NEW total stock quantity: ").strip()
            if new_input.isdigit():
                new_qty = int(new_input)
                if new_qty >= 0:
                    target_product["stock"] = new_qty
                    print(f"\n  [Success] Stock updated. New available stock: {target_product['stock']} units.")
                    break
                else:
                    print("  Stock quantity cannot be negative.")
            else:
                print("  Invalid input! Please enter a whole number.")
    else:
        print("  Invalid choice! Stock update cancelled.")


def process_customer_sale(products_list, sales_list):
    # Processes customer purchase, verifies stock availability, and records sale
    if len(products_list) == 0:
        print("\n  Inventory is empty. Cannot process any sales.")
        return

    id_input = input("\nEnter Product ID to purchase: ").strip()
    if not id_input.isdigit():
        print("  Invalid Product ID! Please enter numbers only.")
        return

    product_id = int(id_input)
    target_product = None

    for item in products_list:
        if item["id"] == product_id:
            target_product = item
            break

    if target_product is None:
        print(f"  [Error] Product with ID {product_id} does not exist.")
        return

    # Check if product is out of stock
    if target_product["stock"] == 0:
        print(f"  [Error] '{target_product['name']}' is currently OUT OF STOCK!")
        return

    print(f"\n  Selected: {target_product['name']}")
    print(f"  Price   : Rs. {target_product['price']:,d} per unit")
    print(f"  In Stock: {target_product['stock']} units")

    # Ask for purchase quantity
    while True:
        qty_input = input("\nEnter quantity to purchase: ").strip()
        if qty_input.isdigit():
            purchase_qty = int(qty_input)
            if purchase_qty <= 0:
                print("  Quantity must be at least 1 unit.")
                continue

            # Check stock availability
            if purchase_qty > target_product["stock"]:
                print(f"  [Error] Cannot process sale! Requested {purchase_qty} units, but only {target_product['stock']} units available.")
                return
            else:
                break
        else:
            print("  Invalid quantity! Please enter a whole number.")

    # Calculate total and deduct stock
    total_amount = purchase_qty * target_product["price"]
    target_product["stock"] -= purchase_qty

    # Store sales record
    sale_record = {
        "id": target_product["id"],
        "name": target_product["name"],
        "quantity": purchase_qty,
        "total_amount": total_amount
    }
    sales_list.append(sale_record)

    # Display neat receipt
    print("\n" + "=" * 50)
    print("             CUSTOMER PURCHASE RECEIPT            ")
    print("=" * 50)
    print(f" Product ID        : {target_product['id']}")
    print(f" Product Name      : {target_product['name']}")
    print(f" Unit Price        : Rs. {target_product['price']:,d}")
    print(f" Quantity Bought   : {purchase_qty}")
    print("-" * 50)
    print(f" TOTAL PAYABLE     : Rs. {total_amount:,d}")
    print("-" * 50)
    print(f" Remaining Stock   : {target_product['stock']} units")
    print("=" * 50)
    print("  Thank you for shopping with us!")


def view_sales_records(sales_list):
    # Displays all completed customer sales transactions
    if len(sales_list) == 0:
        print("\n  No sales transactions have been recorded yet.")
        return

    print("\n" + "=" * 65)
    print(f"{'COMPLETED SALES TRANSACTIONS':^65}")
    print("=" * 65)
    print(f" {'No.':<4} | {'ID':<6} | {'Product Name':<26} | {'Qty':>5} | {'Total (Rs.)':>12}")
    print("-" * 65)

    total_revenue = 0
    total_items_sold = 0

    for idx, sale in enumerate(sales_list, start=1):
        total_revenue += sale["total_amount"]
        total_items_sold += sale["quantity"]
        print(f" {idx:<4} | {sale['id']:<6} | {sale['name']:<26} | {sale['quantity']:>5} | {sale['total_amount']:>12,d}")

    print("-" * 65)
    print(f" Total Transactions : {len(sales_list)}")
    print(f" Total Units Sold   : {total_items_sold} units")
    print(f" Cumulative Revenue : Rs. {total_revenue:,d}")
    print("=" * 65)


def generate_store_report(products_list, sales_list):
    # Generates a comprehensive summary report of the store operations
    total_products = len(products_list)
    total_stock = 0
    low_stock_items = []

    for item in products_list:
        total_stock += item["stock"]
        if item["stock"] < 5:
            low_stock_items.append(item)

    total_sales_count = len(sales_list)
    total_revenue = 0
    for sale in sales_list:
        total_revenue += sale["total_amount"]

    # Find highest and lowest priced products
    highest_product = None
    lowest_product = None

    if total_products > 0:
        highest_product = products_list[0]
        lowest_product = products_list[0]

        for item in products_list:
            if item["price"] > highest_product["price"]:
                highest_product = item
            if item["price"] < lowest_product["price"]:
                lowest_product = item

    print("\n" + "=" * 60)
    print("              SMART GROCERY STORE REPORT             ")
    print("=" * 60)
    print(f" Total Products in Inventory : {total_products}")
    print(f" Total Available Stock Units : {total_stock} units")
    print(f" Total Sales Completed       : {total_sales_count} transactions")
    print(f" Total Revenue Generated     : Rs. {total_revenue:,d}")
    print("-" * 60)

    # Highest and Lowest Price
    if highest_product and lowest_product:
        print(f" Highest Priced Product      : {highest_product['name']} (Rs. {highest_product['price']:,d})")
        print(f" Lowest Priced Product       : {lowest_product['name']} (Rs. {lowest_product['price']:,d})")
    else:
        print(" Price Metrics               : N/A (No products registered)")

    print("-" * 60)
    print(" Products with Low Stock (Below 5 units):")
    if len(low_stock_items) > 0:
        for item in low_stock_items:
            print(f"   - [ID: {item['id']}] {item['name']:<24} (Stock: {item['stock']} units)")
    else:
        print("   All products have sufficient stock (5 or more units).")

    print("=" * 60 + "\n")


# ----------------------------------------------------
# Main Program Execution
# ----------------------------------------------------

while True:
    display_menu()
    user_choice = input("Enter your choice (1-8): ").strip()

    if user_choice == "1":
        add_product(products)
    elif user_choice == "2":
        view_all_products(products)
    elif user_choice == "3":
        search_product(products)
    elif user_choice == "4":
        update_product_stock(products)
    elif user_choice == "5":
        process_customer_sale(products, sales_records)
    elif user_choice == "6":
        view_sales_records(sales_records)
    elif user_choice == "7":
        generate_store_report(products, sales_records)
    elif user_choice == "8":
        print("\n" + "=" * 45)
        print("  Thank you for using Smart Grocery Store!")
        print("  System shutting down safely. Goodbye.")
        print("=" * 45 + "\n")
        break
    else:
        print("  Invalid choice! Please select an option between 1 and 8.")
