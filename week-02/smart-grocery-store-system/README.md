# Smart Grocery Store Management System

A practical, menu-driven Python console application designed to manage daily grocery store operations, inventory tracking, customer sales processing, and business analytics using lists of dictionaries.

---

## 📌 Project Overview

This project is built for **Week 02** of the PSEB DEPLOY journey to demonstrate mastery of:
- **Compound Data Structures**: Representing multi-attribute entities using a list of dictionaries (`products = [{...}]`).
- **Transactional Ledger**: Maintaining a separate list of dictionaries (`sales_records = [{...}]`) to record completed customer orders.
- **Stock Management & Validation**: Preventing overselling by checking available stock against customer purchase requests.
- **Duplicate Prevention**: Enforcing unique numeric Product IDs across the entire inventory.
- **Real-Time Store Reporting**: Computing inventory totals, cumulative revenue, price extremes (highest/lowest), and low-stock alerts (< 5 units).
- **Clean Python Code (PEP 8)**: Zero AI boilerplate (`if __name__ == "__main__": main()`), procedural top-to-bottom flow, lowercase `snake_case` functions, and input validation without `try/except`.

---

## ⏱️ Engineering Hours Breakdown & Defense (5.0 Hours Total)

The **5.0 hours** recorded in `hours-log.md` is defended by the following technical milestones:

| Phase | Time Spent | Engineering Focus & Technical Proof |
| :--- | :---: | :--- |
| **1. Requirements & Data Architecture** | **1.0 hr** | Designed data schema using lists of dictionaries for inventory (`id`, `name`, `category`, `price`, `stock`) and completed sales transactions (`id`, `name`, `quantity`, `total_amount`). Seeded realistic starting products in PKR. |
| **2. Inventory Management & Duplicate Protection** | **1.0 hr** | Implemented `add_product()` with uniqueness checking on Product ID, non-empty title-cased names/categories, and numeric price/stock guards. Built `view_all_products()` displaying tabular inventory with low-stock warnings `(!)`. |
| **3. Search & Stock Update Workflows** | **1.0 hr** | Engineered `search_product()` supporting dual-mode search (by numeric ID or case-insensitive name matching via `.lower()`). Implemented `update_product_stock()` allowing store owners to add new units to existing stock or set fresh quantities. |
| **4. Customer Sales & Stock Deduction** | **1.0 hr** | Built `process_customer_sale()` verifying stock availability, rejecting sales when requested units exceed stock, deducting sold quantity from inventory, appending transaction details to `sales_records`, and generating customer purchase receipts. |
| **5. Store Report, Testing & Documentation** | **1.0 hr** | Implemented `generate_store_report()` calculating total inventory units, total sales, cumulative revenue, min/max priced items, and low-stock alerts. Verified zero `try/except` blocks (using `.isdigit()`), zero AI boilerplate, and prepared comprehensive documentation. |

---

## 🚀 Application Features & Menu Options

The application runs in a persistent `while True` loop with 8 operational options:

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

1. **Add New Product**:
   - Collects Product ID, Name, Category, Price, and Stock.
   - Enforces unique Product IDs to prevent accidental overwrites.
   - Validates input using `.isdigit()` and `if/else` checks (no `try-except`).
2. **View All Products**:
   - Renders a clean ASCII table displaying all stored products with price formatting.
   - Highlights items with stock below 5 units with an alert tag `(!)`.
3. **Search Product**:
   - Searches by numeric Product ID or case-insensitive name substring (`.lower()`).
   - Displays complete product details if found.
4. **Update Product Stock**:
   - Prompts for Product ID and allows adding units or setting a new total quantity.
5. **Process Customer Sale**:
   - Prompts for Product ID and purchase quantity.
   - Blocks sales if requested quantity exceeds available stock.
   - Deducts purchased quantity from inventory, appends transaction to `sales_records`, and displays a clean receipt.
6. **View Sales Records**:
   - Displays all recorded customer sales with transaction count and cumulative revenue.
7. **Generate Store Report**:
   - Summarizes total products, total stock units, total transactions, total revenue, highest/lowest priced items, and all low-stock items (< 5 units).
8. **Exit**:
   - Breaks out of the loop and exits gracefully.

---

## 🛠️ Python Concepts Applied

- **Lists of Dictionaries**: Storing complex entity records (`products` and `sales_records`).
- **Dictionary Key Access & Mutation**: Updating stock (`product["stock"] -= qty`) and reading properties (`product["price"]`).
- **PEP 8 Functions (`snake_case`)**: `display_menu`, `add_product`, `view_all_products`, `search_product`, `update_product_stock`, `process_customer_sale`, `view_sales_records`, `generate_store_report`.
- **Procedural Scripting**: Simple top-to-bottom execution without unnecessary wrappers.
- **Input Validation Without `try-except`**: Clean `.isdigit()` checks with conditional `if-else` guards inside `while True` loops.
- **Aggregation Logic**: Computing sums, minimums, maximums, and filtering low-stock items.

