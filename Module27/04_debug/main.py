
def debug(name):
    def wrapper(*args,**kwargs):
        print(f"Вызывыется {name.__name__},{args},{kwargs}")
        result = name(*args,**kwargs)
        print(result,"\n")
    return wrapper

@debug
def greeting(name, age=None) -> str:
    """ That function returns person info """

    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

if __name__ == '__main__':
    greeting("Том")
    greeting("Миша", age=100)
    greeting(name="Катя", age=16)