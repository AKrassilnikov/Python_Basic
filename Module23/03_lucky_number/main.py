import random

errors = [ArithmeticError, AssertionError, AttributeError]
result = 0
f = open('nums.txt', 'w')

with f as file:
    while result <= 777:
        number = int(input('Input number: '))
        result += number
        if random.choices((0, 1), (1-1/13, 1/13))[0]:
            raise random.choice(errors)
        print(number, file=file)