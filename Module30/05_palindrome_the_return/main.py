
from collections import Counter

def can_be_poly(string):
    dict_pal = {}
    for leter in string:
        dict_pal[leter] = dict_pal.get(leter,0) + 1
    count =0
    for leter in dict_pal.values():
        if leter %2 != 0:
            count += 1
    return count <= 1


def can_be_poly2(string):
    return len(list(filter(lambda number: number % 2 ,Counter(string).values()))) <= 2

print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

print(can_be_poly2('ababc'))
print(can_be_poly2('abbbc'))