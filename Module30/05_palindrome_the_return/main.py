
from collections import Counter

def can_be_poly(string):
    dict_pal = {}
    for a in string:
        dict_pal[a] = dict_pal.get(a,0) + 1
    count =0
    for a in dict_pal.values():
        if a %2 != 0:
            count += 1
    return count <= 1


def can_be_poly2(string):
    return len(list(filter(lambda x: x % 2 ,Counter(string).values()))) <= 2

print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

print(can_be_poly2('ababc'))
print(can_be_poly2('abbbc'))