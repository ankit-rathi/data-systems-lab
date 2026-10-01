-- Deliberately flawed production-style query.
-- Investigate the grain before changing it.
SELECT
    DATE(o.created_at) AS revenue_date,
    SUM(o.amount) AS revenue
FROM orders AS o
JOIN payments AS p
    ON o.customer_id = p.customer_id
WHERE p.status = 'settled'
GROUP BY DATE(o.created_at);
