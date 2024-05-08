import mysql.connector 

# Function to establish database connection
def connect_to_db():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="your_hostname",
            user="your_username",
            password="your_password",
            database="your_database_name"
        )
        print("Connected to the database successfully!")
        return connection

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        return None