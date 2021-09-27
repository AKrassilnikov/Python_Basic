old_list = []
numbers = int(input("Колл-во номеров: "))
for i in range(numbers):
    print(i + 1,"- е число: ", end = " ")
    number = int(input())
    old_list.append(number)
print("Изначальный список:", old_list)
old_list.sort()
print("Отсортированный список:",old_list)
