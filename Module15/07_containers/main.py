
containers_list = []
number_of_containers = int(input("Колл-во контейнеров: "))
for i in range(number_of_containers):
    print("Вес",i + 1,"-го контейнера. не более 200 кг.: ", end = " ")
    weigh = int(input())
    if 0 < weigh <= 200:
        containers_list.append(weigh)
    else:
        print("Ошиба ввода")
containers_list.sort(reverse=True)
new_conteiner = int(input("Введите вес нового контейнера: "))
for weigh_conteiners in range(len(containers_list)):
    if containers_list[weigh_conteiners] > new_conteiner and containers_list[weigh_conteiners + 1] < new_conteiner or containers_list[weigh_conteiners] == new_conteiner:
        containers_list.insert(weigh_conteiners + 1,new_conteiner)
        break
    elif containers_list[weigh_conteiners] < new_conteiner:
        containers_list.insert(0, new_conteiner)
        break
print("Позиция нового контейнера: ",containers_list.index(new_conteiner) + 1)




