print("Мой вариант")
number_list = (number for number in range(1000))
count = 0
for number in number_list:
    count += 1
    print(number,end = "\t")
    if count == 20:
        count = 0
        print()

print()
print("Односточный")
number_list_2 = [number for number in range(1000)]
print(number_list_2)