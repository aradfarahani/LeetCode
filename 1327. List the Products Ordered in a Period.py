# Write your MySQL query statement below
select product_name, sum(unit) as unit from products
join orders using(product_id)
where year(order_date)=2020 and month(order_date)=2
group by 1
having sum(unit)>99
