
def def_data(data):
    return [index for index, number in enumerate(data) if is_prime(index)]

def is_prime(index):
    k = 0
    if index < 2:
        return False
    else:
        for i in range(2, index // 2+1):
            if index % i == 0:
                k += 1
        if k <= 0:
            return True
        else:
             return False

data = input('Введите текст: ').split()
id_list = def_data(data)
new_list = [data[sumb] for sumb in id_list]
print(new_list)





