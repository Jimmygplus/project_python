# SimpleOrderRoom
2018 workshopII continue exercise.
Python3.x
Simple Online Order Room

============================
###Function

####Admin -- 
	

- Login
- Add User
- Add Room
- Manage Room order list

####User -- 
	
- Login
- Book Room
- Manage Room list(Check - Remove order)


============================
### Try MySQL

- install MySQL dependence

	~~~
	pip install wheel
	pip install pymysql

	~~~

- create db - testweb

- create table todo
	~~~
	CREATE TABLE todo ( id int not null primary key  AUTO_INCREMENT, title text, created TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, done varchar(1) DEFAULT 'f' )

	~~~

- create testdb.py

- create folder templates

- create testdb.html into folder templates

- run
	~~~
		python3 testdb.py 1234 
	~~~
