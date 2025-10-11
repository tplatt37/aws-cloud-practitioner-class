# SQL 

Here's some SQL (Structured Query Language) commands we can use with our Aurora Serverless v2 (Postgresql) database


# Create a Database Table

Run this commend in the Query Editor to create a database table:
```
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```

# Insert data into the table

Run this to add data rows to the table:
```
INSERT INTO customers (name, type) VALUES
    ('Sarah Mitchell', 'Retail'),
    ('David Chen', 'Wholesale'),
    ('Emma Rodriguez', 'Corporate'),
    ('Michael Thompson', 'Retail'),
    ('Joe Franks', 'Retail'),
    ('Bill Smith', 'Corporate');

```

# Show the rows in the table

```
select * from customers;
```

Show all the Retail customers:
```
select * from customers where type = 'Retail';
```

# Update a row

```
update customers set type = 'Corporate' where name = 'Joe Franks';
```
# Delete a row

```
delete from customers where name = 'Joe Franks';
```

NOTE: Transactions can't really be demonstrated from the RDS Query Editor.
