from Dashboard import user_dashboard

users={
    "id":'1001',
    "pas":'danish1001'
}

def menu():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice=input("Enter Your Choice: ")
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("Thank You User!")
            break
        else:
            print("Invalid Choice")
def register():
    while True:
        u=(input("Enter User ID: "))
        if u.isdigit():
            break
        print("Please Enter Integer Value Only!")
        
    while True:
        p=input("Enter User Password: ")
        if p.isalnum():
            break
    if users["id"]==u and users["pas"]==p:
        print("Register Successful!")
            
    else:
        print("Invalid ID & Password!")    

def login():
    while True:
        user_id=(input("Enter User ID: "))
        if user_id.isdigit():
            break
        print("Please Enter Integer Value Only!")

    while True:
        
        password=input("Enter User Password: ")
        if password.isalnum():
            break
    if users["id"]==user_id and users["pas"]==password:
        print("Login Successful!")
        user_dashboard(user_id)
    else:
        print("Invalid ID & Password!")


    