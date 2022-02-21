import math


class Qube:
    def __init__(self) -> None:
        self.side = 0

    @property
    def calculation(self) -> str:
        """ Геттер, расчёт периметра и площади куба и возвразщает значения"""
        qube_volume = self.side ** 3
        qube_are = 6 * self.side ** 2
        return f'Qube Volume: {qube_volume}, Qube area: {qube_are}'

    @calculation.setter
    def calculation(self,size: int or float) -> None:
        """ Сеттер, принимает ширину ребра """
        self.side = size


class Triangle:
    def __init__(self) -> None:
        self.size = 0
        self.high = 0

    @property
    def triangle(self) -> str:
        """ Геттер, расчёт площади пирамиды """
        high = math.sqrt(self.high ** 2 - (self.size//2) ** 2)
        area = 4*(0.5 * self.size * high) + self.size ** 2
        volume = ((self.size*2) * high)//3
        return f'Triangle volume: {volume}, Triangle area: {area}'

    @triangle.setter
    def triangle(self,a_list:list) -> None:
        """ Сеттер, принимает высоту ребра и ширину одной стороны основания """
        a = iter(a_list)
        self.size = next(a)
        self.high = next(a)

qube_1 = Qube()
qube_1.calculation = 4
print(qube_1.calculation)

triangle_1 = Triangle()
triangle_1.triangle = [10,13]
print(triangle_1.triangle)
















