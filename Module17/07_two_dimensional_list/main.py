def new_lsts(n):
    start = n
    small_list = [num for num in range(start,13,4)]
    return small_list

new_list = [new_lsts(n) for n in range(1,5)]
print(new_list)
