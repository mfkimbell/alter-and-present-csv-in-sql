from serverSQL import *
import mysql.connector
from mysql.connector import Error
import pandas as pd
import IPython
import sqlite3

db = "bookstore" #this is the database
pw = #enter your password here

###THIS IS HOW YOU WOULD MAKE THE CONNECTION, TABLE QUERY, and DATABASE
connection = create_server_connection("localhost","root", pw)
create_database_query = "CREATE DATABASE " + db + " ;"
create_database(connection, create_database_query)
connection = create_db_connection("localhost","root", pw, db)


data = pd.read_csv ("~/Desktop/sql/SQLinPython/rentals.csv")   
df = pd.DataFrame(data)

data2 = pd.read_csv ("~/Desktop/sql/SQLinPython/books.csv")   
df2 = pd.DataFrame(data2)

data3 = pd.read_csv ("~/Desktop/sql/SQLinPython/customers.csv")   
df3 = pd.DataFrame(data3)


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
create_books_table = """
CREATE TABLE books (
  book_title VARCHAR(40) PRIMARY KEY,
  author VARCHAR(40),
  pages INT,
  publisher VARCHAR(40),
  year INT,
  copies INT,
  genre VARCHAR(40)
);
"""

create_customers_table = """
CREATE TABLE customers (
  name VARCHAR(40) PRIMARY KEY,
  email VARCHAR(40),
  number VARCHAR(40),
  address VARCHAR(40)
);
"""

def rentalCSVtoSQL():
    sql_pop_rentals="INSERT INTO rentals VALUES\n"

    for row in df.itertuples(index=True, name='Pandas'):
        sql_pop_rentals+=("('" + row.Title + "'," + str(row.RentalID) + ",'" + row.Author + "'," + str(row.Pages) + ",'" + row.Publisher + "'," + str(row.Year) + ",'" + row.Customer + "','" + row.Genre + "'),\n")

    sql_pop_rentals=sql_pop_rentals[:-2]

    sql_pop_rentals+=";"

    execute_query(connection, sql_pop_rentals)

def bookCSVtoSQL():
    sql_pop_books="INSERT INTO books VALUES\n"

    for row in df2.itertuples(index=True, name='Pandas'):
            sql_pop_books+=("('" + row.Title + "','" + row.Author + "'," + str(row.Pages) + ",'" + row.Publisher + "'," + str(row.Year) + "," + str(row.Copies) + ",'" + row.Genre + "'),\n")


    sql_pop_books=sql_pop_books[:-2]

    sql_pop_books+=";"

    execute_query(connection, sql_pop_books)

def customerCSVtoSQL():

     sql_pop_customers="INSERT INTO customers VALUES\n"

     for row in df3.itertuples(index=True, name='Pandas'):
        sql_pop_customers+=("('" + row.Name + "','" + row.Email + "','" + row.Number + "','" + row.Address + "'),\n")

     sql_pop_customers=sql_pop_customers[:-2]

     sql_pop_customers+=";"

     execute_query(connection, sql_pop_customers)
  
def JOINdata():
   join_command = "CREATE TABLE joined_table AS (SELECT books.book_title, rentals.rental_id, rentals.customer FROM books LEFT JOIN rentals ON books.book_title = rentals.rental_title);"
   execute_query(connection, join_command)

def printJoined():
   fetchTable = "SELECT * FROM joined_table;"
   results = read_query(connection,fetchTable)
   db = []
   for result in results:
    
    result = list(result)
    
    db.append(result)
   columns = ["Title","RentalID","Renter"]
   df = pd.DataFrame(db, columns=columns)
   df.style
   print(df.to_string())


execute_query(connection, create_books_table)
execute_query(connection, create_rentals_table)
execute_query(connection, create_customers_table)
rentalCSVtoSQL()
bookCSVtoSQL()
customerCSVtoSQL()
JOINdata()
printJoined()

