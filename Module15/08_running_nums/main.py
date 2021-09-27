
import time

list_N = []
numbers = int(input("Колл-во номеров: "))
number_K = int(input("Сдвиг: "))
for i in range(numbers):
    print(i + 1,"- е число: ", end = " ")
    number = int(input())
    list_N.append(number)
print("\nИзначальный список:",list_N)
while True:
    for change in range(number_K):
        list_N.insert(len(list_N),list_N[0])
        list_N.remove(list_N[0])
    print("Сдвинутый список:",list_N)
    time.sleep(0.25)

