
def new_list(nice_list):
    result = []
    for e in nice_list:
        if isinstance(e,int):
            result.append(e)
        else:
            result.extend(new_list(e))
    return result

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
print("Ответ:",new_list(nice_list))

