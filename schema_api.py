import mysql.connector 

# Function to establish database connection
def connect_to_db():
    try:
        # Get user input for database connection details
        host = input("Enter the host name: "),
        user = input("Enter the user name: "),
        password = input("Enter the password: "),
        database = input("Enter the database name: ")

        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        print(f"Connected to the database {database} successfully!")
        return connection

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        return None