def min_dev_def(number):
    dev_list = []
    for dev in range(2, number + 2):
        if number % dev == 0:
            dev_list.append(dev)
    min_dev = dev_list[0]
    for min in dev_list:
        if min_dev > min:
            min_dev = min
    return min_dev

number = int(input("Введите число: "))
min_dev = min_dev_def(number)
print("Наименьший делитель, отличный от единицы:",min_dev)