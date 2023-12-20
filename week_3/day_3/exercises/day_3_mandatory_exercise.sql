-- Exercise 1: DVD Rental
-- Instructions
-- Get a list of all the languages, from the language table.
select * from language;
-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
select f.title as film_title, f.description, l.name as language
from film f
join language l on f.language_id = l.language_id
;
-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
select f.title as film_title, f.description, l.name as language
from film f 
left join language l on f.language_id=l.language_id;
-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

create table new_film (id serial PRIMARY KEY, name varchar(200))

insert into new_film (name)
values ('007'),('Aladdin'), ('The Lion King');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
create table customer_review (review_id serial primary key NOT NULL, film_id INT REFERENCES new_film(id) ON DELETE CASCADE, language_id INT REFERENCES language(language_id) ON DELETE CASCADE,
							 title varchar, score smallint CHECK (score >= 1 AND score <= 10), review_text varchar(500), last_update timestamp default current_timestamp)				 
					
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review (film_id, language_id, title, score, review_text)
values
(1, 1, '007', 3, 'Boring movie'),
(2, 1, 'Aladdin Rev', 8, 'Excellent drama, a little long though')

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
	delete from customer_review
	where film_id =1
   -- Answer: when you delete a row from new_film, customer_reviews will also have that review deleted

--Exercise 2: DVD Rental
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
	select * from film where film_id in (8,133)
	
	update film
	set language_id = 2
	where film_id = 133
	
	update film set language_id = 3 where film_id = 8
-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
   -- Answer: Address_id, from the address table

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking
	Drop table customer_review
   --Answer: I want to check that I'm not deleting vital information. Other than that, seems like an easy step. It worked.

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
	select count(rental_id) from rental where return_date is NULL


-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
	select p.amount, r.rental_id, r.return_date
	from payment p join rental r on p.rental_id = r.rental_id where return_date is NULL
	order by amount desc
	limit 30
	
-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
-- but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
	select title from film
	where description like '%Sumo Wrestler%' and film_id in (select film_id from film_actor where 
	actor_id = (select actor_id from actor where first_name || ' ' || last_name = 'Penelope Monroe'))

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
	select * from film where length < 60 and rating = 'R' and description like '%Documentary%'

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.
	select title
	from film where film_Id = 
	(select film_id
	from inventory where inventory_id = (
	select r.inventory_id
	from rental r full join payment p on r.rental_id = p.rental_id
	where r.return_date between '2005-07-28' and '2005-08-01' and p.amount > 4 and r.customer_id = 
	(select customer_id
	from customer
	where last_name = 'Mahan' )
	)
	 )
	

-- The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
	 select *
	 from film where (lower(description) like '%boat%' or lower(title) like '%boat%') and film_id in (
		select film_id 
		from inventory 
		where inventory_id in (
		select inventory_id 
		from rental where rental_id in (
			 select rental_id from rental where customer_id = (
			  select customer_id 
			 from customer where last_name = 'Mahan' and first_name = 'Matthew'))))
			 order by replacement_cost desc
			 limit 1
	