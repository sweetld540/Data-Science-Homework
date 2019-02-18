use sakila;
#1A
select first_name, last_name from actor;

#1B
SELECT first_name, last_name,
	concat(first_name," ", last_name) AS 'Actor Name' 
	FROM actor;
    
#2A
select actor_id, first_name,last_name from actor where first_name = "JOE";

#2B
select actor_id, first_name, last_name from actor where last_name like "%GEN%";

#2C
select last_name, first_name from actor where last_name like '%Li%';

#2D
select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China');

#3A
ALTER TABLE actor
ADD COLUMN description BLOB After last_update;

#3B
ALTER TABLE actor
drop column description;

#4A
SELECT last_name, count(last_name)
from actor 
group by last_name 

#4B
SELECT last_name, count(last_name)
from actor 
group by last_name 
having COUNT(last_name) > 1;

#4C
update actor set first_name = 'Harpo' where actor_id = 172;

#4D
SET SQL_SAFE_UPDATES = 0;
update actor set first_name = 'GROUCHO' where first_name = 'Harpo';
select * from actor where first_name = 'GROUCHO';


#5A
Create Table New_Address (
  `new_id` int(11) NOT NULL AUTO_INCREMENT,
  `new_address` char(60) DEFAULT NULL,
  PRIMARY KEY (`new_id`)
);
drop table New_Address;


#6A
select staff.first_name, staff.last_name, address.address
from address
join staff on
staff.address_id = address.address_id;


#6B
select sum(payment.amount), staff.first_name, staff.last_name, staff.staff_id
from payment
join staff on
staff.staff_id = payment.staff_id
where payment.payment_date like '2005-08%'
group by staff.staff_id;


#6C
select count(film_actor.actor_id), film.title
from film
join film_actor
on film.film_id = film_actor.film_id
group by film.title;


#6D
select film.title, count(film.film_id)
from film
join inventory
on film.film_id = inventory.film_id
WHERE film.title ='HUNCHBACK IMPOSSIBLE'
group by film.film_id


#6E
select sum(payment.amount), customer.first_name, customer.last_name
from payment
left join customer
on customer.customer_id = payment.customer_id
group by customer.customer_id
order by customer.last_name ASC


#7A
select title
from film
where language_id in

(
	select language_id
	from language
    where name = "ENGLISH" 	
)
AND  title like 'K%' or title like 'Q%';


#7B

select actor.first_name, actor.Last_name
from actor
where actor_id in
(
	select actor_id
	from film_actor
	where film_id in

		(select film_id 
		from film 
		where film.title = "ALONE TRIP")
);


#7C

select last_name, first_name, email
from customer
join address on address.address_id = customer.address_id
join city on city.city_id = address.city_id
join country on country.country_id = city.country_id;


#7D
select title, category.name
from film
join film_category on film.film_id = film_category.film_id
join category on category.category_id = film_category.category_id
where category.name = "Family"; 


#7E
select title, count(payment.rental_id)
from payment
join rental on rental.rental_id = payment.rental_id
join inventory on inventory.inventory_id = rental.inventory_id
join film_text on film_text.film_id = inventory.film_id
group by title
order by count(rental.rental_id) desc;


#7F
select store_id, sum(payment.amount)
from staff join payment on staff.staff_id = payment.staff_id
group by store_id;


#7G
select store_id, city, country
from staff 
join address on address.address_id = staff.address_id
join city on city.city_id = address.city_id
join country on country.country_id = city.country_id
;


#7H
select category.name, sum(payment.amount)
from category 
join film_category on film_category.category_id = category.category_id
join inventory on inventory.film_id = film_category.film_id
join rental on rental.inventory_id = inventory.inventory_id
join payment on payment.rental_id = rental.rental_id
group by category.name
order by sum(payment.amount) desc;


#8A
create view top_five as 
	select category.name, sum(payment.amount)
	from category 
	join film_category on film_category.category_id = category.category_id
	join inventory on inventory.film_id = film_category.film_id
	join rental on rental.inventory_id = inventory.inventory_id
	join payment on payment.rental_id = rental.rental_id
	group by category.name
	order by sum(payment.amount) desc;

#8B
select * from top_five;

#8C
drop view top_five;
