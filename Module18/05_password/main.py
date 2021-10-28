
while True:
    password = input("Введите пароль: ")
    digit_count = 0
    up_count = 0
    if len(password) < 8:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
        continue
    for symbol in password:
        if symbol.isupper():
            up_count += 1
        elif symbol.isdigit():
            digit_count += 1
    if digit_count < 3 or up_count == 0:
        print("Пароль ненадёжный. Попробуйте ещё раз.")
        continue
    else:
        break
print("Это надёжный пароль!")



