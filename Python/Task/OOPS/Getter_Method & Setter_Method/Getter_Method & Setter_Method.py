class Bank:
    def __init__(self):
        self.__password="user@1234"

    def get_password(self):
        return self.__password

    def set_password(self,new_password):
        self.__password=new_password
        print("you are password is update successfully")


obj=Bank()
obj.set_password("newpassword@1001")
print("Update Password",obj.get_password())