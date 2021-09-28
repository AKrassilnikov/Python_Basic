
core_number = int(input("Введите кол-во клеток: "))
core_list = []
bad_list = []
for i in range(core_number):
    print("Введите эффективность", i + 1,"клетки: ", end =" ")
    effect = int(input())
    core_list.append(effect)
for e_core in range(len(core_list)):
    if core_list[e_core] <= e_core:
        bad_list.append(core_list[e_core])
print("\nНеподходящие значения: ", bad_list)
