a_list = [1, 5, 3]
b_list = [1, 5, 1, 5]
c_list = [1, 3, 1, 5, 3, 3]
count_5 = 0
a_list.extend(b_list)
for five in a_list:
    if five == 5:
        count_5 += 1
        a_list.remove(5)
a_list.extend(c_list)
count_3 = a_list.count(3)
print("Результат работы программы:")
print("Кол-во цифр 5 при первом объединении: ",count_5)
print("Кол-во цифр 3 при втором объединении:  ",count_3)
print("Итоговый список: ", a_list)