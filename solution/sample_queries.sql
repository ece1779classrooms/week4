# list of example to do in the lecture 

select * from category;								#get the id and name of all categories
select name from product where category_id = 1; 	#get the names of all the video games 

select c.name 										#get the category name for the product with id=3
from product as p join category as c on p.category_id = c.id 
where p.id = 3;

select p.name, c.name 
from product as p 
join customer_has_product as cp 
join customer as c 
on p.id = cp.product_id and 
   cp.customer_id = c.id;

insert into category (name) values ('Songs');		# create a new category for songs


# queries for hands-on part

select name,email from customer;					# get the names and emails of all customers
select name from customer where id = 2;				# get the name of the customer with id = 2
select name from product where name like 'G%';		# get the names of all products that start wiht G

select cat.name, p.name, c.name 
from product as p 
join customer_has_product as cp 
join customer as c 
join category as cat 
on p.id = cp.product_id and 
   cp.customer_id = c.id and
   cat.id = p.category_id;


