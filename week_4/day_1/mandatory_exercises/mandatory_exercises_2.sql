-- Exercise 1 : Bootcamp

create table students (
	id serial PRIMARY KEY,
	last_name VARCHAR(50),
	first_name VARCHAR(50),
	birth_date TIMESTAMP 
);

insert into students(last_name, first_name, birth_date) 
Values 
('Benichou', 'Marc', '1998-11-02'),
('Cohen',	'Yoan'	,'2010-12-03'),
('Benichou',	'Lea','1987-07-27'),
('Dux' , 'Amelia'	,'1996-04-07'),
('Grez', 'David' ,'2003-06-14'),
('Simpson',	'Omer',	'1980-10-03')
;


-- Select
-- Fetch all of the data from the table.
select * from students;
-- Fetch all of the students first_names and last_names.
select first_name, last_name from students;
-- For the following questions, only fetch the first_names and last_names of the students.
	-- Fetch the student which id is equal to 2.
	select  first_name, last_name from students where id = 2;
	-- Fetch the student whose last_name is Benichou AND first_name is Marc.
	select  first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc';
	-- Fetch the students whose last_names are Benichou OR first_names are Marc.
		select  first_name, last_name from students where (last_name = 'Benichou' or first_name = 'Marc');
	-- Fetch the students whose first_names contain the letter a.
		select  first_name, last_name from students where first_name like '%a%';
	-- Fetch the students whose first_names start with the letter a.
			select  first_name, last_name from students where first_name like 'a%';
	-- Fetch the students whose first_names end with the letter a.
		select  first_name, last_name from students where first_name like '%a';
	-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
		select  first_name, last_name from students where first_name like '%a_' ;
	-- Fetch the students whose id’s are equal to 1 AND 3 .
	select first_name, last_name from students where id in (1,3)

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select * from students where birth_date >= '2000-01-01'