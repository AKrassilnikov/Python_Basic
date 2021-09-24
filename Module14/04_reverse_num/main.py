def revers_def(number):
    numbers = str(number).split(".")
    first_part = (numbers[0])[::-1]
    second_part = (numbers[1])[::-1]
    number = [first_part,second_part]
    number_rev = float(".".join(number))
    return number_rev

number_N = float(input("Введите число N: "))
number_K = float(input("Введите число K: "))

revers_N = revers_def(number_N)
revers_K = revers_def(number_K)

print("\nПервое число наоборот: ",revers_N)
print("Второе число наоборот: ",revers_K)
print("Сумма: ",revers_N + revers_K)


