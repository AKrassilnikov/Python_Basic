
def def_data(data):
    return [index for index, number in enumerate(data)]

def def_data_for_dict(data):
    return [index for index, number in data.items()]

def def_num(id_list,data):
    k = 0
    numList = []
    for x in id_list:
       for i in range(2, x // 2+1):
           if x % i == 0:
               k += 1
       if k == 0:
           numList.append(data[x])
       else:
           k = 0
    return numList

data = input('Введите текст: ').split()
id_list = def_data(data)
num_list = def_num(id_list,data)

print(num_list)




