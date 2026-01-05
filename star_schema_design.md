# Star Schema Design Documentation

## Section 1: Schema Overview
[cite_start]This data warehouse uses a Star Schema to analyze historical sales patterns[cite: 22].

* **FACT TABLE: fact_sales**
    * **Grain:** One row per product per order line item.
    * [cite_start]**Measures:** `quantity_sold`, `unit_price`, `total_amount`.
    * **Foreign Keys:** `date_key`, `product_key`, `customer_key`.

* **DIMENSION TABLE: dim_date**
    * [cite_start]**Purpose:** Time-based analysis.
    * [cite_start]**Attributes:** `date_key` (PK), `full_date`, `month_name`, `quarter`, `year`.

* **DIMENSION TABLE: dim_product**
    * **Purpose:** Product category and pricing analysis.
    * [cite_start]**Attributes:** `product_key` (PK), `product_name`, `category`, `unit_price`.

* **DIMENSION TABLE: dim_customer**
    * **Purpose:** Customer segmentation and geography analysis.
    * [cite_start]**Attributes:** `customer_key` (PK), `customer_name`, `city`, `customer_segment`.

## Section 2: Design Decisions
* **Granularity:** We chose the transaction line-item level to allow for detailed "drill-down" analysis into specific products[cite: 24].
* [cite_start]**Surrogate Keys:** We use auto-incrementing integer keys (surrogate keys) to maintain data integrity and handle potential changes in source system IDs[cite: 24].

## Section 3: Sample Data Flow
[cite_start]**Source Transaction:** Order #101, Customer "John Doe", Product "Laptop", Qty: 1, Price: 50000[cite: 24].

**Data Warehouse Representation:**
* **fact_sales:** {date_key: 20240115, product_key: 1, customer_key: 1, quantity_sold: 1, total_amount: 50000}[cite: 24].
* [cite_start]**dim_product:** {product_key: 1, product_name: 'Laptop', category: 'Electronics'}[cite: 25].