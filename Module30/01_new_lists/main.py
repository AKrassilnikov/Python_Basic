floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]



floats_new = list(map(lambda num: round(num ** 3,3),floats))
names_new = list(filter(lambda name: len(name) > 5,names))
numbers_new = sum(map(lambda number:number , numbers))



print('New float list: ',floats_new)
print('New names list: ',names_new)
print('Sum of numbers list: ',numbers_new)

