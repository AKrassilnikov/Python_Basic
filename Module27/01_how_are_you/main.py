from typing import Callable,Any

def how_are_you(func:Callable) -> Callable:
    """ Функция с запросом """

    print("Как дела?",end=" ")
    input()
    print("А у меня не очень! Ладно, держи свою функцию.")
    return func


@how_are_you
def test() -> Any:
    print('<Тут что-то происходит...>')

if __name__== '__main__':
    test()












