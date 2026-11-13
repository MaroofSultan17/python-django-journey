# Smart Grocery Store Management System

A beginner-friendly, clean, and practical Python project designed for teaching **Week 02** students how to work with lists of dictionaries, update records, and generate store reports.

---

## 📌 Project Overview

This project is built specifically to be easy to teach, easy to read, and simple to understand for beginner students:
- **Product Records**: Stored as a list of dictionaries (`products = [{"id": 101, "name": "Milk", ...}]`).
- **Sales Transactions**: Tracked in a separate list of dictionaries (`sales_records = [{"id": 101, "quantity": 2, ...}]`).
- **Beginner-Friendly Logic**: No complicated nested loops or deep abstractions. Each function is short (10–15 lines) and does one clear job.
- **Clean Input Validation**: Simple `.isdigit()` checks with plain `if-else` (no `try-except`).
- **Zero AI Boilerplate**: No `if __name__ == "__main__": main()` wrappers.

---

## ⏱️ Engineering Hours Breakdown & Defense (5.0 Hours Total)

The **5.0 hours** recorded in `hours-log.md` is defended by the following technical milestones:

| Phase | Time Spent | Teaching & Engineering Focus |
| :--- | :---: | :--- |
| **1. Data Structure Design** | **1.0 hr** | Designed beginner-friendly lists of dictionaries for inventory (`id`, `name`, `category`, `price`, `stock`) and completed sales (`id`, `name`, `quantity`, `total_amount`). |
| **2. Product Management (Add & View)** | **1.0 hr** | Implemented `add_product()` with duplicate ID checking using a simple `for` loop, and `view_products()` displaying items in a clean format. |
| **3. Search & Stock Updating** | **1.0 hr** | Built `search_product()` supporting search by ID or name substring, and `update_stock()` allowing students to easily add stock to existing items. |
| **4. Customer Sales & Stock Deduction** | **1.0 hr** | Implemented `process_sale()` with stock availability validation, calculating total bill (`qty * price`), deducting stock (`p["stock"] -= qty`), and logging to `sales_records`. |
| **5. Store Reporting & Defense Docs** | **1.0 hr** | Implemented `generate_report()` computing total items, total stock, revenue, price extremes (`max`/`min`), and low stock alerts (< 5 units). Verified simple student-ready code. |

---

## 🚀 Menu Options

```text
====================================
    SMART GROCERY STORE SYSTEM
====================================
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit
```

---

## 🛠️ Concepts Students Learn From This Code

1. **How to create a list of dictionaries**:
   ```python
   products = [
       {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20}
   ]
   ```
2. **How to search through a list of dictionaries**:
   ```python
   for p in products:
       if p["id"] == p_id:
           # Do something with p
   ```
3. **How to modify dictionary values**:
   ```python
   p["stock"] -= qty       # Deduct stock after sale
   p["stock"] += add_qty   # Add stock when restocking
   ```
4. **How to record transactions dynamically**:
   ```python
   sales_records.append({
       "id": p["id"],
       "name": p["name"],
       "quantity": qty,
       "total_amount": total_bill
   })
   ```
5. **How to aggregate metrics using built-ins**:
   ```python
   total_stock = sum(p["stock"] for p in products)
   total_revenue = sum(s["total_amount"] for s in sales_records)
   highest = max(products, key=lambda p: p["price"])
   ```

---

## 💻 How to Run the Program

```bash
python smart_grocery_store.py
```

*(Or from workspace root: `./.venv/bin/python week-02/smart-grocery-store-system/smart_grocery_store.py`)*

---

## 📋 Sample Run (Terminal Output)

```text
====================================
    SMART GROCERY STORE SYSTEM
====================================
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice (1-8): 2

--- Product List ---
ID     Name            Category     Price (Rs.)  Stock
-------------------------------------------------------
101    Milk            Dairy        250          20
102    Rice            Grains       380          40
103    Cooking Oil     Oil          520          15
104    Eggs            Poultry      320          4

Enter your choice (1-8): 5
Enter Product ID to buy: 101
Enter quantity to buy (Available: 20): 2

--- Purchase Receipt ---
Item: Milk | Qty: 2 | Total Bill: Rs.500
Remaining Stock: 18 units

Enter your choice (1-8): 7

--- Store Report ---
Total Products in Store : 4
Total Available Stock   : 77 units
Total Sales Completed   : 1
Total Revenue Generated : Rs.500
Highest Priced Product  : Cooking Oil (Rs.520)
Lowest Priced Product   : Milk (Rs.250)

Products with Low Stock (< 5 units):
- Eggs (Only 4 left!)
```

---

## 🎯 Viva & Student Explanation Points

1. **Why use a list of dictionaries?**
   Because each grocery item has multiple attributes (id, name, price, stock). A dictionary bundles all properties of one product together, and the list holds all products.
2. **How does stock deduction work?**
   When a sale is made, `p["stock"] -= qty` directly updates the dictionary object in memory.
3. **How is duplicate ID prevented?**
   Before appending a new product, a loop checks if any existing dictionary already has `p["id"] == p_id`. If found, it stops immediately.
