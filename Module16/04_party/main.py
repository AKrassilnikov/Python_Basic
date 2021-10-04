
guests = ['Петя','Ваня','Саша','Лиза','Катя']
while True:
    action = input("Гость пришёл или ушёл?: ")
    if action == 'пришёл':
        name = input("Ведите имя: ")
        if len(guests) == 6:
            print("Прости,",name,'но мест нет')
        else:
            guests.append(name)
            print("Привет", name)
    elif action == 'ушёл':
        name = input("Ведите имя: ")
        guests.remove(name)
        print("Пока", name)
    elif action == 'Пора спать':
        break
    print()
    print("Сейчас на вечеринке 5 человек: ",guests)
print("\nВечеринка закончилась, все легли спать.")