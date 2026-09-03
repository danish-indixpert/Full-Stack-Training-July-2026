import os
import json

print("=========================")
print("*    Management Tool    *")
print("=========================")
while True:
    print("1. Create an Directory")
    print("2. Delete an Directory ")

    choice=input("Enter Your Choice: ")

    if choice=="1":
        create=input("Please Enter Create Directory Name: ")
        os.mkdir(create)
        print("Directory Create Successful!")

        print("=========================")
        print("*        New File       *")
        print("=========================")
        print("1. yes")
        print("2. no")
        option=input("Please Enter Your (yes/no) Option: ")
        if option=="yes":
            filename=input("Enter Create A New file Name: ")
            filename=os.path.join(create, filename)
            with open(filename,'w') as newfile:
                print("New File Create Successful!\n")
                print("=========================")
                print("*       Insert Data     *")
                print("=========================")
                print("1. yes")
                print("2. no")

                select=input("Please Enter (yes/no) Select : ")

                if select=="yes":
                        id=int(input("Enter Student ID: "))
                        name=input("Enter Student Name: ")
                        cls=input("Enter Student Class: ")
                        address=input("Enter Your Address: ")
                        city=input("Enter Your City: ")


                        student_subject={  
                            "hindi":int(input("Enter Your Hindi Marks: ")),
                            "english":int(input("Enter Your English Marks: ")),
                            "maths":int(input("Enter Your Maths Marks: ")),
                            "physics":int(input("Enter Your Physics Marks: ")),
                            "chemistry":int(input("Enter Your Chemistry Marks: "))
                        }
                        listdata={
                                "id"      :id,
                                "name"    :name,
                                "class"   :cls,
                                "address" :address,
                                "city"    :city,
                                "subject" :student_subject
                        }

                        with open(filename,'w')as onenewfile:
                            jsondata=json.dump(listdata,onenewfile,indent=4)
    
                        print("Json File Created & Data Successful\n")

                        print("=========================")
                        print("*        Text File      *")
                        print("=========================")
                        print("1. yes")
                        print("2. no")

                        textfile_choice=input("Please Enter Create A New Textfile (yes/no): ")

                        if textfile_choice=="yes":
                            with open(filename,'r') as text:
                                textfile=json.load(text)
                            with open("text.txt",'w') as newtextfile:
                                for key,value in textfile.items():
                                    newtextfile.write(f"{key}:{value}\n")
                                    
                                print("Text File Create & Data Insert Successful!")
                                break
                                    
                        elif textfile_choice=="no":
                            print("Thank You ! User")
                            break
                        else:
                            print("Invalid Choice!")
                elif select=="no":
                    print("You are is back!")
                else:
                    print("invalid Option!")
        elif option=="no":
            print("Thank You User ! You Are Is Stop")   
        else:
            print("Invalid Option")
    elif choice=="2":
        delete=input("Enter Your Delete Directory: ")
        os.rmdir(delete)
        print("directory delete successful!")
        break
    else:
        print("Invalid Your Choice!")