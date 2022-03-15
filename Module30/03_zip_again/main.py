from typing import List

strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = list(map(lambda leter, number : (leter,number), strings,numbers))
print("Result: ",new_list)