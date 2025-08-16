def calculate_stats():
    user_input = input("Введите строку чисел через пробел:")
    numbers_input = user_input.split()
    numbers = []
    for num_str in numbers_input:
        num = int(num_str)
        numbers.append(num)
    if sum(numbers) > 100:
        print('Большая сумма')
    return (f'сумма значений: {sum(numbers)}; максимальное значение: {max(numbers)}; минимальное значение:'
            f'{min(numbers)}')






