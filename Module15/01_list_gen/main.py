number = int(input("Введите число: "))
num_list = []
for num in range(1,number + 1):
    if num % 2 != 0:
        num_list.append(num)
print("Список нечётных",num_list)
