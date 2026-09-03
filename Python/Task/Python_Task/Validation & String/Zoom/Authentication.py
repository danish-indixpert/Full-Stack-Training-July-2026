from Dashboard_P import zoom_dashboard

zoom_data={}
zoom_user=[]
def zoom_menu():
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice=input("Enter Your Choice: ")
        if choice=="1":
            zoom_register()
        elif choice=="2":
            zoom_login()
        elif choice=="3":
            print("Thank You User!")
        else:
            print("Invalid Choice!")

def zoom_register():
    print("==============================")
    print("*          Register          *")
    print("==============================")
    while True: 
        user_id=input("Enter User ID: ")
        if user_id.isdigit():
            break
        print("Please Enter Integer Value Only!")
    password=input("Enter Your Password: ")
    print("Registration Successful ! Get 2 Press & Login")
    zoom_login()
def zoom_login():
    print("==============================")
    print("*           Login            *")
    print("==============================")

    while True:
        login_id=input("Enter Your Login ID: ")
        if login_id.isdigit():
            break
        print("Please Enter Integer Value Only!")

    while True:
        login_password=input("Enter Your Login Password: ")
        if login_password.isalnum():
            break
        print("please Enter Alphabet Only!")
    
    print("Login Successfull!")
    zoom_dashboard(login_id)
