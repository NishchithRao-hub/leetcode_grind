# Write your MySQL query statement below
SELECT e.name , b.bonus from Employee e
LEFT JOIN Bonus b ON e.empId=b.empId
where bonus<1000 or bonus IS NULL 
