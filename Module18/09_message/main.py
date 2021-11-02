def rev_string(string,symbols_list):
    for symb in symbols_list:
        if symb in list(string):
            sep_list = string.split(symb)
            sep_rev_list = [rev_str[::-1] for rev_str in sep_list]
            return symb.join(sep_rev_list)

symbols_list = list("!,.:;@#&?")
text = input("Введите текст: ")
text_list = text.split()
new_List = []
for string in text_list:
    if string.isalnum() == False:
        rev_list = rev_string(string,symbols_list)
        new_List.append(rev_list)
    else:
        new_List.append(string[::-1])

print(" ".join(new_List))


