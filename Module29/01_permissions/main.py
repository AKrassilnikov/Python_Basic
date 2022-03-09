
def check_permission(user_permission):
    def check_access(func):
        def wrapper(arg):
            if user_permission != arg:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            result = func(arg)
            return result
        return wrapper
    return check_access

user_permission = 'admin'

@check_permission(user_permission)
def delete_site(user):
    print('Удаляем сайт')

@check_permission(user_permission)
def add_comment(user):
    print('Добавляем комментарий')

delete_site('admin')
print()
add_comment('user')







