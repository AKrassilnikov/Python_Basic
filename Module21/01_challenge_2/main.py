def num_def(number):  # оздание списка от 1 до n c помощью рекурсии
    if number == 1:
        return list_num.append(number)
    else:
        num_def(number - 1)  # передаём значение number
        return list_num.append(number)

number = int(input("Input number: "))
list_num = []
num_def(number)
print(list_num)
