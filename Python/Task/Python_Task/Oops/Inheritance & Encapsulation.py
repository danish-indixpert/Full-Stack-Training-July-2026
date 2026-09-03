import stdiomask
data = []
class Registration:
    def register(self):
        self.username = input("Enter Your Username: ")
        while True:
            if self.username.isalpha():
                break
            print("Please Alpha Value Only!")
        self._email_id = input("Enter Your Email ID: ")
        while True:
            if "@" in self._email_id and ".com " in self._email_id:
                break
            print("Please Correct Email ID")
        self.__password = stdiomask.getpass("Enter Your Password: ", mask="*")
        self.age = input("Enter Your Age: ")
        while True:
            if self.age.isdigit():
                break
            print("Please Integer Value Only")

        reg = {
            "username": self.username,
            "email_id": self._email_id,
            "password": self.__password,
            "age": self.age
        }
        
        data.append(reg)
        print("Registration Successful!")
class Display:
    def display(self):
        if data:
            for i, user in enumerate(data, start=1):
                print("\n====================")
                print(f"User {i}")
                print("====================")
                print("Username :", user["username"])
                print("Email ID :", user["email_id"])
                print("Password :", "*" * len(user["password"]))
                print("Age      :", user["age"])
            return
        print("No data found!")             
class Update:
    def update(self):
        if  data:
            username = input("Enter username to update: ")
            for user in data:
                    if user["username"] == username:
                        print("\n1. Update Username")
                        print("2. Update Email")
                        print("3. Update Password")
                        print("4. Update Age")
                        choice = input("Enter Your Update Choice: ")
        
                        if choice == "1":
                            user["username"] = input("Enter New Username: ")
                            print("Username updated successfully!")
        
                        elif choice == "2":
                            user["email_id"] = input("Enter New Email ID: ")
                            print("Email updated successfully!")
        
                        elif choice == "3":
                            new_password = stdiomask.getpass(
                                "Enter Your New Password: ", mask="*"
                            )
                            user["password"] = new_password
                            print("Password updated successfully!")
                        elif choice == "4":
                            user["age"] = input("Enter New Age: ")
                            print("Age updated successfully!")
                        else:
                            print("Invalid Choice!")
                        return
                    print("Username not found!")
            return
        print("No data found!")
class Delete:
    def delete(self):
        if data:
            print("====================")
            print("*      Delete      *")
            print("====================")
            print("1. Delete User")
            print("2. Delete Username")
            print("3. Delete Age")

            choice = input("Enter Your Delete Choice: ")

            username = input("Enter username: ")

            for user in data:
                if user["username"] == username:

                    if choice == "1":
                        data.remove(user)
                        print("User deleted successfully!")

                    elif choice == "2":
                        user["username"] = ""
                        print("Username deleted successfully!")

                    elif choice == "3":
                        user["age"] = "0"
                        print("Age deleted successfully!")
                    else:
                        print("Invalid Choice!")
                return
            print("User not found!")
class Menu(Registration, Display, Update, Delete):
    def Main_Menu(self):
        while True:
            print("\n====================")
            print("*       Menu       *")
            print("====================")
            print("1. Register")
            print("2. Display")
            print("3. Update")
            print("4. Delete")
            print("5. Exit")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.display()
            elif choice == "3":
                self.update()
            elif choice == "4":
                self.delete()
            elif choice == "5":
                print("Thank You!")
                break
            else:
                print("Invalid Choice!")


obj = Menu()
obj.Main_Menu()