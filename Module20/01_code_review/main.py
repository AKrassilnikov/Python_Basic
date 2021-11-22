students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def def_list(dict):
    hobby_list = []
    string = ''
    for i in dict:
        hobby_list += (dict[i]['interests'])
        string += dict[i]['surname']
    return hobby_list, len(string)

pairs = []
for i in students:
    print("ID {} возраст {}".format(i, students[i]['age']))

hobby_list, surname_length = def_list(students)
print("Список хобби {}, \nДлина символов фамилий {}".format(hobby_list, surname_length))


