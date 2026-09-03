from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("hoo hoo hooo hooo")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj=Dog()
obj.sound()