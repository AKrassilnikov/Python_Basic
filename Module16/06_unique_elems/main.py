
def list_input(n):
    list = []
    for num in range(n):
        print("Введите", num + 1, "число", end= "")
        number = int(input(": "))
        list.append(number)
    return list

a_num = 3
b_num = 7
first_list = list_input(a_num)
print()
second_list = list_input(b_num)
print("\nПервый список:",first_list)
print("Второй список:",second_list)
first_list.extend(second_list)
first_list = list(set(first_list))
print("Новый первый список с уникальными элементами: ",first_list)



















