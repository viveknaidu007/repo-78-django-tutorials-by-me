# repo-78-django-tutorials-by-me
here im writing the coe or django   porjetc with clear documentation

# for installations
pip install Django

# create and run our first Django project
django-admin startproject ________

# for running the code:
python manage.py  runserver

# for running in specific port
python manage.py runserver 8888 

# why settings.py
we can set our apps folder
and what databse we r using

* we will map every view with url , then if user gives url 

# for documentations
https://docs.djangoproject.com/en/5.0/

https://docs.djangoproject.com/en/5.0/intro/tutorial01/

# steps:
1.create an application under project
2.add this application entry in settings.py file
3.create views(function bases/class based)
4.link views with urls in urls.py file
5.run the project

# for staarting applications
1. django-admin startapp admissions


********************** Database ****************************
# for database 
install mysql 

1. open command prompt
2. type a command : mysql -u root -p
3. enter the password

* mysql> this is called MYSQL prompt

# databse Operations: CRUD Operations
1. Create
2. Read
3. Update

# DBMS minimun basics to start implementing database connectivity in projects

1. Create: creating a table and insert data     create, insert
2. Read: reading or extracting data from the table   select
3. update: updating existing data in a table       update
4. delete: deleting data from a table       delete

# mysql : for logging into sql prompt in cmd and give ur password 
mysql -u root -p

# databses :
school -----> tables

# create a database:
create database school;

# creating table and inserting data
create table tablename (col1 datatype, col2 datatype.... )

ex:
create table students(rno int, name varchar(1000), class varchar(1000));



insert into ___________ values(..);

ex:
insert into students values(1,"vivek","L.K.G);



# before we creating a table , we have to select the dtabase we want to use or if we didnt select the datasbe it will show

use databasename

# for using the databse
use school 

# for seeing our present database we are using now 
select database();

# for seeing the tables in database , it will show tables we created in the database
show tables;

# to see the data inside the table we use read command in CRUD operations "select"

select * from school

# Reading:
select name,class from students where rno=1

# update:
update tablename set col=value
update students set name='teja' where rno=1;

# delete:
delete from tablename 
ex:
delete from students where rno=2;