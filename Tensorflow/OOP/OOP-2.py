##default değerler
class Dog():
    def __init__(self,age=5):
        self.age=age
    def ageOfpeople(self):
        return self.age*7
myDog=Dog(3)#eğer burda değer vermezsek classta tanımlı olan yaş değeri döndürürlür
#print(myDog.age)
print(myDog.ageOfpeople())