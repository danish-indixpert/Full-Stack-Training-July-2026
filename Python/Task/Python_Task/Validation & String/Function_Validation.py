students=["spider-man","hulk","batman","captain-america","thor"]
passwords=["1001","1002","1003","1004","1005"]

def menu():
    print("=".center(40,'='))
    print(" Menu ".center(40,'*'))
    print("=".center(40,'='))
    print("1. Register")
    print("2. Login")
    print("3. Delete")
    print("4. Exit")


def register():
    while True:
        student_id = input("Enter Student ID: ")
        if student_id.isalpha():
            break
        print("Please Enter (Student_ID) Alphabet Data Only")

    while True:
        password = (input("Enter Your Password: "))
        if password.isdigit() :
            break

        print("Please Enter (Password) Digit Data Only!")

    students.append(student_id)
    passwords.append(password)
    print("Registration Successful!")
def login():
    student_id=input("Enter Student ID: ").strip()
    password=input("Enter Student Password: ").strip()

    if student_id in students:
        index=students.index(student_id)

        if passwords[index]==password:
            print("Login Successful!")
            dashboard(students,passwords)
        else:
            print("Invalid Password")
    else:
        print("Invalid Student ID!")
def dashboard(student_id,password):
    print("Dashboard".center(30,'='))
    print("Welcome",student_id,password)
    

def delete():
    student_id=input("Enter Student ID: ")
    if student_id in students:
        index=students.index(student_id)
        students.pop(index)
        passwords.pop(index)
        print("Student Delete Successfull!")
    else:
        print("Student Not Found!")
    
while True:
    menu()
    choice=int(input("Enter Your Choice: "))
    
    if choice==1:
        register()
    elif choice==2:
        login()
    elif choice==3:
        delete()
    elif choice==4:
        print("Thank You User!")
        break
    else:
        print("Invalid Choice!")