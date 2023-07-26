# Write your MySQL query statement below

SELECT MAX(num)  AS num from (SELECT num from MyNumbers GROUP BY num HAVING COUNT(num) = 1) NEW;
