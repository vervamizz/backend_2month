def log_execution(func):
    def wrapper(a, b):
        print(f'Функция {func.__name__} вызвана с аргументами {(a, b)}')
        result = func(a, b)
        print(f'Результат: {result}')
        print('Функция завершена')
        return result
    return wrapper

@log_execution
def add(a, b):
    return a + b

add(5, 3)

def require_admin(func):
    def wrapper(user):
        if user.role == 'admin':
            func(user)
        if user.role != 'admin':
            print("Доступ запрещен!")
    return wrapper


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

@require_admin
def delete_database(user):
    print("База данных удалена")

user1 = User('Syrga', 'admin')
user2 = User('Aisuluu', 'user')

delete_database(user1)
delete_database(user2)