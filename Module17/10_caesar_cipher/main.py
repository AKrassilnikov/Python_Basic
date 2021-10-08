
def alphavit_leter(id):
    leter = [alphavit[leter + step] for leter in range(len(alphavit)) if alphavit[leter] == text[id]]
    return "".join(leter)

alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = list(input("Введите текст: "))
step = int(input("Шаг: "))
crypto_text = [alphavit_leter(id) for id in range(len(text))]
print("Зашифрованное сообщение: ",''.join(crypto_text))

