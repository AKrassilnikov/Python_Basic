def find_monetka(x,y,r):
    if x<=r and y<=r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')
print("Введите координаты монетки:")
x_m = float(input("X: "))
y_m = float(input("Y: "))
radius = int(input("Введите радиус: "))
find_monetka(x_m,y_m,radius)
