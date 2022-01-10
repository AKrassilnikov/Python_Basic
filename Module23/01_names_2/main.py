test_file = open('people.txt','r')
summ = 0
for line in test_file.readlines():
    try:
        if len(line) - 1 < 3:
            raise TypeError
            pass
        else:
            summ += len(line) - 1
    except TypeError:
        print('In',line,'Lower than 3 symbols')
print('Sum of all symbols:',summ)

