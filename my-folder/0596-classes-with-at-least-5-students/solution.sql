# Write your MySQL query statement below

SELECT class from courses GROUP BY class having COUNT(distinct student) >=5;
