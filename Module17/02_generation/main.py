
import random

number = int(input("Введите число: "))
numlist = [random.randint(1,50) for _ in range(number)]
numlist = [(1 if num % 2 == 0 else num // 5) for num in numlist]
print(numlist)
