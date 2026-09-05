#1. 
import os
directory=input("Enter Directory (Folder) Name: ")
os.mkdir(directory)
print("Directory Created Successfull")
file_=input("Enter File Name: ")
print("File Created Successull and with Directory")
with open(os.path.join(directory,file_),"w") as file:
    file.write("Hello World")







#2. 
dire=input("Enter Directory (Folder) Name: ")
os.mkdir(dire)
print("Directory Created Successfull")
with open(dire+"/main.py",'w') as file_file:
    file_file.write("Hello World")
