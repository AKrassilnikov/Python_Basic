import os
file_num = open(os.path.abspath('numbers.txt'),'r')
num_list = file_num.read()
print('Содержимое файла numbers.txt: \n',num_list)
num2_list = []
for num in num_list:
    if num == "2":
        num2_list.append(int(num))
file_num.close()
file_num_answer = open(os.path.abspath('answer.txt'),'w')
file_num_answer.write(str(sum(num2_list)))
file_num.close()
file_num_answer = open(os.path.abspath('answer.txt'),'r')
file_num_answer_read = file_num_answer.read()
print('Содержимое файла answer.txt:\n',file_num_answer_read)


