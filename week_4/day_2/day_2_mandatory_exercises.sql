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
--when you delete a row from new_film, customer_reviews will also have that review deleted
