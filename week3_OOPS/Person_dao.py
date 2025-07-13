import pymysql

class Person():
    def __ini__(self, name="", gender="", dob="", location=""):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.location = location
    def __str__(self):
        print(f"Name : {self.name} Location : {self.location}")

class db_operations():
    def __init__(self):
        pass

    def connect_db(self):
        connection = None
        try:
            connection = pymysql.connect(host='localhost', user="root", password="root", database='sheshadri_db', port=3306, charset="utf8")
            print('Database Connected')
        except:
            print('Database Connection Failed')
        return connection

    def disconnect_db(self, connection):
        try:
            connection.close()
            print('Database disconnected')
        except:
            print('Database disconnection failed')

    def create_db(self):
        query = 'create database IF NOT EXISTS sheshadri_db'
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            print('Database created')
            cursor.close()
            self.disconnect_db(connection)
        except:
            print('Database creation failed')

    def create_table(self):
        query = "create table IF NOT EXISTS Person(id int primary key auto_increment, name varchar(32) not null, gender char check(gender in('m','M', 'f','F')), location varchar(32), dob date);"
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            print('Table created')
            cursor.close()
            self.disconnect_db(connection)
        except:
            print("Table creation failed")

    def read_person_details(self):
        name = input("Enter Person name :")
        gender = input("Enter Person Gender :")
        dob = input("Enter Person Date of birth :")
        location = input("Enter Person location :")
        return (name, gender, dob, location)
    
    def get_latest_row_id(self):
        query = 'select max(id) from Person'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute(query)
            id = cursor.fetchone()
            cursor.close()
            self.disconnect_db(connection)
            return id[0]
        except:
            print("Geting id failed ")
    
    def insert_row(self, person):
        query = 'insert into Person (name, Gender, dob, location) values(%s, %s, %s, %s)'
        person_details = (person.name, person.gender, person.dob, person.location)
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute(query, person_details)
            connection.commit()
            print("Insertion done.")
            cursor.close()
            self.disconnect_db(connection)
            id = self.get_id()
            return id
        except:
            print("Insertion failed")
    
    def update_row(self, data):
        query = f'update person set name = %s gennder = %s dob = %s location = %s where id = %s'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query, data)
            if count == 0:
                print(f'Person with id = {id} not found')
            else:
                print(f'Person with id = {id} updated')
                connection.commit()
            cursor.close()
            self.disconnect_db(connection)
        except:
            print("Updation failed")

    def delete_row(self):
        query = f'delete from Person where id = {id}'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'Person with id = {id} not found')
            else:
                print(f'Person with id = {id} deleted')
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
        except:
            print("Delection failed")

    def search_row(self, id):
        row = None
        query = f'select * from Person where id = {id}'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'Person with id = {id} not found')
            else:
                row = cursor.fetchone()
                print(f'Person details are \n', str(row))
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
            return row
        except:
            print("Searching row failed")
            return row

    def list_all_rows(self):
        query = f'select * from Person'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'No rows found in the table')
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print(str(row))
            cursor.close()
            self.disconnect_db(connection)
            return rows
        except:
            print("Error in reading rows")


