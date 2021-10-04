num = int(input("Сколько чисел: "))
num_list = []
rev_list = []
for i in range(num):
    print("Введите", i + 1,"число: ", end = "")
    number = int(input())
    num_list.append(number)
print(num_list)
rev_list = num_list.copy()
rev_list.reverse()
rev_list.remove(rev_list[0])
for _ in range(len(rev_list)):
    if rev_list[0] == num_list[len(num_list) - 1]:
        rev_list.remove(rev_list[0])
print(rev_list)
print("Необходимо добавить: ",rev_list)


