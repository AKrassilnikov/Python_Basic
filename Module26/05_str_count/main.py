import os

def line_code_count(path):
    line_count = 0
    for py_file in os.listdir(path):
        if py_file.endswith(".py"):
            with open(os.path.join(path,py_file),"r",encoding="utf-8") as file:
                for line in file.readlines():
                    if line.startswith("#") or line == "\n":
                        pass
                    else:
                        line_count += 1
    return line_count

path = "E:\Python"
result = line_code_count(path)
print("Number of code lines = ",result)