# Write your MySQL query statement below

SELECT product.product_name,sales.year,sales.price 
    FROM sales,product
WHERE sales.product_id =  product.product_id;
