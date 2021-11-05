def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

text = input("Input text: ")
leters = histogram(text)

for sym_key in leters.keys():
    print(sym_key,":",leters[sym_key])
value_list = set(leters.values())

for num in value_list:
    num_dict = {key for key in leters.keys() if leters[key] == num}
    print(num,":",list(sorted(num_dict)))










