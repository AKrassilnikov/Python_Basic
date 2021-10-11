import random
def random_num():
    random_list = [random.randint(1,number) for _ in range(2)]
    if random_list[0] > random_list[1]:
        random_list = random_list[::-1]
    return random_list

number = int(input("Сколько палочек: "))
rocks = int(input("Сколько камней: "))
stick_list = ['!' for _ in range(number)]
for rock in range(rocks):
    random_list = random_num()
    for num in range(random_list[0],random_list[1] + 1):
        stick_list[num - 1] = "."
    print(rock + 1,"бросок: ","".join(stick_list))
print("Итого выбито","".join(stick_list))
