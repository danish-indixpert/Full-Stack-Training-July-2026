#print("Print 1-10 Number:")

# for number in range(1,11):
#     print(number)





# #Even Number ke Liye
# for number in range(1,11):
#     if number%2==0:
#         print("Even Number: ",number)  





data={
    "id":1001,
    "name":'Danish Khan',
    "address":'Dholpur',
    "email":'danish@gmail.com',
    "contact":8269192353,
    "pincode":'476221',
    "qualification":'10th, 12th, BA'
}


print("Outpupt: ")
for key,value in data.items():
    print(f"{key}:{value}")
