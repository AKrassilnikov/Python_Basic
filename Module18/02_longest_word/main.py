text = input("Ввудите текст: ").split()
max_len = 0
max_ken_word = ""
for string in text:
    if max_len < len(string):
        max_ken_word = string
    elif max_len == len(string):
        pass
print("Самое длинное слово:",max_ken_word, "его id:",text.index(max_ken_word))

