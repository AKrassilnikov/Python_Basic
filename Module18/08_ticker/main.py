from sys import exit
first_string = "abcd"
second_string = "cdba"
first_list = list(first_string)
count = 0
while True:
    if count > len(first_list):
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
        exit()
    first_list.append(first_list[0])
    first_list.remove(first_list[0])
    count += 1
    if "".join(first_list) == second_string:
        break
print("Первая строка получается из второй со сдвигом",count)




