def person_order(order):
    list_new = dict()
    list_new[order[1]] = int(order[2])
    return list_new

number = int(input('Введите кол-во заказов: '))
order_dict = dict()
for num in range(number):
    order = input("{} заказ: ".format(num + 1)).split()
    person = person_order(order)
    if order[0] in order_dict.keys():
        if order[1] in order_dict[order[0]].keys():
            order_dict[order[0]][order[1]] += person[order[1]]
        else:
            order_dict[order[0]].update(person)
    else:
        order_dict[order[0]] = person
for key in sorted(order_dict.keys()):
    print("{}:".format(key))
    for value in sorted(order_dict[key].keys()):
         print(" {}: ".format(value),order_dict[key][value])




