class Hero():
    def __init__(self,name,age,job,specialPower):
        print("Init is called")
        self.name=name
        self.age=age
        self.job=job
        self.specialPower=specialPower
    def method1(self):
        print(f"I am Hero and my Job: {self.job}")

hero=Hero("dark",30,"Press","Invisible")
hero.name="Clark"
#print(hero.name)
#hero.method1()
