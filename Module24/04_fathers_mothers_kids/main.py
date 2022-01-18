import random

class Parent:
    def __init__(self,name,age,child):
        self.name = name
        self.age = age
        self.child = child

    def __repr__(self):
        return repr((self.name,self.age,self.child))

    def eat(self,name):
        print("Coock for {}".format(name))
        return False

    def peace(self,name):
        print("Sing a song")
        return True

class Child:
    def __init__(self,name,age,peacfull,hungry):
        self.name = name
        self.age = age
        self.peacfull = peacfull
        self.hungry = hungry

    def __repr__(self):
        return repr((self.name,self.age,self.peacfull,self.hungry))
    def info(self):
       return print("""
Name: {} 
Age: {}
Peacfull: {}
Hungry: {} \n""".format(child_1.name, child_1.age, child_1.peacfull, child_1.hungry))

def hungry():
    list = [True,False]
    child_1.hungry = random.choice(list)
    if child_1.hungry == True:
        child_1.peacfull = False
        print(child_1.name, "Is is hungry and not peacefull")
        child_1.info()
        child_1.hungry = parent_1.eat(child_1.name)
        child_1.peacfull = parent_1.peace(child_1.name)

def peace():
    child_1.peacfull = False
    print(child_1.name, "Is is not peacefull")
    child_1.info()
    child_1.peacfull = parent_1.peace(child_1.name)

child_1 = Child("Bobic",5,True,False)
parent_1 = Parent("Tom",35,child_1)

action = random.choice([hungry,peace])
action()

child_1.info()


