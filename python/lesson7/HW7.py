"""
task1
Напишите функцию, которая принимает список чисел и возвращает их среднее значение.
Обработайте исключения, связанные с пустым списком и некорректными типами данных.
"""

def calcaveragevalue(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

try:
    average = calcaveragevalue([1, 10, 22])
    print(f'Среднее значение: {average}')
except TypeError as e:
    print(f'Некорректный тип: {e}')
except ValueError:
    print(f'Ошибка ввода')
except ZeroDivisionError:
    print(f'пустой список')


"""
task2
Создайте программу, которая считывает список чисел из файла, проверяет каждое число на чётность 
и записывает результаты (чётное или нечётное) в другой файл. 
Используйте обработку исключений для возможных ошибок ввода-вывода.
"""

def check_even_or_odd():
    try:
        path_1 = "/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson7/original_list.txt"
        path_2 = "/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson7/sorted_list_elements.txt"
        with open(path_1, "r") as original_file, open(path_2, "w+") as sorted_file:
            for line in original_file:
                try:
                    number = int(line.strip())
                    if number % 2 == 0:
                        result = 'Четное'
                    else:
                        result = 'Нечетное'
                    sorted_file.write(str(number) + '-' + result +'\n')
                except ValueError as e:
                    print(f'Некорректный формат: {e} ')
    except FileNotFoundError as e:
        print('Некорректный путь, файл не найден')

checking_values = check_even_or_odd()

"""
task3
Создайте программу, которая запрашивает у пользователя список чисел, введённых через пробел, 
и сохраняет их в список; напишите функцию, которая перебирает этот список в цикле и 
вычисляет квадрат каждого числа, но если встречается отрицательное число, выбрасывается собственное 
исключение NegativeNumberError с сообщением «Отрицательные числа недопустимы», 
при этом программа должна обработать это исключение, вывести сообщение об ошибке 
 продолжить обработку остальных элементов, а в конце вывести итоговый список квадратов 
 всех корректных чисел.

"""


class NegativeNumberError(Exception):
    pass

def square(numbers):
    square_numbers = []
    for num_str in numbers:
        try:
            number = int(num_str)
            if number < 0:
                raise NegativeNumberError("Отрицательные числа недопустимы")
            else:
                square_numbers.append(number ** 2)
        except NegativeNumberError as e:
            print(f'Обработка числа прервана {num_str}.Ошибка: {e}')
    return square_numbers

user_input = input("Введите строку чисел через пробел:")
numbers_input = user_input.split()
numbers = []
for num_str in numbers_input:
    try:
        num = int(num_str)
        numbers.append(num)
    except ValueError as e:
        print(f'Введите правильный тип данных: {e}')
print(f'Исходный список чисел: {numbers}')

correct_result = square(numbers)
print(f'Конечный список чисел: {correct_result}')

"""
task4
Создайте программу, которая запрашивает у пользователя пары «ключ:значение», 
введённые через запятую, и сохраняет их в словарь; напишите функцию, 
которая в цикле проходит по словарю и проверяет, чтобы все значения были положительными числами, 
при этом если встречается отрицательное число или строка вместо числа, 
выбрасывается собственное исключение InvalidValueError с сообщением 
«Некорректное значение для ключа <ключ>», программа должна обработать это исключение,
 вывести предупреждение и продолжить проверку остальных элементов, 
 а в конце вывести словарь только с корректными данными.
"""

class InvalidValueError(Exception):
    pass

input_value = input('Введите пары "ключ:значение через запятую:')
user_dict = {}
input_value_string = input_value.split(',')
for every_string in input_value_string:
    try:
        if ':' in every_string:
            key_value = every_string.split(':', 1)
            key = key_value[0]
            value = key_value[1]
            if key:
                user_dict[key] = int(value)
    except ValueError as e:
        print(f'Введите правильный тип значений словаря {e}:')
print(f'Исходный словарь:{user_dict}')

def correctkeysdict(input_dict):
    positive_dict = {}
    for key, value in input_dict.items():
        try:
            if isinstance(value, str) or (value) < 0:
                raise InvalidValueError('Некорректное значение ключа')
            else:
                positive_dict[key] = value
        except InvalidValueError as e:
            print(f'Некорректное значение для ключа:{key}, {e}')
    return positive_dict


correct_dict = correctkeysdict(user_dict)
print(f'Словарь с корректными данными:{correct_dict}')

"""
task5
Создайте программу, которая запрашивает у пользователя число и с помощью цикла считает факториал этого числа, 
при этом если пользователь вводит отрицательное значение, 
должно выбрасываться собственное исключение NegativeFactorialError 
с сообщением «Факториал отрицательных чисел не определён», 
программа должна обработать это исключение и вывести сообщение об ошибке, 
а при корректном вводе — напечатать результат вычисления факториала.
"""

class NegativeFactorialError(Exception):
    pass

def calcfact(number):
        if number < 0:
            raise NegativeFactorialError('Факториал отрицательных чисел не определен')
        elif number == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, number +1):
               factorial *= i
            return factorial

try:
    user_input = input('Введите число:')
    num = int(user_input)
    calc_fact = calcfact(num)
    print(f'Факториал числа равен:{calc_fact}')
except NegativeFactorialError as e:
    print(f'Введено отрицательное число:{e}')







#


