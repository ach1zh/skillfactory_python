import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарьяяя', 'Ангелина']
students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']

# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

# сгенерируем данные по оценкам:
for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print("--------------->")
#######


# print("3")
print('Удаление записи оценки')
# Считываем данные
student_name = 'Ярослав'
class_name = 'Математика'

# Проверка данных
if student_name in students_marks.keys() and class_name in students_marks[student].keys():

    print(f"\nОценки {student_name} по предмету {class_name} : {students_marks[student_name][class_name]}\n")

    # Считываем данные
    #mark_index = int(input('Введите порядковый номер удаляемой оценки начиная: '))
    mark_index = 2

    #print(students_marks[student_name][class_name])

    # Проверка данных
    if (mark_index) <= len(students_marks[student_name][class_name]):

        students_marks[student_name][class_name].pop(mark_index)
        print(students_marks[student_name][class_name])
    else:
        print("Не корректный порядковый номер изменяемой оценки")

# неверно введены название предмета или имя ученика
else:
    print('ОШИБКА: неверное имя ученика или название предмета')

