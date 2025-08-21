"""
task1
Откройте файл example.txt и выведите его содержимое на экран.
"""
file = open(r"/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/example.txt", "r")
content = file.read()
file.close()
print(content)

"""
task2
Создайте файл output.txt и запишите в него строку "Hello, World!"

"""
file = open(r"/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/output.txt", "r+")
input_user = file.write("Hello, World!")
file.close()

"""
task3
Напишите программу, которая считает количество строк, 
слов и символов в заданном текстовом файле и выводит результаты.
"""
file = open(r"/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/thirdtask.txt", "r+")
content = file.readlines()
file.close()
print(f"Количество строк: {len(content)}")

counter = 0
for contain in content:
    words = contain.split()
    num_words = len(words)
    #print(f"Количество слов в каждой строке:{num_words}")
    counter += num_words
print(f"Общее количество слов: {counter}")

count_symbols = 0
for contain in content:
    for symbol in contain:
        if symbol in contain:
            count_symbols += 1
print(f"Количество символов: {count_symbols}")

"""
task4
Напиште программу, которая читает данные из файла students.txt, 
где каждая строка содержит имя и оценку ученика (например: Иван 4). 
Программа должна выбрать только тех учеников, у которых оценка 4 или выше, 
и записать их в новый файл good_students.txt в том же формате.

"""

with open(r"/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/students.txt", "r") as grade_list, open(r"/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/good_students.txt", "w") as good_grade_list:
    for line in grade_list:
        content = line.split()
        if int(content[1]) >= 4:
            good_grade_list.write(line)













