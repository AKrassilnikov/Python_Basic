string = input("Введите строку: ")
new_string = [leter for leter in range(len(string)) if string[leter] == 'h']
rev_string = string[new_string[0] + 1 : new_string[1]][::-1]
new_string = string[:new_string[0] + 1] + rev_string + string[new_string[1]:]
print(new_string)
