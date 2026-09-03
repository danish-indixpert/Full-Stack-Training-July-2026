try:
    withdrawal=int(input("Enter Your withdrawal Money: "))

except Exception as file:
    print("Infuccient Balance")
    print(file)
finally:
    print("thank you user ! please try again")