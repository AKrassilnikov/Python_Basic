from time import sleep
from typing import Callable,Any

def slowdown_2s(func: Callable) -> Callable:
    """
    Декоратор для замедления работы функции.

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
        sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapper

@slowdown_2s
def chec_web_site() -> Any:
    print("Checking code changes")

for _ in range(5):
    chec_web_site()

