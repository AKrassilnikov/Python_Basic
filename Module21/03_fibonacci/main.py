
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

number = int(input("Введите порядковый номер числа Фибоначчи: "))
print("Число: ", fib(number + 1))