from typing import Callable,Any
from datetime import datetime


def logging(func:Callable) -> Callable:
    """ Функция с запросом и с логированием ошибки в файл """

    print(f'Function name: {logging.__name__}, Description: {logging.__doc__}\n')

    print("Как дела?",end=" ")
    answer = input()
    if not isinstance(answer,str):
        with open("function_errors.log",'a') as log_file:
            error_log = f"{SyntaxError} : {datetime.now()}"
            log_file.write(error_log)
    print("А у меня не очень! Ладно, держи свою функцию.")
    return func


@logging
def test() -> Any:
    print('<Тут что-то происходит...>')

test()
