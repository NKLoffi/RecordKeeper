import sqlite3

class Database:
    def __init__(self, db_name = 'data.db'):
        self.db_name = db_name

    def connect(self): # Establishes connection to the database
        return sqlite3.connect(self.db_name)
    
    def create_table(self):  # Creates the table

        CREATE_DATA_TABLE = """CREATE TABLE IF NOT EXISTS info (
                                InfoID INTEGER PRIMARY KEY AUTOINCREMENT,
                                FirstName TEXT NOT NULL,
                                LastName TEXT NOT NULL,
                                EmailId TEXT NOT NULL,
                                Dob DATE NOT NULL,
                                Sin TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                City TEXT NOT NULL,
                                Province TEXT NOT NULL
                                );"""
        
        connection = self.connect()
        with connection:
            connection.execute(CREATE_DATA_TABLE)
        connection.close()

    def insert_user_data(self, fname, lname, email, dob, sin, addy, city, prov): # function to insert user data

        INSERT_INFO = """ INSERT INTO info (
                            FirstName,
                            LastName,
                            EmailId,
                            Dob,
                            Sin,
                            Address,
                            City,
                            Province )
                            values( ?, ?, ?, ?, ?, ?, ?, ?
                        );"""
        connection = self.connect()
        with connection:
            connection.execute(INSERT_INFO, (fname, lname, email, dob, sin, addy, city, prov))
        connection.close()


