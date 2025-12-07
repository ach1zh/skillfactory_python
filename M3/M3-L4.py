# M3-L4

# Итоговое задание

todo = []
n = int("3")
# n = int(input('Введите количество добавляемых записей: '))

if n == 0 or n == None:
    print("Записи добавлять не требуется")
else:
    for i in range(n):
        case = input(("Введите запись № " + str(i + 1) + ": "))
        todo.append(case)
    print("Список всех записей:")
    print(todo)

    n_edit = int(input("\n Введите номер дела, которое необходимо отредактировать: "))
    case_edit = input(("Введите отредактированную запись " + str(n_edit) + ": "))
    todo[n_edit - 1] = case_edit
    print("Список всех записей:")
    print(todo)

    n_edit = int(input("\n Введите номер дела, которое необходимо удалить: "))
    todo.pop(n_edit - 1)
    print("Список всех записей:")
    print(todo)