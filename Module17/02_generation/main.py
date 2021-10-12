
number = int(input("Введите длину списка: "))
numlist = list(range(number))
numlist = [(num % 5 if num % 2 != 0 else 1) for num in numlist]
print("Результат:",numlist)
