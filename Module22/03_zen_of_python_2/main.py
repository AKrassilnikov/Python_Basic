import os

def min_leter(data):
    leters_count = {}

    for leter in data.lower():
        if leter.isalpha():
            if not leter in leters_count.keys():
                leters_count[leter] = 1
            else:
                leters_count[leter] += 1
    return leters_count

zen_file = open(os.path.abspath('zen.txt'),'r')
line_count = len(zen_file.readlines()) #lines number
zen_file.close()
zen_file = open(os.path.abspath('zen.txt'),'r')
len_lines = []
line_words_count = []
for line in zen_file:
    line_words_count.append(len(line.split())) # words count
    len_lines.append(len(line)) # leters number
zen_file.close()
zen_file = open(os.path.abspath('zen.txt'),'r')
min_count_leter = min_leter(zen_file.read()) # each leter count
zen_file.close()
print('Количество букв в файле: ',sum(len_lines))
print('Количество слов в файле: ',sum(line_words_count))
print('Количество строк в файле:',line_count)
print('Наиболее редкая буква:',list(min_count_leter.keys())[list(min_count_leter.values()).index(sorted(min_count_leter.values())[0])],":", sorted(min_count_leter.values())[0])




