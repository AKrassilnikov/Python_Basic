import math

class Mymath:
    """ Класс математический вычеслений """

    @classmethod
    def circle_length(cls,number) -> float:
        """ Длина окружности d = 2r"""
        diametr = number * 2
        return math.pi * diametr

    @classmethod
    def circle_are(cls,number) -> float:
        """ Площадь окружности S = пr2 """
        return math.pi * number ** 2

    @classmethod
    def qube_area(cls,number) -> float:
        """ Площадь куба V = S3 """
        s = number * math.sqrt(2)
        return s ** 3

    @classmethod
    def sphere_area(cls,number) -> float:
        """Пощадь сферы S = 4пr2 """
        return 4 * math.pi * number ** 2

