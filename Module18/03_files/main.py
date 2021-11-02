import sys
file_name = input("Введите имя файла: ")
symbols = "@,№,$,%,^,&,*,(),.".split(',')
for sym in symbols:
    if file_name.startswith(sym):
        print("Ошибка: название начинается на один из специальных символов")
        sys.exit()
if file_name.endswith(".txt") or file_name.endswith(".docx"):
    print("Файл назван верно.")

else:
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
