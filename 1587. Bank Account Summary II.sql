# Write your MySQL query statement below
SELECT u.name AS NAME,SUM(t.amount) AS BALANCE
FROM Users u, Transactions t
WHERE u.account=t.account
GROUP BY u.account
HAVING SUM(t.amount)>10000;
