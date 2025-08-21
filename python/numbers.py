def filter_even_numbers():
    first_path = "/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/input.txt"
    second_path = "/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/output.txt"
    with open(first_path, "r") as input_file, open(second_path, "r+") as output_file:
        numbers = []
        even_numbers = []
        for line in input_file:
            number = int(line.strip())
            numbers.append(number)
            if number % 2 == 0:
                even_numbers.append(number)
                output_file.write(str(number) + '\n')
    return (f'четные числа: {even_numbers},сумма исходных чисел: {sum(numbers)}, '
            f'Количество четных чисел: {len(even_numbers)}')



