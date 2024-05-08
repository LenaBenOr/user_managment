import mysql.connector
import socket

class User: 
    def __init__(self, user_id, user_name, first_name, last_name, password, is_admin):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_admin = is_admin
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

#def create_db():   
    # Connect to MySQL server
    #try:
      #  connection = mysql.connector.connect(
       #     host=get_user_host(),
        #    user=get_user_name(),
         #   password=get_user_password()
        #)
        #cursor = connection.cursor()     

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
