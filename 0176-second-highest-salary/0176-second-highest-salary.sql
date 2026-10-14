# Write your MySQL query statement below
SELECT MAX(e.salary) AS SecondHighestSalary
FROM Employee e
Where e.salary <(
    SELECT MAX(e.salary)
    FROM Employee e
);