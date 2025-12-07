#M4-2-L6

def outer_function(param):

    def inner_function():
        print('Вложенная функция имеет доступ к <{}>'.format(param))

    return inner_function  # Возвращаем ссылку на функцию

x = outer_function('Some_Parameter')  # В x теперь хранится ссылка на объект-функцию
x()  # Вызываем её
# Вложенная функция имеет доступ к <Some_Parameter>

#Задание 19.6.6 (External resource)
print("\n-------------------------------------------------->")

def create_counter():
    counter = 0
    def inner_function():
        nonlocal counter
        counter += 1
        return counter
    return inner_function

counter = create_counter()
print(counter())  # вернет "1"
print(counter())  # вернет "2"
print(counter())  # вернет "3"

# 1
# 2
# 3


#Задание 19.6.7 (External resource)
print("\n-------------------------------------------------->")

def create_unique_checker():
    dataSet = set()
    def inner_function(num):
        nonlocal dataSet
        result = None
        if num in dataSet:
            result = False
        else:
            result = True
        dataSet.add(num)
        return result
    return inner_function


unique_checker = create_unique_checker()
print(unique_checker(5))
print(unique_checker(5))
print(unique_checker(10))
# True
# False
# True


#Задание 19.6.8 (External resource)
print("\n-------------------------------------------------->")

import time

"""
#v1
def timer():
    timerData = None

    def inner_function():
        nonlocal timerData
        startTime = time.time()
        if timerData is None:
            timerData = startTime
        result = startTime - timerData
        timerData = startTime
        return result

    return inner_function
"""
#v2
def timer():
    #timerData = None
    #для прохождения автотестов
    timerData = time.time()

    def inner_function():
        nonlocal timerData
        startTime = time.time()
        if timerData is None:
            timerData = startTime
        result = startTime - timerData
        timerData = startTime
        #print(f"-->{result}")
        return result

    return inner_function


#my_timer = timer()
#time.sleep(3)
#print(int(my_timer())) # int — для приближенного значения секунд
## Ждем немного...
#time.sleep(4)
#print(int(my_timer()))
# Вывод:
# 0
# 2

# Создание таймера
elapsed_timer = timer()
print("Test 1: No wait")
time.sleep(0.5)
print(round(elapsed_timer(),1))  # Ожидаемый вывод: примерно 0.5 секун

#Создание таймера
elapsed_timer = timer()
print("Test 5: 0.1 second wait")
time.sleep(0.1)
print(round(elapsed_timer(),2))  # Ожидаемый вывод: примерно 0.1 секунд

#Задание 19.6.9 (External resource)
print("\n-------------------------------------------------->")
import random
def create_password_generator(pass_length,symbols):
    def inner_function():
        nonlocal pass_length,symbols
        result = ''
        for i in range(pass_length):
            result += random.choice(symbols)
        return result
    return inner_function

symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password_generator = create_password_generator(10, symbols_for_password)
print(password_generator())
print(password_generator())

# Stl0tgwWSL
# oboYrgROdF
