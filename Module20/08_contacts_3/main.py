phone_dict = {}
def include_number():
    name = input("Input name and surename: ").split()
    phone_dict[tuple(name)] = int(input("Input number: "))
    print(phone_dict)

def finde_number():
    s_name = input("Enter name: ")
    for name,number in phone_dict.items():
        if s_name in name:
            print(name[1],number)
while True:
    choose = input("Если хотите добавить номер - 1, если найти - 2, выйти - 3: ")
    if choose == "1":
        include_number()
    elif choose == "2":
        finde_number()
    else:
        print("Выход")
        break

