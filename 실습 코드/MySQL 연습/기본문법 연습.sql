create database 생활코딩;
use 생활코딩;
drop table if exists topic;

create table topic(
	id int(11) NOT NULL auto_increment,
	title varchar(100) NOT null,
    created datetime NOt null,
    primary key(id)
    );
    
insert into topic (title, created) values ('First_book', now());
insert into topic (title, created) values ('Second_book', now());
insert into topic (title, created) values ('Third_book', now());
insert into topic (title, created) values ('fourth_book', now());

select * from topic;

select title,created from topic order by id;

update topic set title='My_First_book' where title='First_book';

select title,created from topic order by id;

delete from topic where id=1;

select title,created from topic order by id;
insert into topic (title, created) values ('First_book', now());

update topic set title='My_First_book', created=now() where title='My_First_book';