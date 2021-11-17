
def can_make_pal(text):
    dict_pal = {}
    for a in text:
        dict_pal[a] = dict_pal.get(a,0) + 1
    count =0
    for a in dict_pal.values():
        if a %2 != 0:
            count += 1
    return count <= 1

text = input("Введите текст: ")
if can_make_pal(text):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")

