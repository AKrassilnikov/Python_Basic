import os

def find_file(path):
    directories = 0
    files = 0
    size = 0
    for sub_path in os.listdir(path):
        new_path = os.path.join(path, sub_path)
        size += os.path.getsize(new_path)
        if os.path.isfile(new_path):
            files += 1
        if os.path.isdir(new_path):
            directories += 1
    return directories, files, size

path = os.path.abspath(os.path.join("..","..","..","Новая папка"))  # где искать
directories,files, size = find_file(path)
print("Directorys:",directories)
print("Files:",directories)
print("Size:",round(size/1024,2),"MB")
