def calculate_func(first_number, second_number, operation):
    print('Введите числа и математические операторы:+ , - , * , / ')
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number / second_number
