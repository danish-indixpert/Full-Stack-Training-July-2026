class ATM:
    def __init__(self,name,password,amount,branch):
        self.name=name
        self.__password=password
        self.__amount=amount
        self.branch=branch

    def display(self):
        print("Name",self.name)
        print("Password",self.__password)
        print("Amount",self.__amount)
        print("Branch",self.branch)

obj=ATM("danish","user@1234",10000,"ABD Joura")
obj.display()



#Use

#1. (Public Varible) isme koi kisi bhi cheez ko private ya protect nhi karte hai jaise: password ko ham aasaani se access kar sakte hai
#2. (Private Varible) single underscore (_) ka use kisi Cheez ko private karne ke liye use karte hai jaise: _danish
#3. (Protected Varible) isme ham double underscore (__) ka use kisi cheez ko protect & protected karna aur isko class ke ander hi use kar sakte hain

    