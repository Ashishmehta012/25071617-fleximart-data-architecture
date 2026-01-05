import sqlite3
import pandas as pd
import os

def run_sqlite_etl():
    print("--- STARTING SQLITE SETUP ---")
    
    # 1. Connect to SQLite (Creates a file 'fleximart.db' automatically)
    try:
        conn = sqlite3.connect('fleximart.db')
        cursor = conn.cursor()
        print("1. Database file 'fleximart.db' created successfully.")
    except Exception as e:
        print(f"ERROR: {e}")
        return

    # 2. Create Tables (SQLite syntax is slightly simpler)
    print("2. Creating tables...")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY, 
                first_name TEXT, 
                email TEXT, 
                city TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY, 
                product_name TEXT, 
                category TEXT, 
                price REAL
            )
        """)
        # We also create the orders table for later
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY, 
                customer_id INTEGER, 
                total_amount REAL
            )
        """)
        print("   Tables created successfully.")
    except Exception as e:
        print(f"ERROR Creating Tables: {e}")

    # 3. Load Data
    print("3. Loading data from CSV...")
    try:
        # Check if file exists first
        if not os.path.exists('data/customers_raw.csv'):
            print("ERROR: 'data/customers_raw.csv' not found.")
            return

        df_cust = pd.read_csv('data/customers_raw.csv')
        
        # Insert data
        count = 0
        for _, row in df_cust.head(5).iterrows():
            sql = "INSERT INTO customers (first_name, email, city) VALUES (?, ?, ?)"
            # SQLite uses '?' instead of '%s'
            cursor.execute(sql, (row['first_name'], row['email'], row['city']))
            count += 1
        
        conn.commit()
        print(f"   SUCCESS! Loaded {count} customers into SQLite.")
        
    except Exception as e:
        print(f"ERROR Loading Data: {e}")
        
    cursor.close()
    conn.close()
    print("--- COMPLETED ---")

if __name__ == "__main__":
    run_sqlite_etl()