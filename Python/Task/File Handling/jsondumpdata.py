import json

filedata=[
    {
    "name":'danish',
    "address":'dholpur'
}
]
with open("data.json",'w')as file:
    data=json.dump(filedata,file,indent=4)
    print(data)
