import random

def def_number():
    return random.randint(1, 7)

errors = ["KillError", "DrunkError", "CarCrashError","GluttonyError","DepressionError"]
result = 0
with open("karma.log.txt","a") as file:
    while result <= 500:
        result += def_number()
        try:
            if random.choices((0, 1), (1 - 1 / 10, 1 / 10))[0]:  #расчёт вероятности 1 к 10
                file.write(random.choice(errors) + "\n")
        except:
            continue
        print(result)











