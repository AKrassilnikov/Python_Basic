
def numbers_summ_def(number):
    summ = 0
    num_len = len(str(number))
    for num in range (num_len):
        a = number % 10
        summ += a
        number = number // 10
    return summ

def number_count_def(number):
    num_len = len(str(number))
    return num_len


number = int(input("Введите целое положительное число: "))
numbers_summ = numbers_summ_def(number)
number_count = number_count_def(number)
print("Сумма цифр: ",numbers_summ)
print("Кол-во цифр в числе: ",number_count)
print("Разность суммы и кол-ва цифр: ", abs(numbers_summ - number_count))