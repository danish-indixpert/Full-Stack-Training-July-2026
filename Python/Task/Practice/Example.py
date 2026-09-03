# # with open("text.txt",'r') as file:
# #     new=file.seek()
# #     print(new)


# with open("text.txt", "r") as file:
#     print(file.read(5))

#     file.seek(0)

#     print(file.read(5))

# try:
#     one=int(input("enter one number: "))
#     two=int(input("enter two number: "))
#     print("sum: ",one+two)
# except Exception as f:
#     print("not correct value")


# import uuid
# data=str(uuid.uuid4().int)[:10]
# print(data)



# class Addition:
#     def additionf(self,a,b):
#         print("This is Addition",a+b)
# class Subtraction(Addition):
#     def subtractionf(self):
#         print("This is Subtraction")
# class Multiplication(Subtraction):
#     def multiplicationf(self):
#         print("This is Multiplication")
# class Divide(Multiplication):
#     def divide(self):
#         print("This is Divide")


# obj=Divide()
# obj.additionf(10,20)
# obj.subtractionf()
# obj.multiplicationf()
# obj.divide()



# class student:
#     def second(self):
#         self.name=input("Enter Your Name: ")
#         self.age=input("Enter Your Age: ")
        
# obj=student()
# obj.second()




from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def atmpin(self):
        pass

class HDFC(ATM):
    def security(self):
        print("HDFC SECURITY")
    def atmpin(self):
        print("user@1234")

ob=HDFC()
ob.security()
ob.atmpin()
