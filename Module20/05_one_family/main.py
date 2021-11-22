family ={"Сидоров":{"Сидоров Никита": 35, "Сидорова Аня": 22, "Сидоров Костя": 12 }}
surname = input("Введите фамилию: ").title()
for main, seconds in family.items():
    if main == surname:
        for name, age in seconds.items():
            print(name,age)

