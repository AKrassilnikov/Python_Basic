ls = '4 0 5 0 3 0 0 5'.split(' ')
result = [num for num in ls if num != '0']
count_zero = len(ls) - len(result)
result += ['0' for _ in range(count_zero)]
print(result)
result = result[0:count_zero]
print(result)
