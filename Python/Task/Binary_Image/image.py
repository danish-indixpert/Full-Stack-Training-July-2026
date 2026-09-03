with open("newimage.jpeg","rb") as file:
    data=file.read()
    print(data)

with open("image.jpg","wb") as fileone:
    dataone=fileone.write(data)
    print(dataone)
    