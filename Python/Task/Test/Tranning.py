"""
dis_data={

    "age":int(input("Enter Your Age: "))
}
if dis_data["age"]>18:
    print("Vote is Eligible: ")
else:
    print("Vote is Note Eligible: ")
    print(type(dis_data))
"""
"""

dis={

    "id":int(input("Enter ID: ")),
    "name":input("Enter name: "),
    "address":input("Enter Address: "),
    "pincode":int(input("Enter Pincode: "))

}
if dis["pincode"]>=100000 and dis["pincode"]<=999999:
    print("Valid Pincode\n")
else:
    print("Not Valid Pincode\n")


print("================================")
print("*            Output            *")
print("================================")
print("ID: ",dis["id"])
print("Name: ",dis["name"])
print("Address: ",dis["address"])
print("Pincode: ",dis["pincode"])
"""


"""
english_marks=int(input("Enter English Marks: "))
hindi_marks=int(input("Enter Hindi Marks: "))
maths_marks=int(input("Enter Maths Marks: "))
total=english_marks+hindi_marks+maths_marks
average=total/3

if average>80:
    print("Grade: A")
elif average>70:
    print("Grade: B")
elif average>60:
    print("Grade: C")
elif average>33:
    print("Pass")
else:
    print("Fail")
"""


"""
english_marks=int(input("Enter English Marks: "))
hindi_marks=int(input("Enter Hindi Marks: "))
maths_marks=int(input("Enter Maths Marks: "))
science_marks=int(input("Enter Science Marks: "))
social_science_marks=int(input("Enter Social Science Marks: "))
total_marks=english_marks+hindi_marks+maths_marks+science_marks+social_science_marks
average=total_marks/5

if average>90 and average<100:
    print("Grade A+")
elif average>80 and average<90:
    print("Grade A")
elif average>70 and average<80:
    print("Grade B")
elif average>60 and average<70:
    print("Grade C")
elif average>50 and average<60:
    print("Grade D")
elif average>33 and average<50:
    print("Pass")
else:
    print("Fail")

"""
dictdata={

    "id":101,

    "name":"kailash singh",

    "address":"gurgaon",

    "email":"kailash.singh@indixpert.com"

    

    

}

 

for value in dictdata.values():

    print(value)






















