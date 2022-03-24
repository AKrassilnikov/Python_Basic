import itertools

numbers = "0123456789"
combination = itertools.combinations(numbers,4)
print(*combination,sep="\n")