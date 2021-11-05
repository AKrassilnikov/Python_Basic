import sys
number = int(input("Введите количество пар слов: "))
words_sin = dict()
for num in range(number):
    words_sin[num] = [input("{} пара: ".format(num + 1)).split(" - ")]
print(words_sin)
id_sin = 0
while True:
    word_new = input("Введите слово: ")
    for key in words_sin.keys():
        for word in words_sin[key]:
            if word_new in word:
                id_word = word.index(word_new)
                if id_word == 0:
                    id_sin = 1
                print("Синоним:", word[id_sin])
                sys.exit()
    else:
        print("Такого слова в словаре нет.")




