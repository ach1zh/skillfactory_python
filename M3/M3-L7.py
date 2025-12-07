# M3-L7
# Итоговое задание

#1 Добавьте возможность удалять и редактировать данные по оценкам, предметам и ученикам.
#2 Добавьте вывод информации по всем оценкам для определенного ученика.
#3 Добавьте вывод среднего балла по каждому предмету по определенному ученику.
#4 Добавьте еще команды, которые, на ваш взгляд, могут быть полезны для этой задачи.

"""
#Новая структура меню программы:

1. Редактирование данных
    1.1 Добавление записей
        1.1.1 Добавление записей учеников
        1.1.2 Добавление записей предметов
        1.1.3 Добавление записей оценок
        1.1.4 Выход в предыдущий пункт меню
    1.2 Редактирование записей
        1.2.1 Редактирование записей учеников
        1.2.2 Редактирование записей предметов
        1.2.3 Редактирование записей оценок
        1.2.4 Выход в предыдущий пункт меню
    1.3 Удаление записей
        1.3.1 Удаление записей учеников
        1.3.2 Удаление записей предметов
        1.3.3 Удаление записей оценок
        1.3.4 Выход в предыдущий пункт меню
    1.4 Выход в предыдущий пункт меню
2. Просмотр данных
    2.1 Вывод всех оценок по всем ученикам
    2.2 Вывод всех оценок определенного ученика
    2.3 Вывод среднего балла по каждому предмету по каждому ученику
    2.4 Вывод среднего балла по каждому предмету по определенному ученику
    2.5 Выход в предыдущий пункт меню
3. Выход из программы
"""

###
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

#####

