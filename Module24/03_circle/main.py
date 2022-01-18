import math

class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        return math.sqrt(self.r) * math.pi

    def get_perimeter(self):
        return 2 * self.r * math.pi

    def scale(self, k):
        self.r *= k

    def is_intersect(self, x2,y2,r2):
        return (self.x - x2) ** 2 + (self.y - y2) ** 2 <= (self.r + r2) ** 2

new_circle = Circle(0,0,1)
print("Площадь круга: ",round(new_circle.get_area(),2))
print("Периметр круга: ", round(new_circle.get_perimeter(),2))
n = int(input("Во сколько увеличиваем?: "))
new_circle.scale(n)
print("Площадь круга: ",round(new_circle.get_area(),2))
print("Периметр круга: ", round(new_circle.get_perimeter(),2))
print("Пересечение кругов: ",new_circle.is_intersect(10,10,3))
