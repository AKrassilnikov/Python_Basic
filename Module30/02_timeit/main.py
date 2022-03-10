import timeit

num_list = timeit.timeit("-".join(str(n) for n in range(100)),number=10000)
print("Time:",num_list)

print('Var №1')
num_list_v1 = ["-".join(str(n) for n in range(100))]
print("Time:",timeit.timeit(*num_list_v1,number=10))

print('Var №2')
num_list_v2 =  timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print("Time:",num_list_v2)