while True:

    print("\n1. Редактирование данных\n2. Просмотр данных\n3. Выход из программы\n")
    command = int(input('Введите команду: '))

    # 1. Редактирование данных
    if command == 1:

        while (True):

            print(
                "\n1.1 Добавление записей\n1.2 Редактирование записей\n1.3 Удаление записей\n1.4 Выход в предыдущий пункт меню\n")
            command = int(input('Введите команду: '))

            # 1.1 Добавление записей
            if command == 1:

                while (True):

                    print(
                        "\n1.1.1 Добавление записей учеников\n1.1.2 Добавление записей предметов\n1.1.3 Добавление записей оценок\n1.1.4 Выход в предыдущий пункт менюю\n")
                    command = int(input('Введите команду: '))

                    # 1.1.1 Добавление записей учеников
                    if command == 1:
                        # print("1")

                        print('Добавление записи новго ученика ')
                        # Считываем данные
                        student = input('Введите имя ученика: ')

                        # Проверка данных
                        if student not in students_marks.keys():
                            # добавляем нового ученика
                            students_marks[student] = {}

                            for class_ in classes:
                                marks = [0 for i in range(3)]
                                students_marks[student][class_] = marks

                        else:
                            print('ОШИБКА: такое имя уже есть в списке')

                    # 1.1.2 Добавление записей предметов
                    elif command == 2:

                        # print("2")
                        print('Добавление записи новго предмета ')
                        # Считываем данные
                        class_ = input('Введите предмет: ')

                        # Проверка данных
                        if class_ not in students_marks[student].keys():
                            # добавляем новый предмет
                            for student in students_marks:
                                class_new = {}
                                # marks_new = []
                                marks_new = [0 for i in range(3)]
                                class_new[class_] = marks_new
                                students_marks[student].update(class_new)

                            print(f'Для всех студентов добавлен новый предмет {class_}')
                        # неверно введены название предмета или имя ученика
                        else:
                            print('ОШИБКА: такой предмет уже есть в списке')

                    # 1.1.3 Добавление записей оценок
                    elif command == 3:
                        # print("3")

                        print('Добавление оценки ученика по предмету')

                        # Считываем данные
                        student = input('Введите имя ученика: ')
                        class_ = input('Введите предмет: ')
                        mark = int(input('Введите оценку: '))

                        # Проверка данных
                        if student in students_marks.keys() and class_ in students_marks[student].keys():
                            # добавляем новую оценку для ученика по предмету
                            students_marks[student][class_].append(mark)
                            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                        # неверно введены название предмета или имя ученика
                        else:
                            print('ОШИБКА: неверное имя ученика или название предмета')

                    # 1.1.4 Выход в предыдущий пункт меню
                    elif command == 4:
                        print("4")
                        break
                    else:
                        print("Некорректный ввод")

            # 1.2 Редактирование записей
            elif command == 2:

                while (True):

                    print(
                        "\n1.2.1 Редактирование записей учеников\n1.2.2 Редактирование записей предметов\n1.2.3 Редактирование записей оценок\n1.2.4 Выход в предыдущий пункт меню\n")
                    command = int(input('Введите команду: '))

                    # 1.2.1 Редактирование записей учеников
                    if command == 1:
                        # print("1")

                        print('Изменение записи ученика ')

                        # Считываем данные
                        student_name = input('Введите имя ученика: ')
                        student_name_new = input(f'Введите новое имя ученика {student_name}: ')

                        # Проверка данных !!!
                        if student_name in students_marks.keys():

                            students_marks[student_name_new] = students_marks.pop(student_name)
                        else:
                            print('ОШИБКА: такого имени нет в списке')

                    # 1.2.2 Редактирование записей предметов
                    elif command == 2:
                        print("2")
                        print('Изменение записи предмета ')

                        # Считываем данные
                        class_name = input('Введите имя предмета: ')
                        class_name_new = input(f'Введите новое имя предмета {class_name}: ')

                        # Проверка данных !!!
                        for student in students:
                            flag = 0
                            if class_name in students_marks[student].keys():
                                students_marks[student][class_name_new] = students_marks[student].pop(class_name)

                                flag = 1
                            if flag == 0:
                                print('ОШИБКА: такого имени нет в списке')

                    # 1.2.3 Редактирование записей оценок
                    elif command == 3:
                        # print("3")
                        print('Изменение записи оценки')

                        # Считываем данные
                        student = input('Введите имя ученика: ')
                        class_ = input('Введите предмет: ')

                        # Проверка данных
                        if student in students_marks.keys() and class_ in students_marks[student].keys():

                            print(f"\nОценки {student} по предмету {class_} : {students_marks[student][class_]}\n")

                            # Считываем данные
                            mark_index = int(input('Введите порядковый номер изменяемой оценки начиная с 0: '))
                            mark_new = int(input('Введите новое значение оценки: '))

                            # Проверка данных
                            if (mark_index) <= len(students_marks[student][class_]):
                                students_marks[student][class_][(mark_index)] = mark_new
                            else:
                                print("Не корректный порядковый номер изменяемой оценки")

                        # неверно введены название предмета или имя ученика
                        else:
                            print('ОШИБКА: неверное имя ученика или название предмета')

                    # 1.2.4 Выход в предыдущий пункт меню
                    elif command == 4:
                        print("4")
                        break
                    else:
                        print("Некооретный ввод")

            # 1.3 Удаление записей
            elif command == 3:

                while (True):

                    print(
                        "\n1.3.1 Удаление записей учеников\n1.3.2 Удаление записей предметов\n1.3.3 Удаление записей оценок\n1.3.4 Выход в предыдущий пункт меню")
                    command = int(input('Введите команду: '))

                    # 1.3.1 Удаление записей учеников
                    if command == 1:
                        # print("1")

                        # print("1")

                        print('Удаление записи ученика')

                        # Считываем данные
                        student_name = input('Введите имя ученика: ')

                        # Проверка данных !!!
                        if student_name in students_marks.keys():
                            print(f"\nУдаление {student_name}\n")
                            del students_marks[student_name]
                        else:
                            print('ОШИБКА: такого имени нет в списке')

                    # 1.3.2 Удаление записей предметов
                    elif command == 2:
                        # print("2")
                        print('Удаление записи предмета ')

                        # Считываем данные
                        class_name = input('Введите имя предмета: ')

                        for student in students_marks.keys():
                            if class_name in students_marks[student].keys():
                                print(f"\nУдаление {class_name}\n")
                                del students_marks[student][class_name]

                            # else:
                            #    print('ОШИБКА: такого предмета нет в списке')

                    # 1.3.3 Удаление записей оценок
                    elif command == 3:
                        # print("3")
                        print('Удаление записи оценки')

                        # Считываем данные
                        student_name = input('Введите имя ученика: ')
                        class_name = input('Введите предмет: ')

                        # Проверка данных
                        if student_name in students_marks.keys() and class_name in students_marks[student].keys():

                            print(f"\nОценки {student_name} по предмету {class_name} : {students_marks[student_name][class_name]}\n")

                            # Считываем данные
                            mark_index = int(input('Введите порядковый номер удаляемой оценки начиная с нуля: '))
                            # Проверка данных
                            if (mark_index) <= len(students_marks[student_name][class_name]):
                                students_marks[student_name][class_name].pop(mark_index)
                            else:
                                print("Не корректный порядковый номер изменяемой оценки")
                        # неверно введены название предмета или имя ученика
                        else:
                            print('ОШИБКА: неверное имя ученика или название предмета')

                    # 1.3.4 Выход в предыдущий пункт меню
                    elif command == 4:
                        print("4")
                        break
                    else:
                        print("Некооретный ввод")

                        # 1.4 Выход в предыдущий пункт меню
            elif command == 4:
                print("4")
                break

            else:
                print("Некорректный ввод")

    # 2. Просмотр данных
    elif command == 2:

        while (True):

            print("\n2.1 Вывод всех оценок по всем ученикам\n2.2 Вывод всех оценок определенного ученика\n2.3 Вывод среднего балла по каждому предмету по каждому ученику\n2.4 Вывод среднего балла покаждому предмету по определенному ученику\n2.5 Выход в предыдущий пункт меню\n")
            command = int(input('Введите команду: '))

            # 2.1 Вывод всех оценок по всем ученикам
            if command == 1:
                #print("1")
                for student in students_marks:
                    print(f"{student} \t{students_marks[student]}")

            # 2.2 Вывод всех оценок определенного ученика
            elif command == 2:
                #print("2")
                student_name = input('Введите имя ученика: ')

                # Проверка данных
                if student_name in students_marks.keys():
                    print(f"\n{student_name} \t{students_marks[student_name]}")
                else:
                    print("Такого ученика нет в списке")

            # 2.3 Вывод среднего балла по каждому предмету по каждому ученику
            elif command == 3:
                #print("3")

                for student_name in students_marks.keys():
                    print(f"\n{student_name} :\n")
                    for class_name in students_marks[student].keys():

                        # находим сумму оценок по предмету
                        marks_sum = sum(students_marks[student_name][class_name])
                        # находим количество оценок по предмету
                        marks_count = len(students_marks[student_name][class_name])
                        # выводим средний балл по предмету
                        print(f'{class_name} - {marks_sum // marks_count}')

            # 2.4 Вывод среднего балла по каждому предмету по определенному ученику
            elif command == 4:
                #print("4")

                student_name = input('Введите имя ученика: ')

                # Проверка данных
                if student_name in students_marks.keys():

                    print(f"\n{student_name} :\n")
                    for class_name in students_marks[student_name].keys():
                        # находим сумму оценок по предмету
                        marks_sum = sum(students_marks[student_name][class_name])
                        # находим количество оценок по предмету
                        marks_count = len(students_marks[student_name][class_name])
                        # выводим средний балл по предмету
                        print(f'{class_name} - {marks_sum // marks_count}')
                else:
                    print("Такого ученика нет в списке")

            # 2.5 Выход в предыдущий пункт меню
            elif command == 5:
                #print("5")
                break

            else:
                print("Некорректный ввод")

    # 3. Выход из программы
    elif command == 3:
        #print('3. Выход из программы')
        break

    else:
        print("Некорректный ввод")