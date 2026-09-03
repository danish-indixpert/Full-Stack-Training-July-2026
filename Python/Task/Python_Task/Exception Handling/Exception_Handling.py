import os
import datetime


try:
    firstnumber=int(input("Enter First Number: "))
    secondnumber=int(input("Enter Second Number"))
    thirnumber=int(input("Enter Third Number: "))
    print("Sum",firstnumber+secondnumber+thirnumber)

    
except Exception as e:
    print("Please Enter Correct Value Only!")
    with open("Error.Log",'w') as newfile:
        newfile.write(f"{e} path on\n {str(os.getcwd())} \n {str(datetime.datetime.now())}\n")
       
       
       

   