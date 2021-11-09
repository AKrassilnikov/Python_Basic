from random import randint

def def_num_secret(max_number):
    sec = set([(randint(1,max_number)) for _ in range(3)])
    if len(sec) < 3:
        sec = def_num_secret(max_number)
    return sec
max_number = int(input("Введите максимальное число: "))
while True:
    secret_number = def_num_secret(max_number)
    num_list = input("Введите 5 чисел через пробел: ")
    if num_list == "Помогите!":
        print("Артём мог загадать следующие числа:",secret_number)
        break
    else:
        num_list = num_list.split()
    for num in num_list:
        if int(num) in secret_number:
            print("Ответ от Артёма: Да")
            break
    else:
        print("Ответ от Артёма: Нет")



