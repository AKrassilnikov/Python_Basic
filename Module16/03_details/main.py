shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
count = 0
price = 0
tool = input("Введите имя детали: ")
for d_count in range(len(shop)):
    if shop[d_count][0] == tool:
        count += 1
        price += shop[d_count][1]
print("Кол-во деталей",count)
print("Общая стоимость", price)
