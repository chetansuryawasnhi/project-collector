create database project;
use project;
drop table users;
create table users(student_name varchar(50),college_name varchar(100),university_name varchar(50),project_title varchar(30),project_desc varchar(255));
select * from users;
create table collage(college_name varchar(100),university_name varchar(50),password varchar(20));
select * from collage;
insert into users values();
ALTER TABLE users
ADD status varchar(25);
SET SQL_SAFE_UPDATES = 0;

