nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list = [num for list_in in nice_list for nums in list_in for num in nums]
print(new_list)