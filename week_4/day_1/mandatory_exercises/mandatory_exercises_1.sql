create table items (
	id serial PRIMARY KEY,
name VARCHAR(50),
price integer NOT NULL,
description VARCHAR(100)	
)
;
INSERT INTO 
    items (name, price, description)
VALUES
    ('small desk', 100,'a desk measuring 1 x 1 meters'),
     ('large desk', 300,'a desk measuring 3 x 3 meters'),
    ('fan', 80,'a higher-powered fan');

create table items (
	id serial PRIMARY KEY,
	name VARCHAR(50),
 	price integer NOT NULL,
	description VARCHAR(100)	
 )
;

 create table customers (
 	id serial PRIMARY KEY,
 	first_name VARCHAR(50),
 	last_name VARCHAR(50),
 	address VARCHAR(50))

;

insert into customers (first_name, last_name)
values 
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson')


-- Use SQL to fetch the following data from the database:
-- All the items.
select* from items;

-- All the items with a price above 80 (80 not included).
select* from items where price > 80;

-- All the items with a price below 300. (300 included)
select* from items where price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
select * from customers where last_name ='Smith'; 
--the outcome is an empty table because there are no Smiths

-- All customers whose last name is ‘Jones’.
select * from customers where last_name ='Jones';

-- All customers whose firstname is not ‘Scott’.
select * from customers where last_name !='Scott';