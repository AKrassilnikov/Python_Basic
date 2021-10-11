
def alphavit_leter(id):
    leter_list = ""
    for leter in range(len(alphavit)):
        if alphavit[leter] == text[id] and leter + step <= len(alphavit):
            leter_list += alphavit[leter + step]
        elif alphavit[leter] == text[id] and leter + step > len(alphavit):
            leter_list += alphavit[0 + (step - (len(alphavit) - leter))]
    return "".join(leter_list)

alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = list(input("Введите текст: "))
step = int(input("Шаг: "))
crypto_text = [alphavit_leter(id) for id in range(len(text))]
print("Зашифрованное сообщение: ",''.join(crypto_text))

