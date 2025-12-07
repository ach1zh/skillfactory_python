# создаем словарь
translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
print('Исходный словарь:')
# цикл по элементам словаря
for key, value in translator.items():
    # выводим пары ключ - значение
    print(f'{key} - {value}')

print("\n|>----------------\n")

# Итоговое задание

phoneBook = {'Маша':'84954374670','Даша':'84954374671','Наташа':'84954374672','Саша':'84954374673','Глаша':'84954374674',}

print(phoneBook)
print(phoneBook.keys())
print(phoneBook.values())

#Контакт: {Имя} Телефон: {Номер телефона} (метод items()).

for key, value in phoneBook.items():
    print(f'Контакт: {key} Телефон: {value}')

#n = input('Введите колличество контактов, которые хотите добавить')
n = 2

for i in range(n):
    newName = input('Введите имя новго контакта:\n')
    newNumber = input('Введите телефонный номер новго контакта:\n')
    phoneBook[newName] = newNumber

print()
print(phoneBook)
print()

toEditName = input('Введите имя контакта, который хотите изменить\n')
if toEditName in phoneBook:
    toEditNumber = input(f'Введите новый номер для {toEditName}\n')
    phoneBook[toEditName] = toEditNumber
else:
    print("Такого имени нет в телефонной книге\n")

print()
print(phoneBook)
print()

#4

toEditName = input('Введите имя контакта\n')
if toEditName in phoneBook:
    print(phoneBook.pop(toEditName) + " удален !")
else:
    print("Такого имени нет в телефонной книге. Добавляем.\n")
    phoneBook[toEditName] = 'лень добавлять'

print()
print(phoneBook)
print()
