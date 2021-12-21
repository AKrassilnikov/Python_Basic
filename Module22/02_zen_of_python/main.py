zen = open("zen.txt",'r')
line = zen.readlines()
for num_line in range(len(line),-1,-1):
    print(line[num_line - 1])
zen.close()








