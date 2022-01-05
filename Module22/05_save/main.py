
import os
data = input("Input data: ")
input_path = input("Input dir path over space: ").split()
file_name = input("Input file name: ")
file_path = os.path.abspath(file_name)
open_file = open(file_path,'w')
open_file.write(data)
open_file.close()
