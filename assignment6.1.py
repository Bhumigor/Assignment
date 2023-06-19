#Q1. What is a database? Differentiate between SQL and NoSQL databases.
"""
A database is a structured collection of data that is organized and managed in a way
that allows for efficient storage, retrieval, and manipulation of data. 
It provides a systematic way to store and manage large volumes of information.
"""
"""
SQL (Structured Query Language) databases are relational databases that use structured schemas to define the organization of data. 
They have a predefined schema that determines the structure of the data and the relationships between different tables.
SQL databases use SQL as the standard language for interacting with the data. 
Examples of SQL databases include MySQL, PostgreSQL, Oracle, and SQL Server.
"""
"""
NoSQL (Not Only SQL) databases, on the other hand, do not use a fixed schema and provide a more flexible data model. 
They are designed to handle unstructured, semi-structured, and structured data. 
NoSQL databases are typically used for handling large amounts of distributed data and are horizontally scalable. 
They use different data models such as key-value pairs, documents, columnar, or graph-based structures.
Some popular NoSQL databases include MongoDB, Cassandra, Redis, and Elasticsearch.
"""
"""
The main difference between SQL and NoSQL databases lies in their data models, schema flexibility, and scalability options. 
SQL databases are known for their strong consistency, ACID (Atomicity, Consistency, Isolation, Durability) properties, and support for complex transactions.
NoSQL databases, on the other hand, provide high scalability, flexible schema design, eventual consistency, and are often used in scenarios where data volume and performance are critical.
"""
#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
"""
DDL stands for Data Definition Language. 
It is a set of SQL statements used to define and manage the structure of a database.
DDL statements are responsible for creating, modifying, and deleting database objects such as tables, indexes, views, and schemas.
"""
#CREATE: The CREATE statement is used to create a new database object.
""" CREATE Table_Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);"""
#DROP: The DROP statement is used to delete a database object.
""" DROP TABLE Employees;
"""
#ALTER: The ALTER statement is used to modify the structure of an existing database object.
""" 
ALTER TABLE Employees
ADD COLUMN salary DECIMAL(10, 2);
"""
#TRUNCATE: The TRUNCATE statement is used to delete all the data from a table while keeping its structure intact.
""" 
TRUNCATE TABLE Employees;
"""
#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
""" 
DML stands for Data Manipulation Language. 
It is a set of SQL statements used to manage the data within a database. 
DML statements allow you to insert, update, and delete data from database tables.
"""
#INSERT: The INSERT statement is used to insert new records into a table. 
""" 
INSERT INTO Employees (name, age)
VALUES ('John', 25);
"""
#UPDATE: The UPDATE statement is used to modify existing records in a table.
""" 
UPDATE Employees
SET age = 30
WHERE name = 'John';
"""
#DELETE: The DELETE statement is used to delete records from a table. 
""" 
DELETE FROM Employees
WHERE age > 40;
"""
#Q4. What is DQL? Explain SELECT with an example.
""" 
DQL stands for Data Query Language. 
It is a subset of SQL used to retrieve data from a database. 
The most commonly used DQL statement is SELECT, which allows you to query and retrieve data from one or more tables based on specific conditions.
"""
""" 
The SELECT statement retrieves data from a table or multiple tables and can be customized to 
include or exclude specific columns, apply filters, sort the results, and perform aggregate functions.
"""
#SELECT * FROM Employees;
#SELECT name, age FROM Employees;
#SELECT * FROM Employees WHERE age > 30;

#Q5. Explain Primary Key and Foreign Key.
""" 
Primary Key: A primary key is a column or a set of columns in a table that uniquely identifies each record in the table. 
It enforces the entity's uniqueness and provides a way to establish relationships between tables. 
The primary key constraint ensures that the values in the primary key column(s) are unique and not null. 
Each table can have only one primary key. 
For example, in an "Employees" table, the "id" column can be defined as the primary key, ensuring that each employee has a unique identifier.
"""
""" 
Foreign Key: A foreign key is a column or a set of columns in a table that establishes a link or relationship between two tables. 
It refers to the primary key column(s) in another table and enforces referential integrity. 
Foreign keys are used to maintain the relationships between tables in a relational database. 
They ensure that the values in the foreign key column(s) match the values in the referenced primary key column(s) or are null. 
For example, in a "Orders" table, a foreign key column named "customer_id" can refer to the primary key column "id" in a "Customers" table, indicating which customer placed the order.
"""
#Q6. Write a Python code to connect MySQL to Python. Explain the cursor() and execute() method.
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
#The cursor() method is called on the connection object to create a cursor. The cursor is used to execute SQL statements and retrieve results.
#The execute() method is used to execute an SQL query. It takes the SQL query as a parameter.

#Q7. Give the order of execution of SQL clauses in an SQL query.
#1. FROM: Specifies the table or tables from which to retrieve data.
#2. WHERE: Applies conditions to filter the rows retrieved from the table(s).
#3. GROUP BY: Groups the rows based on specified columns.
#4. HAVING: Applies conditions to filter the groups created by the GROUP BY clause.
#5. SELECT: Specifies the columns to retrieve from the table(s).
#6. ORDER BY: Sorts the result set based on specified columns.
#7. LIMIT: Limits the number of rows returned by the query (optional).
