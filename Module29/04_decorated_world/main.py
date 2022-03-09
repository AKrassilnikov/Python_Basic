from typing import Callable
import functools

def decoretor_for_decorator(decorator_to: Callable) -> Callable:
    """ Декоратор для декоратора - принимает аргументы """
    def decorator_maker(*args,**kwargs) -> Callable:
        def decorator_wrapper(func : Callable) -> Callable:
            return decorator_to(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

@decoretor_for_decorator
def decorated_decorator(func:Callable, *dec_arg, **dec_kwarg) -> Callable:
    """ Декоратор Шаблон """
    @functools.wraps(func)
    def wrapper(*func_args,**func_kwargs) -> Callable:
        print("Передаём данные в декоратор", dec_arg,dec_kwarg)
        return func(*func_args,**func_kwargs)
    return wrapper



@decorated_decorator(100,'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """ Пример декорируемой функции """
    print("Привет", text, num)


decorated_function("Юзер", 101)




