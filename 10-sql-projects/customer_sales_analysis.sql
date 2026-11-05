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
