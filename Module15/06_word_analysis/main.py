

word = input("Введите слово: ")
count_list = []
count = 0
for sumbol in word:
    count_list.append(0)
for same_sumb in range(len(word)):
    for each_sumb in word:
        if word[same_sumb] == each_sumb:
            count_list[same_sumb] += 1
for eniqu_sumb in count_list:
    if eniqu_sumb == 1:
        count += 1
print("Кол-во уникальных букв:", count)
