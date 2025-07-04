import pymysql
from pymysql import Error as PyMySQL_Error

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(host='localhost', user="root", password="Bobby@1211", database='sheshadri_db', port=3306, charset="utf8")
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('Database disconnected')
    except:
        print('Database disconnection failed')

def create_db():
    query = 'create database IF NOT EXISTS sheshadri_db'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Database creation failed')


def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(30), phone_number bigint unique, salary float)'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except:
        print("Table creation failed")

def read_all_employees():
    query = 'select * from employees'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchll()
        for row in rows:
            print(row)
        print('All rows retrived')
        
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')


# connection = connect_db()

# connection.close() # to disconnect the DB

# disconnect_db(connection)

# create_db()

create_table()

read_all_employees()