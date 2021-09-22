def revers_def(number):
    numbers = str(number).split(".")
    first_part = (numbers[0])[::-1]
    second_part = (numbers[1])[::-1]
    number = [first_part,second_part]
    number_rev = ".".join(number)
    return number_rev,first_part,second_part

def summ_all(first_part_N,second_part_N,first_part_K,second_part_K):
    summ_first_part = str(int(first_part_N) + int(first_part_K))
    summ_second_part = str(int(second_part_N) + int(second_part_K))
    summ_num = [summ_first_part, summ_second_part]
    summ_num_all = ".".join(summ_num)
    return summ_num_all

number_N = float(input("Введите число N: "))
number_K = float(input("Введите число K: "))

revers_N,first_part_N,second_part_N = revers_def(number_N)
revers_K,first_part_K,second_part_K = revers_def(number_K)
summ_num_all = summ_all(first_part_N,second_part_N,first_part_K,second_part_K)

print("\nПервое число наоборот: ",revers_N)
print("Второе число наоборот: ",revers_K)
print("Сумма: ",float(summ_num_all))


