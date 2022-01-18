
class Student:
    def __init__(self,name,groupe,progress,avarage):
        self.name = name
        self.group = groupe
        self.progress = progress
        self.avarage = avarage

    def __repr__(self):   # предоставление экз классов ввиде списка кортежей и можно делать операции
        return repr((self.name, self.group, self.progress, self.avarage))

def progress(data):
    nums = []
    for num in data:
        nums.append(int(num))
    avarage = sum(nums) / len(nums)
    return nums,avarage

student_list = []
with open('24 - 2.txt','r') as student_file:
    for line in student_file.readlines():
        nums,avarage = progress(line.split()[2:])
        student_list.append(Student(line.split()[0],line.split()[1],nums,avarage))
student_list.sort(key=lambda av:av.avarage,reverse=True)  # сортировка при __repr__
for list in student_list:
    print(list.name, list.group, list.avarage)  # __repr__ - отображение принтом