---

## 📁 Project Structure

```text
week-02/
├── smart-grocery-store-system/
│   ├── smart_grocery_store.py    # Main grocery management console application
│   └── README.md                 # Detailed documentation, defense table, and sample runs
└── README.md                     # Week 02 index
```

---

## 💻 How to Run

From your terminal or PyCharm:

```bash
python smart_grocery_store.py
```

*(From repository root: `./.venv/bin/python week-02/smart-grocery-store-system/smart_grocery_store.py`)*

---

## 📋 Sample Run (Terminal Transcript)

```text
=============================================
         SMART GROCERY STORE SYSTEM          
=============================================
  1. Add New Product
  2. View All Products
  3. Search Product
  4. Update Product Stock
  5. Process Customer Sale
  6. View Sales Records
  7. Generate Store Report
  8. Exit
=============================================
Enter your choice (1-8): 2

========================================================================
                        CURRENT STORE INVENTORY                         
========================================================================
 ID     | Product Name               | Category        | Price (Rs.) | Stock
------------------------------------------------------------------------
 101    | Milk (1L Pack)             | Dairy           |        250 |    25
 102    | Basmati Rice (1kg)         | Grains          |        380 |    40
 103    | Cooking Oil (1L)           | Oil & Ghee      |        520 |    15
 104    | Farm Eggs (Dozen)          | Poultry         |        320 | 4 (!)
 105    | Black Tea (450g)           | Beverages       |        650 |     8
------------------------------------------------------------------------
 Total Products Listed: 5 | (!) Indicates low stock (< 5 units)

=============================================
         SMART GROCERY STORE SYSTEM          
=============================================
  1. Add New Product
  2. View All Products
  3. Search Product
  4. Update Product Stock
  5. Process Customer Sale
  6. View Sales Records
  7. Generate Store Report
  8. Exit
=============================================
Enter your choice (1-8): 5

Enter Product ID to purchase: 101
  Selected: Milk (1L Pack)
  Price   : Rs. 250 per unit
  In Stock: 25 units

Enter quantity to purchase: 3

==================================================
             CUSTOMER PURCHASE RECEIPT            
==================================================
 Product ID        : 101
 Product Name      : Milk (1L Pack)
 Unit Price        : Rs. 250
 Quantity Bought   : 3
--------------------------------------------------
 TOTAL PAYABLE     : Rs. 750
--------------------------------------------------
 Remaining Stock   : 22 units
==================================================
  Thank you for shopping with us!

=============================================
         SMART GROCERY STORE SYSTEM          
=============================================
  1. Add New Product
  2. View All Products
  3. Search Product
  4. Update Product Stock
  5. Process Customer Sale
  6. View Sales Records
  7. Generate Store Report
  8. Exit
=============================================
Enter your choice (1-8): 7

============================================================
              SMART GROCERY STORE REPORT             
============================================================
 Total Products in Inventory : 5
 Total Available Stock Units : 89 units
 Total Sales Completed       : 1 transactions
 Total Revenue Generated     : Rs. 750
------------------------------------------------------------
 Highest Priced Product      : Black Tea (450g) (Rs. 650)
 Lowest Priced Product       : Milk (1L Pack) (Rs. 250)
------------------------------------------------------------
 Products with Low Stock (Below 5 units):
   - [ID: 104] Farm Eggs (Dozen)        (Stock: 4 units)
============================================================
```

---

## 🎯 Viva & Defense Preparation

Key technical points to explain during evaluation:
1. **List of Dictionaries vs. Parallel Lists**:
   In Week 1, we used parallel lists (`descriptions`, `categories`, `amounts`). In Week 2, dictionaries encapsulate each product's attributes (`id`, `name`, `category`, `price`, `stock`) into a single cohesive object, preventing index misalignment bugs.
2. **Stock Verification Before Sale**:
   The sale logic first checks `purchase_qty > target_product["stock"]`. If true, the transaction is rejected immediately without modifying inventory or sales history.
3. **Preventing Duplicate IDs**:
   When adding a product, a linear search loops through `products_list` to verify no existing dictionary has `item["id"] == product_id`.
4. **Validation Without `try-except`**:
   All user inputs use string validation (`.isdigit()`, `> 0`) inside `while True` loops, keeping the codebase simple and aligned with course standards.
