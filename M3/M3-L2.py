#M3-L2

clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
        'Pam Beesly', 'Kevin Malone']

# выведем нулевой элемент списка
print(clients[0])
# выведем первый элемент списка
print(clients[1])
# выведем список целиком
print(clients)
# выведем предпоследний элемент списка
print(clients[-2])

#Изменение

# изменим третий элемент списка
clients[3] = 'Pam Halpert'

# выведем третий элемент списка
print(clients[3])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[3:6])

#Задание финальное M3-L2
print("\n|>----------------\n")

#2
coworkers = ["Ермолова Виктория","Александрова Амина","Скворцова Мирослава","Савельева Таисия","Евдокимова Александра","Волкова Елизавета","Шишкина Мария","Новикова Виктория","Михайлова Виктория","Харитонова Арина"]

#3
print(coworkers[0])
print("\n")
print(coworkers[-1])
print("\n")

#4
print(coworkers[::1])
print("\n")
print(coworkers[::2])
print("\n")
#5
print(len(coworkers))
print("\n")

#6
#client_name = input('Введите имя клиента: ')
client_name = "Бородина Анна"
coworkers.append(client_name)
print(len(coworkers))
print(coworkers[-1])

#7
#client_name = input('Введите имя клиента: ')
client_name = "Бородина Анна"
client_name = "Сорокина Вероника"
if client_name in coworkers:
    print("такие есть у нас")
else:
    print("таких у нас нет")