schedule=[]
def meeting_menu():
    print("==============================")
    print("*          Meeting           *")
    print("==============================")
    while True:
        print("1. Meeting")
        print("2. Schedule")
        print("3. Exit")
        choice=input("Enter Your Choice: ")
        if choice=="1":
            zoom_meeting()
        elif choice=="2":
            zoom_schedule()
        elif choice=="3":
            print("Welcome User You Are Back!")
            break
        else:
             print("Invalid Your Choice!")

def zoom_end_menu():
    print("1. End Zoom Meeting")
    print("2. Exit")
    choice_one=input("Please Enter Your Choice: ")
    if choice_one=="1":
        print("Meeting End Successful ! You Back Is Dashboard")
        print("==============================")
        print("-        Zoom Dashboard      -")
        print("==============================")
        meeting_menu()
    elif choice_one=="2":
        print("Thank You User. You Are Is Back")
    else: 
        print("Invalid Your Choice!")

def zoom_meeting():
    while True:
        name=input("Please Enter Your Name: ")
        if name.isalpha():
            break
        print("Please Enter Alphabet Only!")
        time=input("Please Enter Time: ")
        print("Name: ",name)
        print("Meeting Time",time)
    print("Meeting Start Successful!")
    zoom_end_menu()

def zoom_schedule():
    zm=int(input("Plese Enter Your Schedule: "))
    print("Successsfully Schedule Your Meeting!")
    schedule.append(zm)
    
    

