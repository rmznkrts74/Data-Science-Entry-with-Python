class Apple():
    def __init__(self,name):
        self.name=name
    def give_info(self):
        return self.name + " 100 calori"
class Banana():
    def __init__(self, name):
        self.name = name

    def give_info(self):
        return self.name + " 150 calori"
elma=Apple("Elma")
#print(elma.give_info())
muz=Banana("Muz")
#print(muz.give_info())
list1=[elma,muz]
for i in list1:
    print(i.give_info())
def get_info(fruit):
    print(fruit.give_info())
get_info(elma)
get_info(muz)