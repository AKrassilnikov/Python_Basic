
symbols_list = list("!,.:;@#&?")
print(symbols_list)
text = input("Введите текст: ")
text_list = text.split()
print(text_list)
new_List = []
for string in text_list:
    if string.isalnum() == False:
            rev = list(string[::-1])
            rev.append(rev[0])
            rev.remove(rev[0])
            new_List.append("".join(rev))
    else:
        new_List.append(string[::-1])

print(" ".join(new_List))

