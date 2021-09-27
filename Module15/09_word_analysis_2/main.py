word = list(input("Введите слово: "))
word_reverse = word.copy()
word_reverse.reverse()
if word == word_reverse:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

