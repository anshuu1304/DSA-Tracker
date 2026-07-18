# Write your MySQL query statement below
SELECT w.name , w.population , w.area
FROM World w
HAVING w.area >= 3000000 OR w.population >= 25000000;