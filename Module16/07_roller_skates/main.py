
def skate_list(n):
    list = []
    for num in range(n):
        print("Размер", num + 1, "пары", end= "")
        number = int(input(": "))
        list.append(number)
    return list

def foot_list(n):
    list = []
    for num in range(n):
        print("Размер ноги ", num + 1, "человека", end= "")
        number = int(input(": "))
        list.append(number)
    return list

skates_num = int(input("Кол-во коньков: "))
skates_list = skate_list(skates_num)
man_num = int(input("Кол-во людей: "))
foots_list = foot_list(man_num)
count = 0

for foot_size in foots_list:
    for skates_size in skates_list:
        if foot_size == skates_size:
            count += 1
            skates_list.remove(foot_size)
            break

print("Наибольшее кол-во людей, которые могут взять ролики: ",count)
