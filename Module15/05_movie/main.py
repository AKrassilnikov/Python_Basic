
films = ['Крепкий орешек','Назад в будущее','Таксист','Леон','Богемская рапсодия','Город грехов','Мементо','Отступники','Деревня']
my_films = []
flag = False
while True:
    print("Какой фильм: ",end = " ")
    my_film = input()
    if my_film == "end":
        break
    for film in films:
        if my_film == film:
            flag = True
    if flag == True:
        my_films.append(my_film)
    else:
        print("Фильма в списке нет")
    flag = False
print("Мой список: ", my_films)

