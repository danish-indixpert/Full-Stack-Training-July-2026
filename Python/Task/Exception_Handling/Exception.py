try:
    num=int(input("Enter Your Number: "))
    print(num)
except Exception as e:
    with open("error.log",'w') as file:
        file.write(str(e))
