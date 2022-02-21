import math

class Mymath:
    """ Класс математический вычеслений """

    def __init__(self,number : int) -> None:
        """ Функция принимающая параметр фигуры
        :param number:
        """
        self.number = number

    def circle_length(self) -> float:
        """ Длина окружности d = 2r"""
        diametr = self.number * 2
        return math.pi * diametr

    def circle_are(self) -> float:
        """ Площадь окружности S = пr2"""
        return math.pi * self.number ** 2

    def qube_area(self) -> float:
        """ Площадь куба V = S3 """
        s = self.number * math.sqrt(2)
        return s ** 3

    def sphere_area(self):
        """Пощадь сферы S = 4пr2 """
        return 4 * math.pi * self.number ** 2

