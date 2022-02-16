from typing import Callable,Any

def how_are_you(func: Callable) -> Callable:
    """
    Декоратор для взаимодействия с пользователем

    :param func:
    :return:
    """
    # @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функция - обертка
        :param args:
        :param kwargs:
        :return:
        """
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result
    return wrapper

@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()













