lis=[
    {"name":"Riya","marks":85},
    {"name":"Rohan","marks":42},
    {"name":"Priya","marks":90},
    {"name":"Rahul","marks":33},
    {"name":"Anaya","marks":80}

]
pass_count=0
fail_count=0
print("================================")
print("*         Pass Student         *")
print("================================")
for value in lis:
    if value["marks"]>50:
        print(value["name"],"-",value["marks"])
        pass_count+=1
print("PASS",pass_count)

print("================================")
print("*         Fail Student         *")
print("================================")
for value in lis:
    if value["marks"]<50:
        print(value["name"],"-",value["marks"])
        fail_count+=1
print("FAIL",fail_count)
