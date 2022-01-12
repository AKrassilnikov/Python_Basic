
def read_lines(line):
    bad_log = open('registrations_bad.txt', 'a', encoding='utf-8')
    good_log = open('registrations_good.txt', 'a', encoding='utf-8')
    list_line = line.split()
    if len(list_line) < 3:
        bad_log.write(str(line)[:-1] + ' IndexError\n')
    elif not list_line[2].isdigit() or 10 > int(list_line[2]) or int(list_line[2]) > 99:
        bad_log.write(str(line)[:-1] + ' ValueError\n')
    elif not list_line[0].isalpha():
        bad_log.write(str(line)[:-1] + ' NameError\n')
    elif not "@" in list_line[1] or not '.' in list_line[1]:
        bad_log.write(str(line)[:-1] + ' SyntaxError\n')
    else:
        good_log.write(line)
    bad_log.close()
    good_log.close()
registrations = open('registrations.txt','r',encoding='utf-8')
for line in registrations.readlines():
    read_lines(line)
