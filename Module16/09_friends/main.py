
frends = int(input("Сколько друзей: "))
debt = int(input("Сколько долговых расписок: "))
frend_list = []
for _ in range(frends):
   frend_list.append(0)
print(frend_list)
for cash in range(debt):
    print(cash + 1,"-ая расписка")
    to_whom = int(input("Кому: "))
    from_whom = int(input("От кого: "))
    amount = int(input("Сколько: "))
    if to_whom == from_whom:
       print("Ошибка")
    else:
       frend_list[to_whom - 1] += amount
       frend_list[from_whom - 1] -= amount
    print()
print("\nБаланс друзей:")
for num in range(len(frend_list)):
   print(num+1,":",frend_list[num])























