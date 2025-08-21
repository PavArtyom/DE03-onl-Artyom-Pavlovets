def register_user():
    name = str(input('Введите ваше имя:'))
    age = int(input('Введите ваш возраст:'))
    if age < 18:
        return 'Доступ ограничен'
    else:
        return f'Добро пожаловать,{name}'

