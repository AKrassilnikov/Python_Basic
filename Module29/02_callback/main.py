
app = {"//":True}

def callback(arg):
    def wrapper(func):
        route = app.get(arg)
        if route:
            response = func()
            print('Ответ:', response)
        else:
            print('Такого пути нет')
    return wrapper

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'