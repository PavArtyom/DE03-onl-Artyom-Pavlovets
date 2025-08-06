"""
task1
Напишите программу,которая запрашивает у пользователя строку
и выводит количество гласных и согласных букв в этой строке.

"""

our_line = str(input("Введите строку: "))      # пользовательский ввод строки
vowels = 'aeyuoi'     # переменная строкового типа со всеми гласными буквами
consonants = 'cbxdfghjklmnpqrstvwxyz'      # переменная со всеми согласными буквами
sum_vowels = 0
sum_consonants = 0
for letter in our_line.lower():      # для каждой буквы в нашей введенной строке
    if letter in vowels:      # если буква содержится в строке с гласными
       sum_vowels += 1      # добавляем в счетчик гласных букв
    elif letter in consonants:
       sum_consonants += 1      # добавляем счетчик согласных букв
print(f'Гласные:{sum_vowels}, cогласные:{sum_consonants}')     # выводим сумму гласных и согласных букв

"""
task2
Напишите программу, которая запрашивает у пользователя числа, вычисляет их сумму и среднее значение. 
Программа должна использовать циклы для обработки ввода и условные операторы для проверки корректности ввода.

"""

sum_of_numbers = 0     # Переменная для суммы чисел
quantity_of_numbers = 0     # Переменная для количества чисел

while True:
    number = float(input("Введите число или 0 для выхода: "))  # Ввод числа
    sum_of_numbers += number  # Подсчет суммы чисел
    quantity_of_numbers = quantity_of_numbers + 1  # увеличение количества чисел на 1
    if number == 0:
        break  # Выходим из цикла при вводе 0
    average = sum_of_numbers / quantity_of_numbers     # Подсчет среднего значения
print(f'Среднее число:{average}, Сумма чисел:{sum_of_numbers}')    # Вывод на экран среднего и суммы значений

"""
task3
Разработайте программу, которая запрашивает у пользователя число 
и выводит таблицу умножения для этого числа до 10.

"""
number_multi = int(input("Введите целое число: "))     # ввод числа с клавиатуры
for i in range(1, 11):          # второй множитель в диапазоне от 1 до 10
    result = i * number_multi       # результат умножения числа с клавиатуры и второго множителя
    print(f'{number_multi} * {i} = {result}')       # вывод на экран произведения

"""
task4
Калькулятор: Напишите программу, которая выполняет простейшие арифметические
операции (сложение, вычитание, умножение, деление) между двумя числами в
зависимости от выбора пользователя. Используйте условные операторы if-elifelse для обработки выбора операции.

"""
first_number = float(input('Введите первое число:'))
second_number = float(input('Введите второе число:'))
math_operator = input('Введите математический оператор /,*,+,-:')

if math_operator == '/':
    print(first_number / second_number)
elif math_operator == '*':
    print(first_number * second_number)
elif math_operator == '+':
    print(first_number + second_number)
elif math_operator == '-':
    print(first_number - second_number)
else:
    print('Введите правильный оператор')

"""
task5
Числа Фибоначчи: Напишите программу, которая выводит первые 10 чисел
Фибоначчи с использованием цикла for.

"""

first_fibon = second_fibon = 1
n = int(input('Введите число:'))

print(first_fibon, second_fibon, end=' ')

for i in range(2, n):
    first_fibon, second_fibon = second_fibon, first_fibon + second_fibon
    print(second_fibon, end=' ')

"""
task6
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!

"""

factor = int(input('\nВведите число:'))

factorial = 1

for i in range(2, factor + 1):
    factorial *= i
print(factorial)