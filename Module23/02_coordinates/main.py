import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return round(y / x, 2)
    except ZeroDivisionError:
        return 0

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return round(y / x, 2)
    except ZeroDivisionError:
        return 0

with open('coordinates.txt', 'r') as file:
    for line in file.readlines():
        nums_list = line.split()
        res1 = f(float(nums_list[0]), float(nums_list[1]))
        res2 = f2(float(nums_list[0]), float(nums_list[1]))
        number = random.randint(0, 100)
        file_2 = open('result.txt', 'w')
        my_list = sorted([str(res1), str(res2), str(number)])
        file_2.write(' '.join(my_list))
        file_2.close()



