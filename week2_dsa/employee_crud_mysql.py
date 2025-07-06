import pymysql
# from pymysql import Error as PyMySQL_Error

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(host='localhost', user="root", password="root", database='sheshadri_db', port=3306, charset="utf8")
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

def desc_table():
    query = "desc employees"
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("All description of rows retrived ")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Description of rows failed")

def read_all_employees():
    query = 'select * from employees'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrived')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')

def add_row():
    query = 'INSERT INTO employees(id, name, designation, phone_number, salary, commission, years_of_experience, technology) ' \
    'values(%s, %s, %s, %s, %s, %s, %s)'
    value = ("raju", "employee", 9865232187, 100000, 0, 3, "App Designer")
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, value)
        print("Row added")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print("Row adding failed")

def update_row():
    query = 'update employees set salary = "95000" where id = 117'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Updation of row done")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Updation of row failed")

def delete_row():
    query = 'delete from employees where id = 117'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Delection of row done")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Delection of row failed")

def read_employee_details():
    print("Enter details of employee")
    name = input("Enter name of employee : ") 
    designation = input("Enter designation of employee : ")
    phone_number = int(input("Enter phone_number of employee : ")) 
    salary = int(input("Enter salary of employee : ")) 
    commission = int(input("Enter commission of employee : ")) 
    years_of_experience = int(input("Enter years_of_experience of employee : ")) 
    technology = input("Enter technology of employee : ")
    return (name, designation, phone_number, salary, commission, years_of_experience, technology)

def add_row_by_user():
    query = "insert into employees (name, designation, phone_number, salary, commission, years_of_experience, technology)" \
    "values(%s, %s, %s, %s, %s, %s, %s)"
    values = read_employee_details()
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        print("Row added to the emloyee")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print("Rows adding failed")

def update_row_by_user():
    id = int(input("Enter ID of employee : "))
    salary = int(input("Enter salary of employee : "))
    years_of_experience = int(input("Enter years of experience : "))
    phone_number = int(input("Enter number of employee : "))
    query = f'update employees set salary = {salary}, years_of_experience = {years_of_experience}, phone_number = {phone_number} where id = {id}'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Updation of row done")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Updation of row failed")


def delete_row_by_user():
    id = int(input("Enter id of employee to delete data : "))
    query = f'delete from employees where id = {id}'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Row deleted")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Row deletion failed")

def search_employee():
    id = int(input("Enter Id of employee to search : "))
    query = f'select * from employees where id = {id}'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        for column in row:
            print(column)
        print('Employee deatils retrived')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Employee details retrival failed')

# connection = connect_db()

# connection.close() # to disconnect the DB

# disconnect_db(connection)

# create_db()

# create_table()

# desc_table()

# read_all_employees()

# add_row()

# add_row_by_user()

# read_all_employees()

# update_row()

# update_row_by_user()

# read_all_employees()

# delete_row()

# delete_row_by_user()

# read_all_employees()

# search_employee()