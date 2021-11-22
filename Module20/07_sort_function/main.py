tuple_number = (1,25,3,4,5,26,48,6,49)
flag = False
for num in tuple_number:
    if isinstance(num,float):
        flag = True
print(sorted(tuple_number) if flag == False else tuple_number)
