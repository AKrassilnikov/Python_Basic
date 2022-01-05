def leter_count (data):
    leters_count = {}
    text_len = 0
    for leter in data.lower():
        if leter.isalpha():
            text_len += 1
            if not leter in leters_count.keys():
                leters_count[leter] = 1
            else:
                leters_count[leter] += 1
    return leters_count, text_len

text_file = open("text.txt",'w')
text_file.write(input('Input text: '))
text_file = open("text.txt",'r')
count_leter,text_len = leter_count(text_file.read())

leter_part = {}
for key in count_leter.keys():
    leter_part[key] = round((count_leter[key] * 100/text_len)/100,3)
leter_part_list= list(leter_part.items())
leter_part_list.sort(key=lambda val: val[1],reverse=True)

new_sort_list = []
sort_list = []
for len in range(0,len(leter_part_list)):
    try:
        if leter_part_list[len][1] == leter_part_list[len + 1][1]:
            new_sort_list.append(leter_part_list[len])
        elif leter_part_list[len][1] != leter_part_list[len + 1][1]:
            new_sort_list.append(leter_part_list[len])
            new_sort_list.sort(key=lambda val: val[0])
            sort_list.append(new_sort_list)
            new_sort_list = []
    except:
        new_sort_list.append(leter_part_list[len])
        new_sort_list.sort(key=lambda val: val[0])
        sort_list.append(new_sort_list)
        new_sort_list = []

text_file = open("analysis.txt", 'w')
for pare in (sort_list):
    for sub_pare in pare:
        text_file.writelines([sub_pare[0],':',str(sub_pare[1]),'\n'])
text_file.close()



















