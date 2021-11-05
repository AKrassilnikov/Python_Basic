def country_city_def(country_city_list):
    list_new = dict()
    list_new[country_city_list[0]] = country_city_list[1:]
    return list_new

number = int(input("Какое колл-во стран: "))
countrys = ["{}-я страна".format(country + 1) for country in range(number)]
citys_disct = dict()
for id_country in range(number):
    print(countrys[id_country],": ", end="")
    country_city_list = input().split()
    country_city = country_city_def(country_city_list)
    citys_disct[id_country + 1] = country_city

print(citys_disct)
city = ""
for search in range(3):
    city = input("{} город: ".format(search + 1))
    flag = False
    for id_num in range(1,number + 1):
        for id_city in citys_disct[id_num].values():
            if city in id_city:
                print("Город",city,"расположен в стране",list(citys_disct[id_num].keys())[0])
                flag = True
    if flag == True:
        pass
    else:
        print("По городу",city,"данных нет.")


