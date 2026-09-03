#number ki limit increase karne ke liye present 13 any number.
data="12345678"
print(data.zfill(13))



#name (string) ko capital letter format main karta hai har ek character ko.
data="danish"
print(data.upper())



#name (string ) ko small letter format main karta hai har ek character ko.
data='Danish'
print(data.lower())



#har ka first character capital ho jata hai.
data="this in my learing full stack development"
print(data.title())



#only paragraph ka first character ko capital letter format main karta hai.
data="this is a company indixper"
print(data.capitalize())



#ye (string) value ko center beech main karta hai 
data='student details'
print(data.center(100,"*"))



#casefold her ek letter ke first character ko capital karta hai.
data='this is a country of india'
print(data.casefold())



#count only jo charater doge unn character ko count karke batata ha.
data='my name is danish khan'
print(data.count('a'))



#find ye jo letter (string) hai jo daloge uska number length batata hia.
data='python is great programming language'
print(data.find('programming'))



#isalpha ye only true and false ke decision leta hai only character ko true batayega na ki numbers ko and number ko false batata hai
data='developer'
data0='developer56'
print(data.isalpha())
print(data0.isalpha())




data='developer1to10'
data1='developer 1 to 10'
print(data.isalnum())
print(data1.isalnum())




data="123456"
data12="developer123455"
print(data.isdigit())
print(data12.isdigit())




data=['1','2','3','4','5']
saperator=','
print(saperator.join(data))




data="dog"
print(data.ljust(8))




data='full stach development'
print(data.swapcase())




data='                      developer indixpert'
print(data.lstrip())




data='      this is indixpert a company      '
print(data.strip())