-- CUSTOMER SALES ANALYSIS PROJECT
-- Database: SQLite

-- 1. Create customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    age INTEGER
);

-- 2. Insert customer data
INSERT INTO customers VALUES
(1, 'Ayse', 'Istanbul', 24),
(2, 'Mehmet', 'Ankara', 31),
(3, 'Zeynep', 'Izmir', 28),
(4, 'Ahmet', 'Istanbul', 42),
(5, 'Elif', 'Bursa', 35);

-- 3. Create orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT,
    amount REAL,
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

-- 4. Insert order data
INSERT INTO orders VALUES
(1, 1, 'Laptop', 25000),
(2, 2, 'Mouse', 500),
(3, 1, 'Keyboard', 1200),
(4, 3, 'Monitor', 7500),
(5, 4, 'Laptop', 25000),
(6, 5, 'Desk', 6000);

-- 5. Display all customers
SELECT * FROM customers;

-- 6. Display all orders
SELECT * FROM orders;

-- 7. Customer spending analysis
SELECT
    customers.name,
    customers.city,
    SUM(orders.amount) AS total_spending
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name, customers.city
ORDER BY total_spending DESC;

-- 8. Total revenue by product
SELECT
    product,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY product
ORDER BY total_revenue DESC;

-- 9. Average order amount
SELECT AVG(amount) AS average_order_amount
FROM orders;

-- 10. Filter orders above 5000
SELECT *
FROM orders
WHERE amount > 5000
ORDER BY amount DESC;

-- 11. Count orders by customer
SELECT
    customers.name,
    COUNT(orders.order_id) AS total_orders
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name
ORDER BY total_orders DESC;

-- 12. Customers with total spending above 10000
SELECT
    customers.name,
    SUM(orders.amount) AS total_spending
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name
HAVING SUM(orders.amount) > 10000;

-- 13. Add a customer without orders
INSERT INTO customers VALUES
(6, 'Can', 'Antalya', 29);

-- 14. Find customers with and without orders
SELECT
    customers.name,
    customers.city,
    COUNT(orders.order_id) AS total_orders
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY
    customers.customer_id,
    customers.name,
    customers.city
ORDER BY total_orders ASC;

-- 13. Add a customer without orders
INSERT INTO customers VALUES
(6, 'Can', 'Antalya', 29);

-- 14. Find customers with and without orders
SELECT
    customers.name,
    customers.city,
    COUNT(orders.order_id) AS total_orders
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
GROUP BY
    customers.customer_id,
    customers.name,
    customers.city
ORDER BY total_orders ASC;
