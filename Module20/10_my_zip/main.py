list_1 = list(input("Введите буквы: "))
list_2 = tuple(input("Введите числа: "))
list_3 = zip(list_1,list_2)
print(num for num in list_3)
for pare in zip(list_1,list_2):
    print(pare)

print("\nВторой вариант")
list_4 = []
for id in range(0,len(list_1)):
    list_4.append(tuple(list_1[id] + list_2[id]))
for pare in list_4:
    print(pare)
