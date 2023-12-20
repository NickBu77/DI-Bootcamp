CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);


UPDATE actors 
SET age='1970-01-01' 
WHERE first_name='Matt' AND last_name='Damon'
RETURNING 
    actor_id,
    first_name, 
    last_name,
    age;

-- Instructions
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- select count(actor_id)
-- from actors


-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
-- insert into actors (
--     first_name,
-- 	last_name
--     )
-- values ( 'Tom','Hanks')
-- ERROR:  Failing row contains (5, Tom, Hanks, null, null).null value in column "age" of relation "actors" violates not-null constraint 