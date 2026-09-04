#first program with if else in negative and positive number.
number=int(input("Enter Number: "))
if number<0:
    print("Negative Number")
else:
    print("Positive Number")



#disctionary main if else program with input user age.
dis={}
dis["age"]=int(input("Enter Yours Age: "))
if dis["age"]>18:
    print("Vote Is Eligible")
else:
    print("Vote Is Not Eligible")












#enter user 3 number and print 1 greatest number

firstnumber=int(input("Enter First Number: "))
secondnumber=int(input("Enter Second Number: "))
thirdnumber=int(input("Enter Third Number: "))

if(firstnumber>secondnumber and firstnumber>thirdnumber):
    print("Number 1 A Greatest",firstnumber)
elif(secondnumber>thirdnumber):
    print("Number First B Greatest",secondnumber)
else:
    print("Number First B Greatest",thirdnumber)




    












#print for student in user for control statement if elif else.


dis={
    "cricket":50,
    "football":25,
    "basketball":30,
    "vollyball":20,
    "hockey":15

}


userinput=input("Please Enter Academy Name: ")

if (userinput=="cricket"):
    print(dis["cricket"])
elif userinput=="football":
    print(dis["football"])
elif userinput=="basketball":
    print(dis["basketball"])
elif userinput=="vollyball":
    print(dis["vollyball"])
elif userinput=="hockey":
    print(dis["hockey"])
else:
    print("Please Enter Correct Number!")