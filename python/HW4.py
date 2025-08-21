"""
task1
Создайте список fruits с элементами "apple", "banana", "cherry". Выведите первый элемент списка.

"""
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

"""
task2
Создайте словарь student с ключами name, age и grade и соответствующими значениями. 
Выведите значение по ключу name.
"""
student = {
    "name": "Artyom",
    "age": 25,
    "grade": 7.8
}
print(student.get("name"))

"""
task3
Напишите программу, которая создает множество уникальных слов из введенной пользователем строки. 
Программа должна учитывать только уникальные слова и игнорировать регистр.
"""
our_input = str(input('Введите строку:'))
words = our_input.lower().split()
unique_words = set(words)
print(unique_words)

"""
task4
Напишите программу, которая создает
список студентов, их возрастов и оценок. 
Используйте списки, кортежи и словари для хранения данных.  
Программа должна выводить всех студентов, их возраста и оценки, 
а также производить операции над этими данными.
"""
students = [
    {'second_name': 'Ivanov', 'name': 'Ivan', 'age': '20', 'grades': [4, 5, 3]},
    {'second_name': 'Petrov', 'name': 'Petr', 'age': '21', 'grades': [5, 4, 5]},
    {'second_name': 'Sidorov', 'name': 'Andrey', 'age': '20', 'grades': [4, 4, 4]},
    {'second_name': 'Kuznetsov', 'name': 'Dmitriy', 'age': '19', 'grades': [5, 5, 5]}
]

for student in students:
    each_student = student.get('second_name')
    grades_each_person = (student.get('grades'))
    print(f'Average grade:{each_student} - {sum(grades_each_person) / len(grades_each_person)}')

for student in students:
    print(student.get('second_name'), end=' ')
    print(student.get('name'))


for student in students:
    general_info = list(student.values())
    print(general_info)



"""
task5
Создайте два списка: [1, 2, 3] и [4, 5, 6]. Напишите
программу, которая объединяет эти списки в один и выводит результат.
"""
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)
print(list_1)

"""
task6
Напишите программу, которая удаляет все дубликаты
из списка [1, 2, 2, 3, 4, 4, 5] с помощью преобразования в множество и выводит результат
"""
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
my_list = list(unique_elements)
print(my_list)
