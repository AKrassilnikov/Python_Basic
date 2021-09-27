card_number = int(input("Кол-во видеокарт: "))
card_list = []
new_list = []
old_card = 0
for i in range(card_number):
    print(i + 1,"Видеокарта: ", end =" ")
    card = int(input())
    card_list.append(card)
print("\nСтарый список видеокарт: ",card_list)
for max_card in card_list:
    if max_card > old_card:
        old_card = max_card
for card in range(len(card_list)):
    if card_list[card] != old_card:
        new_list.append(card_list[card])
print("Новый список видеокарт:",new_list)


