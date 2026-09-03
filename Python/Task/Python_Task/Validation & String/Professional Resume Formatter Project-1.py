print("=======================================================")
print("*            PROFESSIONAL RESUME FORMATTER             ")
print("=======================================================")

while True:
    name=input("Enter Full Name: ")
    if name.isalpha():
        break
    print("Please Enter String Value Only!")
while True:    
    father_name=input("Enter Father Name: ")
    if father_name.isalpha():
        break
    print("Please Enter String Value Only!")
while True:
    email=input("Enter Email ID: ")
    if email.count('@') and email.count('.com'):
        break
    print("Please Enter Correct Gmail ID!: ")
while True:
    phone_number=input("Enter Phone Number: ")
    if phone_number.isdigit():
        break
    print("Please Enter Integer Value Only!")
city=input("Enter City: ")
country=input("Enter Country: ")
qualification=input("Enter  Qualification: ")
university=input("Enter University: ")
skills=input("Enter Skills: ")
languages=input("Enter Languages: ")
experience=input("Enter Experience: ")
career_objective=input("Enter Career Objective: ")
   
print("\n--------------- PERSONAL INFORMATION FORMATING ---------------")
print("Name         : ",name.title())
print("Country      : ",country.upper())
print("City         : ",city.capitalize())
print("Qualification: ",qualification.upper())

print("\n---------------------- SKILLS FORMATTER ----------------------")
skill=skills.split(',')
sep=' | '
print("Skills   : ", sep.join(skill))

print("\n---------------------- LANGUAGE FORMATTER ----------------------")
lang=languages.split(',')
pipe=' | '
print("Skills   : ", pipe.join(lang))

print("\n----------------------- RESUME ANALYSIS -----------------------------")
print("Uppercase Name   : ", name.upper())
print("Lowercase Name   : ", name.lower())
print("Swapcase Name    : ", name.swapcase())
print("Character Count  : ", len(name))
print("Word Count       : ", name.count(name))
print("Letter Frequency : ", name.count('d'))
print("Space Position   : ", name.find(" "))

print("\n------------------------- EMAIL ANALYSIS ---------------------------")
print("Number of @ symbol   : ", email.count('@'))
print("Position of @ symbol : ", email.find('@'))
if '.com' in email:
    presence='True'
else:
    presence='False'
print("Presence of .com     : ",presence)

print("\n---------------------- RESUME ID GENERATION -----------------------")
idgeneration=[name.upper(),city.upper(),qualification.upper()]
hyphen='-'
print("Student Code     : ",hyphen.join(idgeneration))  