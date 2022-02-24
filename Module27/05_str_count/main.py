import random

def counter(function):
    return function

@counter
def count():
    return 1

number = 0

for _ in range(random.randint(0,100)):
    num = count()
    number += num

print("Function was called:", number,"times")