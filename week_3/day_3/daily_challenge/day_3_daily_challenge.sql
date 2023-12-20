-- You are going to practice tables relationships

-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), 
-- customer_id (a reference to the Customer table)
	create table Customer (id serial Primary Key, first_name varchar(50), last_name varchar(50) NOT NULL)
	create table customer_profile (id serial Primary Key, isLoggedIn Boolean DEFAULT false, 
									 customer_id integer REFERENCES customer(id) ON DELETE SET NULL)
	
-- Insert those customers
-- John, Doe
-- Jerome, Lalu
-- Lea, Rive

	insert into Customer (last_name, first_name)
	values ('Doe','John'),('Lalu','Jerome'),('Rive','Lea')

-- Insert those customer profiles, use subqueries
	insert into customer_profile ( customer_id)
	select id from customer

-- John is loggedIn
-- Jerome is not logged in
	update customer_profile 
	set isloggedin = true where id=2
	

-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
	select c.first_name from customer c join customer_profile cp on c.id = cp.customer_id
	where cp.isloggedin = True
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
	select c.first_name, cp.isloggedin from customer c left join customer_profile cp on c.id = cp.customer_id
	
-- The number of customers that are not LoggedIn
	select count(cp.isloggedin) from customer c left join customer_profile cp on c.id = cp.customer_id
	where cp.isloggedin = False
	

-- Part II:

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
	create table Book (book_id serial primary key, title varchar(100) NOT NULL, author varchar(50) NOT NULL)
-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee
	insert into Book (title, author)
	values ( 'Alice In Wonderland', 'Lewis Carroll'),  ('Harry Potter',' J.K Rowling'), 
	('Harry Potter', 'J.K Rowling')

-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
	create table Student (student_id serial primary key, name varchar(50) not null UNIQUE, 
						  age int CHECK( age >0 and age<=15))
-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14
	insert into Student (name, age)
	values ('John' ,12),
	('Lera',11),
	('Patrick',10),
	('Bob', 14)
	
	select* from student
	
-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
	create table Library (book_fk_id integer REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
						 student_id integer REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
						 borrowed_date timestamp)
						 
	alter table library ADD CONSTRAINT pk_Library PRIMARY KEY (book_fk_id, student_id)

-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : 
-- A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
	insert into library (student_id, book_fk_id, borrowed_date)
	values ((select student_id from student where name = 'John'),
			(select book_id  from Book where lower(title) like '%alice%'),
			'2022-02-15')
			
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
		insert into library (student_id, book_fk_id, borrowed_date)
	values ((select student_id from student where name = 'Bob'),
			(select book_id  from Book where lower(title) like '%kill%'),
			'2021-03-03')
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
	insert into library (student_id, book_fk_id, borrowed_date)
	values ((select student_id from student where name = 'Lera'),
			(select book_id  from Book where lower(title) like '%alice%'),
			'2021-05-23')
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021
	insert into library (student_id, book_fk_id, borrowed_date)
	values ((select student_id from student where name = 'Bob'),
			(select book_id  from Book where lower(title) like '%harry%'),
			'2021-08-12')

-- Display the data
-- Select all the columns from the junction table
	select * from library
-- Select the name of the student and the title of the borrowed books
	with s_name_query as (select * from library l join student s 
						 on l.student_id = s.student_id)
	select s.name as student_name, b.title from s_name_query s join book b on s.book_fk_id = b.book_Id
	
	
-- Select the average age of the children, that borrowed the book Alice in Wonderland
	select avg(s.age)
	from student s join library l on s.student_id = l.student_id
	where l.book_fk_id in (select b.book_Id
	from library l join book b on l.book_fk_id = b.book_id where lower(title) like '%alice%')

-- Delete a student from the Student table, what happened in the junction table ?

	delete from student where student_id = 4
	-- Answer he is removed from the library
