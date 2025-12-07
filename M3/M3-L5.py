numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
## считываем номер строки элемента
# rows = int(input('Введите номер строки 0-3: '))
## считываем номер столбца элемента
# columns = int(input('Введите номер столбца 0-2: '))
## выводим элемент по заданному индексу
# print(f'Искомый элемент: {numbers[rows][columns]}')

print("\n")
print(numbers[0][2])

# ------------

# считываем количество строк массива
# rows = int(input('Введите количество строк массива: '))
# считываем количество столбцов массива
# columns = int(input('Введите количество столбцов массива: '))
# создаем пустой массив


rows = 5
columns = 3
array = []
"""
for i in range(rows):
    # каждая строка массива состоит из columns элементов
    array.append([0]*columns)

# выводим сгенерированный массив
print(f'Сгенерирован пустой массив: {array}')

# Заполним массив элементами с помощью вложенного цикла for
for i in range(rows): # цикл по строкам
    for j in range(columns): # цикл по столбцам
        print()
        print(f'Строка:{i} Столбец:{j}')
        array[i][j] = int(input(f'array[{i}][{j}] = '))

# выводим заполненный массив
print()
print(f'Заполненный массив: {array}')
"""

print()
num = 2
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
for i in numbers:
    print(num in i)

print("\n|>----------------\n")
# Итоговое задание M3-L5
print()

todo_list = [  # утро  день  вечер
    ['', '', ''],  # понедельник
    ['', '', ''],  # вторник
    ['', '', ''],  # среда
    ['', '', ''],  # четверг
    ['', '', ''],  # пятница
    ['', '', ''],  # суббота
    ['', '', ''],  # воскресенье
]

# print(todo_list)

import random
import string

# print(todo_list[1][1])
# print(len(todo_list))

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
time = ['утро', 'день', 'вечер']

for i in range(len(todo_list)):
    for j in range(len(todo_list[i])):
        # print(f"Заполняется: {days[i]}, {time[j]}")
        # in_d = input('Введите данные: ')
        # todo_list[i][j] = in_d
        todo_list[i][j] = ''.join(random.choices(string.ascii_letters, k=10))

print(todo_list)

# print()
# print('Удаляем запись: ')
# i = int(input('Введите индекс дня недели: '))
# j = int(input('Введите индекс времени дня: '))
# удаляем запись
# todo_list[i].pop(j)


# print(todo_list)

# print()
# print('Добавляем запись: ')
# i = int(input('Введите индекс дня недели: '))
# task = input('Введите дело: ')
# todo_list[i].append(task)
# print(todo_list)

print()
print('Итоговый список дел: ')
for i in range(7):
    print(days[i])
    print(todo_list[i])
    print()