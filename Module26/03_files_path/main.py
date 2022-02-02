import os

def gen_files_path(path, search_dir):
    for directory in os.listdir(path):
        new_path = os.path.join(path,directory)
        if directory.lower() == search_dir:
           return new_path
        try:
            result = gen_files_path(new_path,search_dir)
            if result:
                return result
        except:
            pass

link = input("Input disk: ").upper()
path = os.path.abspath('{}:\\'.format(link))
search_dir = input("Input name of directory: ").lower()
result = gen_files_path(path,search_dir)
print("Dir path: ",result)
for file_path in os.walk(result):
    print(file_path)

