print("Мой вариант")
number_list = (num for num in range(1000))
count = 0
for num in number_list:
    count += 1
    print(num,end = "\t")
    if count == 20:
        count = 0
        print()

print()
print("Односточный")
number_list_2 = [num for num in range(1000)]
print(number_list_2)