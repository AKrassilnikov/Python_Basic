import os

def def_lines(line):
    new_dict = {}
    for line in line.readlines():
        line_list = line.split()
        if len(line_list) < 3:
            pass
        else:
            new_dict[line_list[1][0]+'.'+ line_list[0]] = line_list[2]
    return new_dict

first_tour_file = open(os.path.abspath('first_tour.txt'))
list_score = def_lines(first_tour_file)
first_tour_file.close()
second_list = list(list_score.items())
second_list.sort(key=lambda value: value[1],reverse=True)
print(second_list)
second_tour = open("second_tour.txt",'w')
n = 0
for pare in range(2,len(second_list)):
    second_tour.writelines([str(second_list[n][0]),': ',str(second_list[n][1]),'\n'])
    n += 1
second_tour.close()



