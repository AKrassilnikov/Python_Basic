from sys import exit
ip_addres = input("Введите IP адрес: ").split(".")
if len(ip_addres) != 4:
    print("Адрес - это четыре числа, разделённые точками")
    exit()
for octet in ip_addres:
    if octet.isdigit() == False:
        print(octet," - не целое число")
        exit()
    elif int(octet) > 255:
        print(octet," - превышает 255")
        exit()
    else:
        continue
print("IP-адрес корректен")

