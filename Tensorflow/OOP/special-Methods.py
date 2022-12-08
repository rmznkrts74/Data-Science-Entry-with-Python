class Fruits():
    def __init__(self,name,calori):
        self.name=name
        self.calori=calori
    def __str__(self):#print(muz)gibi yazabiliri
        return f"{self.name} is {self.calori} calori"
    def __len__(self):
        return self.calori
muz=Fruits("Muz",200)
#print(muz.calori)
print(muz)
print(len(muz))