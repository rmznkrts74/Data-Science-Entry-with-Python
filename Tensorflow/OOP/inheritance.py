##inheritance
class Animal():
    def __init__(self):
        print("Animal class")
    def method1(self):
        print("Method 1")
    def method2(self):
        print("method 2")
"""myAnimal=Animal()
myAnimal.method2()
myAnimal.method1()
"""
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat is called")
    def speak(self):
        print("Speak")
myCat=Cat()
myCat.method1()
myCat.method2()
myCat.speak()