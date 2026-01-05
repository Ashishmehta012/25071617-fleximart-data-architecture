-- Query 1: High Spenders
SELECT first_name, email, COUNT(o.order_id) as total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING total_orders >= 2;

-- Query 2: Product Sales
SELECT category, COUNT(product_id) as product_count
FROM products
GROUP BY category;