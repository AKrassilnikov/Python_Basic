gamers = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list= []
for index in range(len(gamers)):
    if index % 2 == 0:
        new_list.append(gamers[index])
print(new_list)
