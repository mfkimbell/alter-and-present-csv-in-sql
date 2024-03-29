# alter-and-present-csv-in-sql

This project's goal was to learn SQL, MySQLWorkbench, and how to use Python to create databases in SQL, alter data, and then display those results. Additionally, I learned how to use SQL from the command line. I used https://www.freecodecamp.org/news/connect-python-with-sql/ to learn about altering SQL in Python.

**Tools Used:**
* `pandas` for organizing data into tables and displaying in python
* `mysql.connector` connecting to mysql
* `mysql` storing and manipulating data


The data for this project came from my Java_BookstoreManager files. The CSV files are named rentals and books:

<img width="684" alt="rentals" src="https://user-images.githubusercontent.com/107063397/203713149-33a0af3b-82a0-4dda-b460-dc3f757fffb3.png">

<img width="555" alt="Screen Shot 2022-11-24 at 12 46 50 AM" src="https://user-images.githubusercontent.com/107063397/203713164-e806e7d6-a382-41bc-a215-7ce14e0e6bc3.png">

The important Python functions are as follows:

`create_server_connection()` This allows the user to connect to their local MySQL server.

`create_database()` This allows the user to create a database using a python string.

`create_db_connection()` This allows the user to connect to a specific database on the server.

`execute_query()` This allows the user to execute SQL code using a python string on the SQL database.

`read_query()` This allows for the user to access the data from a database's table

The specific commands being used in SQL are basic. I am taking two tables, and doing a LEFT JOIN on the "Title" column of the books data with the "Title" of the rented books. The data being displayed is Book Title, RentalID (if there is one), and Renter(if there is one). I then create a table from this data and display it. The advantage of doing something like this would be for a user to know exactly which books are being rented, as well as which books are not being rented. With a slight alteration to the code, the user could get a table of all the books without someone renting them. 

This is how I formatted the string I would pass into execute_query() to create the tables:
```
create_rentals_table = """
CREATE TABLE rentals (
  rental_title VARCHAR(40),
  rental_id INT PRIMARY KEY,
  author VARCHAR(40),
  pages INT,
  publisher VARCHAR(40),
  year INT,
  customer VARCHAR(40),
  genre VARCHAR(40)
);
"""
```
To populate the data, I iterated through the dataframe object I created with the csv File. Scalable for large tables:
```
def customerCSVtoSQL():

     sql_pop_customers="INSERT INTO customers VALUES\n"

     for row in df3.itertuples(index=True, name='Pandas'):
        sql_pop_customers+=("('" + row.Name + "','" + row.Email + "','" + row.Number + "','" + row.Address + "'),\n")

     sql_pop_customers=sql_pop_customers[:-2]

     sql_pop_customers+=";"

     execute_query(connection, sql_pop_customers)
```

When the Datavase is first run, this is what executes in the terminal:

<img width="857" alt="Screen Shot 2022-11-24 at 12 39 45 AM" src="https://user-images.githubusercontent.com/107063397/203714323-222622ad-431c-4af7-9460-27fdc9f22fba.png">

After that, the newly created table is displayed using the pandas module:

<img width="861" alt="Screen Shot 2022-11-24 at 12 40 05 AM" src="https://user-images.githubusercontent.com/107063397/203714417-8bf0340b-390c-4684-bf15-eb3e35008217.png">

This is what the same table looks like when executing SQL from the command line:

<img width="302" alt="Screen Shot 2022-11-24 at 12 46 07 AM" src="https://user-images.githubusercontent.com/107063397/203715039-b978b55e-169e-4606-9c88-145b907a9327.png">


