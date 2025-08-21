"""
task1
Создайте переменную x и присвойте ей значение 10. Выведите значение переменнойна экран.

"""
value = 10
print(value)

"""
task2
Создайте переменные name (строка), age (число) и is_student (булевый тип). Выведите их значения.

"""
name = 'Artyom'
age = 28
is_student = True

print(f'name:{name}, age:{age}, student:{is_student}')

"""
task3
Напишите программу, которая запрашивает у пользователя три числа, 
сравнивает их между собой и выводит максимальное и  минимальное число
"""

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))

if (a <= b) and (a <= c) and (b <= c):
    print(f'min number:{a}, max number:{c}')
elif (a <= b) and (a <= c) and (c <= b):
    print(f'min number:{a}, max number:{b}')
elif (b <= a) and (b <= c) and (c <= a):
    print(f'min number:{b}, max number:{a}')
elif (b <= a) and (b <= c) and (a <= c):
    print(f'min number:{b}, max number:{c}')
elif (c <= a) and (c <= b) and (b <= a):
    print(f'min number:{c}, max number:{a}')
elif (c <= a) and (c <= b) and (a <= b):
    print(f'min number:{c}, max number:{b}')

"""
task4
Напишите программу, которая запрашивает у пользователя его возраст, 
преобразует введенное значение в целое число, 
добавляет к нему 5 и выводит сообщение: "Через 5 лет вам будет X лет", где X — рассчитанное значение.
"""
user_answ = input('Введите ваш текущий возраст:')
user_age = int(user_answ) + 5
print(f'Через 5 лет вам будет {user_age} лет')

"""
task5
Количество чётных и нечётных чисел в диапазоне Задача: 
Пользователь вводит числа a и b (a ≤ b). 
Вывести количество чётных и нечётных чисел в этом диапазоне.
"""

num_of_even = 0
num_of_odd = 0

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
if a <= b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            num_of_even += 1
        else:
            num_of_odd += 1
    print(f'Количество четных:{num_of_even},Количество нечетных: {num_of_odd}')
else:
    print('Введите правильный диапазон')