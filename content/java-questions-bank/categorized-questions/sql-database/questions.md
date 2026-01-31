---
title: "SQL & Database Interview Questions"
date: 2026-01-30
draft: false
categories: ["SQL & Database"]
---

## Beginner (Basics & Definitions)
1. [What is SQL?](#1-what-is-sql)
2. [What is Database Testing?](#2-what-is-database-testing)
3. [Did you do Database Testing?](#3-did-you-do-database-testing)
4. [Explain primary key and foreign key?](#4-explain-primary-key-and-foreign-key)
5. [What are JOINs in SQL?](#5-what-are-joins-in-sql)
6. [Explain inner join?](#6-explain-inner-join)
7. [What is left join? Whether common values will be available in left join?](#7-what-is-left-join-whether-common-values-will-be-available-in-left-join)
8. [What is the difference between JOIN and UNION in SQL?](#8-what-is-the-difference-between-join-and-union-in-sql)
9. [What is structure in SQL?](#9-what-is-structure-in-sql)
10. [What is the difference between Oracle and SQL?](#10-what-is-the-difference-between-oracle-and-sql)
11. [What is the difference between SQL and MySQL?](#11-what-is-the-difference-between-sql-and-mysql)
12. [What is the difference between delete and truncate?](#12-what-is-the-difference-between-delete-and-truncate)
13. [Can we get truncated data back?](#13-can-we-get-truncated-data-back)
14. [What is limit in SQL?](#14-what-is-limit-in-sql)

## Intermediate (Queries & Practical Tasks)
1. [Write a query to select a table from the DB?](#write-a-query-to-select-a-table-from-the-db)
2. [Give some query command line from SQL?](#give-some-query-command-line-from-sql)
3. [Write an SQL query to find the Employee name from the table?](#write-an-sql-query-to-find-the-employee-name-from-the-table)
4. [SQL command to get common data in two tables?](#sql-command-to-get-common-data-in-two-tables)
5. [Mention some SQL queries you have used?](#mention-some-sql-queries-you-have-used)
6. [Write an SQL query for the sum of the values in a particular column?](#write-an-sql-query-for-the-sum-of-the-values-in-a-particular-column)
7. [Explain drop, delete, and truncate in SQL?](#explain-drop-delete-and-truncate-in-sql)
8. [Write an SQL query to find headers only in a table?](#write-an-sql-query-to-find-headers-only-in-a-table)
9. [How do you use SQL in software testing?](#how-do-you-use-sql-in-software-testing)
10. [What is the purpose of SQL in your project?](#what-is-the-purpose-of-sql-in-your-project)
11. [How will you connect MySQL to Selenium code?](#how-will-you-connect-mysql-to-selenium-code)
12. [How do you initialize a database connection in your automation?](#how-do-you-initialize-a-database-connection-in-your-automation)
13. [How do you maintain the test data in your project?](#how-do-you-maintain-the-test-data-in-your-project)

## Advanced (Complex Scenarios & Data Integrity)
1. [Write a query to find duplicate records in a table?](#write-a-query-to-find-duplicate-records-in-a-table)
2. [Write an SQL query to find the second largest salary?](#write-an-sql-query-to-find-the-second-largest-salary)
3. [Write a query for second maximum value?](#write-a-query-for-second-maximum-value)
4. [How would you validate data integrity between the front end and the database?](#how-would-you-validate-data-integrity-between-the-front-end-and-the-database)
5. [What is SQL injection and how do you test for it?](#what-is-sql-injection-and-how-do-you-test-for-it)
6. [Scenario: Two tables with common date, how do you print all data excluding the date?](#scenario-two-tables-common-date-java-perspective)
7. [Scenario: How do you handle the previous scenario with lakhs of data?](#scenario-handling-lakhs-of-data-in-tables)
8. [Scenario: Table multiplication logic?](#scenario-table-multiplication-logic)
9. [How do you validate the JSON response in API testing against database values?](#how-do-you-validate-the-json-response-in-api-testing-against-database-values)

---

## Questions with Answers

### Beginner (Basics & Definitions) - Answers

### 1. What is SQL? {#1-what-is-sql}
**Answer**: SQL (Structured Query Language) is the standard language used to interact with relational databases. It allows you to create, read, update, and delete data.

### 2. What is Database Testing? {#2-what-is-database-testing}
**Answer**: It is the process of verifying that the data stored in the database is accurate, complete, and consistent with the application's business logic.

### 3. Did you do Database Testing? {#3-did-you-do-database-testing}
**Answer**: Yes, I have performed backend testing by connecting to the database using **JDBC** to validate that UI entries are correctly saved in the DB.

### 4. Explain primary key and foreign key? {#4-explain-primary-key-and-foreign-key}
**Answer**:
- **Primary Key**: A unique identifier for every record in a table. It cannot be null.
- **Foreign Key**: A field in one table that links to the primary key of another table, establishing a relationship.

### 5. What are JOINs in SQL? {#5-what-are-joins-in-sql}
**Answer**: Joins are used to combine rows from two or more tables based on a related column between them.

### 6. Explain inner join? {#6-explain-inner-join}
**Answer**: Returns only the records that have matching values in **both** tables.

### 7. What is left join? Whether common values will be available in left join? {#7-what-is-left-join-whether-common-values-will-be-available-in-left-join}
**Answer**: Returns all records from the left table and the matching records from the right table. **Yes**, common values are included. If no match, the right side is `NULL`.

### 8. What is the difference between JOIN and UNION in SQL? {#8-what-is-the-difference-between-join-and-union-in-sql}
**Answer**:
- **JOIN**: Combines columns from different tables side-by-side.
- **UNION**: Combines the results of two SELECT statements into a single vertical list (stacks rows).

### 9. What is structure in SQL? {#9-what-is-structure-in-sql}
**Answer**: It refers to the **Schema**—the organization of data, tables, relationships, and constraints in the database.

### 10. What is the difference between Oracle and SQL? {#10-what-is-the-difference-between-oracle-and-sql}
**Answer**: **SQL** is the language; **Oracle** is a specific Relational Database Management System (RDBMS) that uses SQL.

### 11. What is the difference between SQL and MySQL? {#11-what-is-the-difference-between-sql-and-mysql}
**Answer**: **SQL** is the language; **MySQL** is an open-source RDBMS that uses the SQL language.

### 12. What is the difference between delete and truncate? {#12-what-is-the-difference-between-delete-and-truncate}
**Answer**:
- **DELETE**: DML command. Deletes specific rows (with `WHERE`). Logged and can be rolled back.
- **TRUNCATE**: DDL command. Deletes all rows. Not logged individually, faster, and cannot be rolled back easily.

### 13. Can we get truncated data back? {#13-can-we-get-truncated-data-back}
**Answer**: No, TRUNCATE is a permanent operation because it does not record individual row deletions in the transaction log.

### 14. What is limit in SQL? {#14-what-is-limit-in-sql}
**Answer**: A clause used to specify the maximum number of records to return in a result set (e.g., `LIMIT 10`).

### Intermediate (Queries & Practical Tasks) - Answers

### 1. Write a query to select a table from the DB? {#write-a-query-to-select-a-table-from-the-db}
**Answer**: `SELECT * FROM table_name;`

### 2. Give some query command line from SQL? {#give-some-query-command-line-from-sql}
**Answer**: `SELECT`, `UPDATE`, `INSERT`, `DELETE`, `CREATE`, `DROP`, `ALTER`.

### 3. Write an SQL query to find the Employee name from the table? {#write-an-sql-query-to-find-the-employee-name-from-the-table}
**Answer**: `SELECT emp_name FROM Employees;`

### 4. SQL command to get common data in two tables? {#sql-command-to-get-common-data-in-two-tables}
**Answer**: `SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;`

### 5. Mention some SQL queries you have used? {#mention-some-sql-queries-you-have-used}
**Answer**:
- `SELECT * FROM Users WHERE status='active';`
- `UPDATE Orders SET total=100 WHERE id=1;`
- `INSERT INTO Logs (msg) VALUES ('Test pass');`

### 6. Write an SQL query for the sum of the values in a particular column? {#write-an-sql-query-for-the-sum-of-the-values-in-a-particular-column}
**Answer**: `SELECT SUM(salary) FROM Employees;`

### 7. Explain drop, delete, and truncate in SQL? {#explain-drop-delete-and-truncate-in-sql}
**Answer**:
- **DELETE**: Removes rows based on condition.
- **TRUNCATE**: Removes all rows but keeps table structure.
- **DROP**: Removes the entire table (data and structure) from the database.

### 8. Write an SQL query to find headers only in a table? {#write-an-sql-query-to-find-headers-only-in-a-table}
**Answer**: `SELECT * FROM table_name WHERE 1=0;` (Or query information_schema).

### 9. How do you use SQL in software testing? {#how-do-you-use-sql-in-software-testing}
**Answer**: For data validation, verifying UI changes in the backend, and preparing test data directly in the database.

### 10. What is the purpose of SQL in your project? {#what-is-the-purpose-of-sql-in-your-project}
**Answer**: To validate that user-submitted data (e.g., a registration form) is correctly and accurately saved in the backend database.

### 11. How will you connect MySQL to Selenium code? {#how-will-you-connect-mysql-to-selenium-code}
**Answer**: By using the **JDBC (Java Database Connectivity)** API. I add the MySQL connector dependency to `pom.xml`.

### 12. How do you initialize a database connection in your automation? {#how-do-you-initialize-a-database-connection-in-your-automation}
**Answer**:
```java
Connection con = DriverManager.getConnection(url, username, password);
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

### 13. How do you maintain the test data in your project? {#how-do-you-maintain-the-test-data-in-your-project}
**Answer**: By using SQL scripts to reset the database state before execution or to insert specific data sets needed for complex scenarios.

### Advanced (Complex Scenarios & Data Integrity) - Answers

### 1. Write a query to find duplicate records in a table? {#write-a-query-to-find-duplicate-records-in-a-table}
**Answer**:
```sql
SELECT name, COUNT(name) 
FROM Employees 
GROUP BY name 
HAVING COUNT(name) > 1;
```

### 2. Write an SQL query to find the second largest salary? {#write-an-sql-query-to-find-the-second-largest-salary}
**Answer**:
```sql
SELECT MAX(salary) FROM Employees 
WHERE salary < (SELECT MAX(salary) FROM Employees);
```

### 3. Write a query for second maximum value? {#write-a-query-for-second-maximum-value}
**Answer**: (Same as second largest salary query above).

### 4. How would you validate data integrity between the front end and the database? {#how-would-you-validate-data-integrity-between-the-front-end-and-the-database}
**Answer**: By performing an end-to-end test where I input data in the UI, then run an SQL query to fetch that record and assert that every field matches the UI input.

### 5. What is SQL injection and how do you test for it? {#what-is-sql-injection-and-how-do-you-test-for-it}
**Answer**: A security vulnerability. I test it by entering `' OR 1=1 --` into input fields to see if I can bypass login or retrieve unauthorized data.

### 6. Scenario: Two tables with common date, how do you print all data excluding the date? {#scenario-two-tables-common-date-java-perspective}
**Answer**: In SQL, I would explicitly name all columns except `date`. In Java, I would use `rs.getMetaData()` to get all column names, filter out "date", and then print the rest.

### 7. Scenario: How do you handle the previous scenario with lakhs of data? {#scenario-handling-lakhs-of-data-in-tables}
**Answer**: I would use **pagination** (`LIMIT` and `OFFSET`) or batch processing in my Java code to avoid memory overflows.

### 8. Scenario: Table multiplication logic? {#scenario-table-multiplication-logic}
**Answer**:
```sql
SELECT t1.name, (t1.quantity * t2.price) as Total 
FROM table1 t1 
JOIN table2 t2 ON t1.product_id = t2.id;
```

### 9. How do you validate the JSON response in API testing against database values? {#how-do-you-validate-the-json-response-in-api-testing-against-database-values}
**Answer**: I use Rest Assured to get the API response and JDBC to get the DB record. I then convert both into **Maps** or **POJOs** and use `Assert.assertEquals(apiObj, dbObj)`.