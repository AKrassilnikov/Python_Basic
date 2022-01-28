import math

class Auto:

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.__x = x
        self.__y = y

    def moove(self, distance, angle):
        self.distance = distance
        self.__x = round(self.__x + distance * math.cos(math.radians(angle)))
        self.__y = round(self.__y + distance * math.sin(math.radians(angle)))
        print(f'{self.name} переместился в точку: x:{self.__x} y:{self.__y}')

    def __str__(self):
        return f'Автомобиль находится в точке: x:{self.__x} y:{self.__y}.'


class Bus(Auto):

    def __init__(self, name, x=0, y=0, passenger=0 ):
        super().__init__(name, x, y)
        self.__passenger = passenger

    def set_in_passenger(self, quantity):
        if quantity > 0:
            print(f'Зашло {quantity} пассажиров.')
            self.__passenger += quantity
        else:
            raise Exception('Неправильно введено значение')

    def out_passenger(self, quantity):
        if 0 < quantity <= self.__passenger:
            self.__passenger -= quantity
            print(f'Вышло {quantity} пассажиров.')
        else:
            print('Неправильно введено значение')

    def moove(self, distance, angle):
        super().moove(distance, angle)
        money = self.__passenger * 20
        print(f'С пассажиров получено денег: {money}')


taxi = Auto('Автомобиль', 0, 0)
taxi.moove(8, 45)
print()

bus = Bus('Автобус', 5, 0, 0)
bus.set_in_passenger(5)
bus.moove(10, 13)









