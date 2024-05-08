import mysql.connector

class User: 
    def __init__(self, user_id, user_name, first_name, last_name, password):
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

def get_user_name():
    
    while True:
        user_name = input("please eneter your name: ")
        if user_name: 
            return user_name
        else:
            print("invalid input. Please enter a non- empty name.")
    



#def get_user_password(): 


#def is_admin(name, password): 

#def create_user():
#def update_user():
#def delete_user():

#def connect_to_db():
#def create_db(): 

def main(): 
    get_user_name()
    


if __name__ == "__main__":
    main()
