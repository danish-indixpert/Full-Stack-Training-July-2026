super_man_list=["Thor",
                "Ironman",
                "Batman",
                "Hulk",
                "Captaion America",
                "Spider-Man",
                "Wolverine",
                "Super-Man",
                "Flash",
                "Black-Panther"]
animal_list=["Tiger",
            "Lion",
            "Zebra",
            "Deer",
            "Goat"]

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")
menu()
def login_menu():
    print("1. Login")
    print("2. Exit")

def dashboard(super_man_list,animal_list):
    print("===========================")
    print("*        Dashboard        *")
    print("===========================")
    print("\nWelcome User\n",super_man_list,animal_list)
    
choice=int(input("Enter Your Choice: "))
if choice==1:
    user_id=int(input("Enter User ID: "))
    user_name=input("Enter User Name: ")
    user_age=int(input("Enter User Age: "))
    user_password=input("Enter User Password: ")
    print("Register Successfull!")
    login_menu()
    login_choice=int(input("Enter Login Choice: "))

    if login_choice==1:
        while True:
      
            login_user_id=int(input("Enter Login User ID: "))
            login_user_password=input("Enter Login User Password: ")
            if user_id==login_user_id and user_password==login_user_password:
                print("Login Successful!")
                dashboard(super_man_list,animal_list)
                break

            else:
                print("Invalid Username and Password")
    elif login_choice==2:
        print("Welcome User!")
    else:
        print("Invalid Choice!")



