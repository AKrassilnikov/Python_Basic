goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
summ_price = 0
summ_qa = 0
for keys in goods.keys():
    value = goods.get(keys)
    for num in range(len(store[value])):
        summ_qa += store[value][num]['quantity']
        price_all = store[value][num]['quantity'] * store[value][num]["price"]
        summ_price += price_all
    print(keys, ":","колл-во -",summ_qa,'цена',summ_price)
    summ_price = 0
    summ_qa = 0


