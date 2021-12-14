def my_zip(it1, it2):
    ite1 = iter(it1)
    ite2 = iter(it2)
    try:
        while True:
            v1 = next(ite1)
            v2 = next(ite2)
            yield (v1, v2)
    except StopIteration:
        return

for a in my_zip([1, 2, 3], [11, 22, 33, 44]):
    print(a)

for a in my_zip("asdf", "123456"):
    print(a)

for a in my_zip(('a', 'b', 'c'), [1, 2, 3, 4, 5]):
    print(a)