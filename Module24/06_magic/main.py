class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            None

class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            None

class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Dirt):
            return Brick()
        else:
            None

class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        else:
            None

class Storm:
    def __str__(self):
        return 'Шторм'

class Vapor:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Brick()
        else:
            None

class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Glass()
        else:
            None

class Lava:
    def __str__(self):
        return 'Лава'

class Brick:
    def __str__(self):
        return 'Кирпич'

class Glass:
    def __str__(self):
        return 'Стекло'

    def __add__(self, other):
        if isinstance(other, Lightning):
            return LightBulb()
        else:
            None

class LightBulb:
    def __str__(self):
        return 'Лампочка'

def main():
    water = Water()
    air = Air()
    earth = Earth()
    fire = Fire()

    print(f'Я колдую ... \n')
    print(f'Получаю: { water + earth } ')
    print(f'Я колдую ... \n')
    print(f'Получаю: { water + earth + fire} ')
    print(f'\nЯ колдую ... \n')
    print(f'Получаю: { air + earth + fire } ')
    print(f'\nЯ колдую ... \n')
    print(f'Получаю: { (air + earth + fire) + (fire + air) } ')

main()

