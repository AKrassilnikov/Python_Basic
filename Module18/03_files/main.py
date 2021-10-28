import sys
file_name = input("Введите имя файла: ")
symbols = "@,№,$,%,^,&,*,(),.".split(',')
for sym in symbols:
    if file_name.startswith(sym):
        print("Ошибка: название начинается на один из специальных символов")
        sys.exit()
if not file_name.endswith(".txt") or file_name.endswith(".docx"):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")
