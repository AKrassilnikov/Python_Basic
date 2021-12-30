
import os
data = input("Input data: ")
input_path = input("Input dir path over space: ").split()
file_path = r'C:\{}\{}\{}\{}\{}'.format(input_path[0],input_path[1],input_path[2],input_path[3],input_path[4])
file_mane = input("Input file name: ")
if os.path.exists(file_path):
    open_file = open(os.path.join(file_path,file_mane),'w')
    open_file.write(data)
    open_file.close()
else:
    print("That path is not exist")