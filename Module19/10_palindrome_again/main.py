
def can_make_pal(text):
    d={}
    for a in text:
        if d.get(a) is None:
            d[a]=1
        else:
            d[a]+=1
    n=len(d)
    e=0
    for a in d.values():
        if a%2==0:
            e+=1
    return e == n or e == n-1

text = input("Введите текст: ")
result = can_make_pal(text)
if result == 0:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")

