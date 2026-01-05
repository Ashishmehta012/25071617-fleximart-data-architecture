
    CREATE TABLE IF NOT EXISTS dim_date (date_key INTEGER PRIMARY KEY, full_date TEXT, year INTEGER, month INTEGER);
    CREATE TABLE IF NOT EXISTS dim_product (product_key INTEGER PRIMARY KEY, product_name TEXT, category TEXT, unit_price REAL);
    CREATE TABLE IF NOT EXISTS dim_customer (customer_key INTEGER PRIMARY KEY, customer_name TEXT, city TEXT);
    CREATE TABLE IF NOT EXISTS fact_sales (
        sale_key INTEGER PRIMARY KEY, 
        date_key INTEGER, 
        product_key INTEGER, 
        customer_key INTEGER, 
        quantity_sold INTEGER, 
        total_amount REAL
    );
    