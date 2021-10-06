num = int(input("Сколько чисел: "))
num_list = []
rev_list = []
add_list = []
for i in range(num):
    print("Введите", i + 1,"число: ", end = "")
    number = int(input())
    num_list.append(number)
print(num_list)
rev_list = num_list.copy()
rev_list.reverse()
for _ in range(len(rev_list)):
    if num_list == rev_list:
        break
    else:
        add_list.append(num_list[0])
        num_list.remove(num_list[0])
        rev_list.remove(rev_list[-1])
add_list.reverse()
print("Нужно добавить",add_list)



