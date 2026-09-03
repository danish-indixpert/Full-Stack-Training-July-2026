print("=========================================================")
print("*                    STUDENT ID CARD                    *")
print("=========================================================")

#student={}
institutename=input("Enter Institute Name: ")
name=input("Enter Student Full Name: ")
fathername=input("Enter Father Name: ")

while True:
    rollnumber=input("Enter Student Roll Number: ")
    if rollnumber.isdigit():
        break
    print("Please Enter Intger Value Only!")

studentclass=input("Enter Student Class: ")

while True:
    section=input("Enter Section: ")
    if section.isalpha():
        break
    print("Plese Enter String Value Only!")

while True:
    department=input("Enter Department: ")
    if department.isalpha():
        break
    print("Please Enter String Value Only!")

city=input("Enter City: ")

while True:
    bloodgroup=input("Enter Blood Group: ")
    if bloodgroup.isalpha():
        break
    print("Please Enter String Value Only!")

mobilenumber=input("Enter Mobile Number: ")

print("============================================")
print("*                INDIXPERT                 *")
print("============================================")

print(name.center(35,'*'))


print("------------- STUDENT DETAILS -------------")
print("Student Name : ",name.title())
print("Father Name  : ",fathername.title())
print("Roll Number  : ",rollnumber.zfill(10))
print("Class        : ",studentclass.title())
print("Section      : ",section.upper())
print("Department   : ",department.title())
print("City         : ",city.title())
print("Blood Group  : ",bloodgroup.upper())
print("Phone        : ",(mobilenumber))


print("------------- NAME ANALYSIS -------------")
print("Upper Name      : ", name.upper())
print("Lower Name      : ", name.lower())
print("Swapcase Name   : ",name.swapcase())
print("Character Count : ", len(name))
print("Word Count      : ", name.count(name))
print("Letter'a' Count : ", name.count('a'))
print("First Space At  :", name.find(" "))


print("------------- VALIDATION REPORT  -------------")
print("Name Valid       : ",name.isalpha())
print("Father Valid     : ",fathername.isalpha())
print("Roll No. Valid   : ",rollnumber.isdigit())
print("Phone No. Valid  : ",mobilenumber.isdigit())

idcard=[department.title(),section.upper(),rollnumber.zfill(10)]
hyphen='-'
print("\nStudent Code     : ",hyphen.join(idcard))

print("=========================================================")
print("*            ID CARD GENERATE SUCCESSFULLY              *")
print("=========================================================")