class Mammal:
    def walk(self):
        print("walk mammal")

class Dog(Mammal):
    def bakr(self):
       print("bark")
    
    def walk(self):
        print("walk dog")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bakr()

# cat = Cat()
# cat.walk()
