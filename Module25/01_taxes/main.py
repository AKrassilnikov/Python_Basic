class Property:
    def __init__(self,worth,cash):
        self.worth = worth
        self.cash = cash

    def __str__(self):
        return "Cost: {}".format(self.worth)

class Apartament(Property):
    def __init__(self,worth,cash):
        super().__init__(worth,cash)

    def get_taxes(self):
        print("For Apartametnts taxes is 1/1000 of worth")
        print("Taxes is:", self.worth//1000)
        print("Can by:", self.cash >= self.worth,"\n")

class Car(Property):
    def __init__(self,worth,cash):
        super().__init__(worth,cash)

    def get_taxes(self):
        print("For Car taxes is 1/200 of worth")
        print("Taxes is:", self.worth//200)
        print("Can by:", self.cash >= self.worth,"\n")

class CountryHouse(Property):
    def __init__(self, worth, cash):
        super().__init__(worth, cash)

    def get_taxes(self):
        print("For CountryHouse taxes is 1/500 of worth")
        print("Taxes is:", self.worth // 500)
        print("Can by:", self.cash >= self.worth,"\n")

cash = int(input("How many cash you have?: "))
w_home = int(input("Cost of Apartament: "))
w_car = int(input("Cost of car: "))
w_dacha = int(input("Cost of CountryHouse: "))


home = Apartament(worth=w_home,cash=cash)
car = Car(worth=w_car,cash=cash)
dacha = CountryHouse(worth=w_dacha,cash=cash)
print()
car.get_taxes()
home.get_taxes()
dacha.get_taxes()











