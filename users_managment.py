import mysql.connector
import socket

class User: 
    def __init__(self, user_id, user_name, first_name, last_name, password, is_admin, db_name):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_admin = is_admin
        self.db_name = db_name
def get_user_name():
    while True:
        user_name = input("please eneter your name: ")
        if user_name: 
            return user_name
        else:
            print("invalid input. Please enter a non-empty name.")
    
def get_user_password(): 
    while True:
        user_password = input("please eneter your password: ").strip()
        if len(user_password) >= 4:
            return user_password
        else:
            print("invalid password. Please enter a password with atleast four charecters long.")

def is_valid_hostname(hostname):
    """
    Check if the given string is a valid hostname.
    """
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]  # strip exactly one dot from the right, if present
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    return all(char in allowed for char in hostname)

def is_valid_ip_address(ip_address):
    """
    Check if the given string is a valid IP address.
    """
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

def get_user_host():
    while True:
        user_host = input("Please enter the hostname or IP address of the MySQL server: ").strip()
        if is_valid_hostname(user_host) or is_valid_ip_address(user_host):
            return user_host
        else:
            print("Invalid input. Please enter a valid hostname or IP address.")

def get_db():
    while True:
        db_name = input("Please enter the name of the data base: ")
        if db_name: 
            return db_name
        else:
            print("invalid input. Please enter a non-empty db_name.")





#if check_database_existence(db_name):
#return db_name     
#else:
#return create_db()

def does_database_exists(db_name):
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            user_host = get_user_host(),
            user_name = get_user_name(),
            user_password = get_user_password()
        )
        cursor = connection.cursor()

        # Execute SQL query to check if the database exists
        query = "SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = %s"
        cursor.execute(query, (db_name,))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print(f"The database '{db_name}' exists.")
            return True
        else:
            print(f"The database '{db_name}' does not exist.")
            return False

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage:
# check_database_existence("your_database_name")


def create_db():   
    db_name = get_db() 
    try:

        if not does_database_exists(db_name):
            connection = mysql.connector.connect(
            host="your_hostname",
            user="your_username",
            password="your_password"
            )
            cursor = connection.cursor()

         # Execute SQL query to create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS db_name")

        print("Database created successfully!")

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error) 

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




#def is_user_admin(name): 

#def create_user():
#def update_user():
#def delete_user():

#def connect_to_db():
 

def main(): 
    user_name = get_user_name()
    user_password = get_user_password()
    user_host = get_user_host()
    print("MySQL server hostname/IP:", user_host)
    


if __name__ == "__main__":
    main()
