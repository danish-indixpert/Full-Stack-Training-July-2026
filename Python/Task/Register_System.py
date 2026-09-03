import json
import datetime
data_one=[]


class Stu:
    def register(self):
        print("==============================")
        print("*           Register         *")
        print("==============================")
        while True:
            try:
                self.uid=input("Enter Your UID: ")
                if self.uid.isdigit() and len(self.uid)>=3:
                    break
                else:
                    print("Invalid Id")
            except:
                print("Please Digit Value Only!")
            with open("Error.log",'a') as uii:
                uii.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Uid!!!\n")
        while True:
            try:
                self.name=input("Enter Your Name: ")
                if self.name.strip() and len(self.name)>=3:
                    break
                else:
                    print("Invalid Name")            
            except:
                print("Please Alphabet Value Only!")
            with open("Error.log",'a') as nn:
                nn.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Name!!! {self.uid}\n")
        while True:
            try:
                self.age=input("Enter Your Age: ")
                if self.age.isdigit():
                    break
                else:
                    print("Invalid Age")
            except:
                print("Please Integer (Digit) Value Only!")
            with open("Error.log",'a') as aa:
                aa.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Age!!! {self.uid}\n")
        while True:
            try:
                self.email=input("Enter Your Email ID: ")
                if "@" in self.email and ".com" in self.email:
                    break
                else:
                    print("Invalid email")
            except:
                print("Please Correct Email ID!")
            with open("Error.log",'a') as ee:
                ee.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Email!!! {self.uid}\n")
        while True:
            try:
                self.address=input("Enter Your Address: ")
                if self.address.strip() and len(self.address)>=3:
                    break
                else:
                    print("Invalid Addresss")
            except:
                print("Please Alphabet Value Only!")
            with open("Error.log",'a') as add:
                add.write(f"[{str(datetime.datetime.now())}] [EROOR] - Invalid Your Address!!! {self.uid}\n")
        while True:
            try:
                self.country=input("Enter Your Country: ")    
                if self.country.isalpha() and len(self.country)>=3:
                    break
                else:
                    print("Invalid country")
            except:
                print("Plsease Correct Your Country")
            with open("Error.log",'a') as cou:
                cou.write(f"[{str(datetime.datetime.now())}] [ERROR] - Invalid Your Country!!! {self.uid}\n")
        with open("students_register.txt",'a') as register:
            register.write(f"{self.uid} | {self.name} | {self.age} | {self.email} | {self.address} | {self.country}\n")
    
            registeration={
                "uid":self.uid,
                "name":self.name,
                "age":self.age,
                "email":self.email,
                "address":self.address,
                "country":self.country,
            }
            
            data_one.append(registeration)    
            with open("Oops.json",'w') as student_registration:
                json.dump(data_one,student_registration,indent=4)
            with open("Error.log",'a') as reg:
                reg.write(f"[{str(datetime.datetime.now())}] [INFO] - Registration Successful {self.uid}\n")    
            print("Registeration Successful!")
    def update(self):
        print("==============================")
        print("*         Update Menu        *")
        print("==============================")
        while True:
            print("1. Name Update")
            print("2. Age Update")
            print("3. Address Update")
            print("4. Country Update")
            print("5. Back")
            choice_update=input("please Enter Your update choice: ")
            update_uid=input("Enter UID ID: ")
            for update_data in data_one:
                if update_data["uid"] == update_uid:
                    if choice_update=="1":
                        try:                        
                            new_name=input("Enter You New Name: ")
                            if new_name.isalpha():
                                update_data["name"]=new_name
                                with open("Oops.json","w") as one_name:
                                    json.dump(data_one,one_name,indent=4)
                                print("Your Name Is Update")
                                break
                            else:
                                print("Invalid name")
                            with open("Error.log",'a') as n_one:
                                n_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Name Updated {update_uid}")
                        except:
                            print("Invalid [Error]")
                    elif choice_update=="2":
                        try:
                            new_age=input("Enter your new age: ")
                            if new_age.isdigit():
                                update_data["age"]=new_age
                                with open("Oops.json","w") as one_age:
                                    json.dump(data_one,one_age,indent=4)
                                print("Your Age Is Update")
                                break
                            else:
                                print("Invalid Age")
                            with open("Error.log",'a') as a_one:
                                a_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Age Updated {update_uid}")
                        except:
                            print("Invalid [Error]")
                    elif choice_update=="3":
                        try:
                            new_address=input("Enter you new address: ")
                            if new_address.isalnum():
                                update_data["address"]=new_address
                                with open("Oops.json","w") as one_address:
                                    json.dump(data_one,one_address,indent=4)
                                print("Your Address Is Update")
                                break
                            else:
                                print("Invalid Address")
                            with open("Error.log",'a') as add_one:
                                add_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Address Updated {update_uid}")
                        except:
                            print("Invalid [Error]")
                    elif choice_update=="4":
                        try:
                            new_country=input("Enter you new country: ")
                            if new_country.strip():
                                update_data["address"]=new_country
                                with open("Oops.json","w") as one_country:
                                    json.dump(data_one,one_country,indent=4)
                                print("Your Country Is Update")
                                break
                            else:
                                print("Invalid Country")
                            with open("Error.log",'a') as c_one:
                                c_one.write(f"[{str(datetime.datetime.now())}] [INFO] - Student Country Updated {update_uid}")
                        except:
                            print("invalid [Error]")
                    elif choice_update=="5":
                        self.menu()
                else:
                    print("Invalid Choice!")
            else:
                print("UID Not Found")
    def delete(self):
        print("==============================")
        print("*           Delete           *")
        print("==============================")
        one_uid=input("Enter Your UID: ")
        print("==============================")
        print("*           Yes/No           *")
        print("==============================")
        while True:
            print("1. yes")
            print("2. no")
            delete_choice=input("Enter Your Choice (yes/no): ")
            if delete_choice=="yes":
                for delete_data in data_one:
                    if delete_data["uid"]==one_uid:
                        data_one.remove(delete_data)
                        with open("Oops.json","w") as one_file:
                            json.dump(data_one,one_file,indent=4)
                        with open("Error.log",'a') as d:
                            d.write(f"[{str(datetime.datetime.now())}] [WARNNING] - Student Deleted {one_uid}")
                        print("Student Deleted Successful!")
                else:
                    print("UID Not Found")
            elif delete_choice=="no":
                print("Your Data is no Delete: ")
                break
            else:
                print("Invalid Choice!")
    def menu(self):
        print("==============================")
        print("*            Menu            *")
        print("==============================")
        while True: 
            print("1. Register")
            print("2. Update")
            print("3. Delete")
            choice=input("Enter Your Choice: ")
            if choice=="1":
                self.register()
            elif choice=="2":
                self.update()
            elif choice=="3":
                self.delete()
                break
            else:
                print("Invalid Choice!")
obj=Stu()
obj.menu()