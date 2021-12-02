def calculating_math_func(data):
    if data == 1:
        return 1
    factorial_nim_1 = calculating_math_func(data - 1)
    factorial = data * factorial_nim_1
    return factorial

number = int(input("Input number: "))
data = calculating_math_func(number)
data /= number ** 3
data = data ** 10
print("Result :",data)