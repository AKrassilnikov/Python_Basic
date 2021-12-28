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
text_file = open("analysis.txt", 'w')
for pare in list(leter_part.items()):
    text_file.writelines([pare[0],':',str(pare[1]),'\n'])
text_file.close()


