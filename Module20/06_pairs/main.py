
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("1-й Вариант:")
new_list = []
start = 0
for num in range(len(original_list)//2):
    new_list.append(tuple(original_list[start : start + 2]))
    start += 2
print(new_list)

print()

print("2-й Вариант:")
first_list = [num for num in original_list[0:len(original_list):2]]
second_list = [num for num in original_list[1:len(original_list):2]]
new_list = list(zip(first_list,second_list))
print(new_list)

