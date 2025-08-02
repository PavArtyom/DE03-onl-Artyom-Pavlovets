#task1

our_line = str(input("Enter string: "))      # пользовательский ввод строки
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

#task2

sum_of_numbers = 0     # Переменная для суммы чисел
quantity_of_numbers = 0     # Переменная для количества чисел

while True:
    number = float(input("Введите число: "))  # Ввод числа
    sum_of_numbers += number  # Подсчет суммы чисел
    quantity_of_numbers = quantity_of_numbers + 1  # увеличение количества чисел на 1
    if number == 0:
        break  # Выходим из цикла при вводе 0
    average = sum_of_numbers / quantity_of_numbers     # Подсчет среднего значения
print(f'Среднее число:{average}, Сумма чисел:{sum_of_numbers}')    # Вывод на экран среднего и суммы значений

#task3
number_multi = int(input("Введите целое число: "))     # ввод числа с клавиатуры
for i in range(1, 11):          # второй множитель в диапазоне от 1 до 10
    result = i * number_multi       # результат умножения числа с клавиатуры и второго множителя
    print(f'{number_multi} * {i} = {result}')       # вывод на экран произведения

