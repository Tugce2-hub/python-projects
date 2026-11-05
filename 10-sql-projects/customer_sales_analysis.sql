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
