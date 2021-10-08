
text = list(input("Введите текст: "))
g_lettes = ['а','у','о','ы','и','э','я','ю','ё','е']
new_list = [text[leter] for leter in range(len(text)) for num in g_lettes if text[leter] == num]
print(new_list)

