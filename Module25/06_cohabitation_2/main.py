import random

class House:
    money = 100
    food = 50
    cat_food = 30
    dirt = 0
    coat = 0

class Man:
    fullness = 30
    happy = 100

    def __init__(self,name):
        self.name = name

    def work(self):
        House.money += 150
        self.happy -= 10
        self.fullness -= 10
        print(self.name, "Go to work")

    def play(self):
        self.happy += 20
        self.fullness -= 10
        print(self.name, "Played on PC")

    def eat(self):
        food = 20
        self.fullness += food
        House.food -= food
        print(self.name, "Go to eat")


    def play_with_cat(self):
        self.happy += 5
        self.fullness -= 10
        print(self.name, "Played with cat")

class Woman:
    fullness = 30
    happy = 100

    def __init__(self,name):
        self.name = name

    def eat(self):
        food = 20
        self.fullness += food
        House.food -= food
        print(self.name, "Go to eat")

    def buy_food(self):
        cash = 50
        House.food += cash
        House.money -= cash
        self.fullness -= 10
        self.happy -= 10
        print(self.name, "Go to market")

    def buy_cat_food(self):
        cash  = 30
        House.cat_food += cash
        House.money -= cash
        self.fullness -= 10
        print(self.name, "Go to animals market")

    def clean(self):
        House.dirt -= 70
        self.fullness -= 10
        self.happy -= 10
        print(self.name, "Clean house")

    def buy_coat(self):
        self.happy += 60
        House.money -= 350
        self.fullness -= 10
        House.coat += 1
        print(self.name, "Bot coat")

    def play_with_cat(self):
        self.happy += 5
        self.fullness -= 10
        print(self.name, "Played with cat")

class Cat:
    fullness = 30

    def __init__(self,name):
        self.name = name

    def eat(self):
        food = 10
        self.fullness += food * 2
        House.cat_food -= food
        print(self.name, "Go to eat")

    def play(self):
        House.dirt += 5
        print(self.name,"Played with walls")

def man_day():
    if man.fullness == 10:
        man.eat()
    elif man.happy <= 30:
        man.play()
    else:
        man.work()
    print("Food: {}, Happy: {}\n".format(man.fullness,man.happy))

def wife_day():
    if wife.fullness == 10:
        wife.eat()
    elif wife.happy <= 30:
        wife.buy_coat()
    elif House.dirt >= 70:
        wife.clean()
    elif House.cat_food <= 10:
        wife.buy_cat_food()
    else:
        wife.buy_food()
    print("Food: {}, Happy: {}\n".format(wife.fullness,wife.happy))

def cat_day():
    if cat.fullness == 10:
        cat.eat()
    else:
        cat.fullness -= 10
        print("Cat's day")
    print("Food: {}\n".format(cat.fullness))

man = Man("Bob")
wife = Woman("Ellise")
cat = Cat("Tom")

for day in range(1,366):
    print("{}'th day \n".format(day))
    if random.choice([True,False]):
        cat.play()
    if man.fullness < 0 or wife.fullness < 0 or cat.fullness < 0:
        print("Game over, person is Hungry")
        break
    if man.happy < 10 or wife.happy < 10:
        print("Game over, person is not Happy")
        break
    man_day()
    wife_day()
    cat_day()
    House.dirt += 5
    if House.dirt > 90:
        House.dirt += 5

    print("Money: {}, Food: {},Cats food: {}, Dirt: {},Coat {}\n"
          .format(House.money,House.food,House.cat_food,House.dirt,House.coat))







