class Addition:
    def first(self, a , b):
        print("Add",a+b)

class Subtraction(Addition):
    def second(self, a,b):
        print("Subtraction", a-b)

class Multipllication(Subtraction):
    def three(self, a,b):
        print("Three",a*b)
obj=Multipllication()
obj.first(4,2)
obj.second(4,6)
obj.three(7,9)