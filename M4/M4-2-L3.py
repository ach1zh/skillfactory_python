#M4-2-L3
from imaplib import Flags
from time import process_time_ns

x = [n**2 for n in range(1, 5)]
print(x)
# [1, 4, 9, 16]

x = (n**2 for n in range(1, 5))
print(x)
# <generator object <genexpr> at 0x00000226CD6B6E40>

x = (n**2 for n in range(1, 5))

print(next(x))
# 1
print(next(x))
# 4
print(next(x))
# 9
print(next(x))
# 16
print(next(x, None))
# None

#very_big_data = list(range(1000000000000))

very_big_data = (n for n in range(10000))
very_big_data = list(very_big_data)
print(type(very_big_data), len(very_big_data))
# <class 'list'> 10000


def generate_combinations(colors, sizes):
   for color in colors:
       for size in sizes:
           yield color, size

combination_generator = generate_combinations(["red", "blue"], ["small", "large"])
for combination in combination_generator:
   print(combination)

combination_generator = ((color, size) for size in ["small", "large"] for color in ["red", "blue"])

#Задание 19.3.3 (External resource)
print("\n---------------------------------------->")

def generate_urls(str_URL,n_start,n_end):
    for n in range(n_start,n_end+1):
        yield str_URL + str(n)

url_generator = generate_urls("/product/", 1, 3)
for url in url_generator:
    print(url)
    # /product/1
    # /product/2
    # /product/3

#$for x in range(1,3):
#$    print(x)

#Задание 19.3.4 (External resource)
print("\n---------------------------------------->")
"""
Генерируемые значения — кортеж из имени, фамилии и возраста. 
Данные значения должны генерироваться случайным образом (воспользуйтесь библиотекой random).
"""

import random
def generate_user_data(size,fNames,lNames,rrange):

    for i in range(1,size+1):
        ttuple = (random.choice(fNames),random.choice(lNames),random.randint(rrange[0],rrange[1]))
        #print(ttuple)
        #дошел до сюда вернул значение и заморозился
        yield ttuple


first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]
user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])

#Изначально user_data_generator это объект генератора, а не просчитанные данные
print(user_data_generator)

#при каждом вызове print(user) генерируется значение, пока генератор не окажется пустым
for user in user_data_generator:
    print(user)
    # ('Charlie', 'Williams', 19)
    # ('Charlie', 'Johnson', 48)
    # ('Bob', 'Johnson', 26)
    # ('Charlie', 'Smith', 36)
    # ('Charlie', 'Johnson', 35)




#Задание 19.3.5 (External resource)
print("\n---------------------------------------->")

"""
def func(...):
   # Какой-то набор операций здесь
   for _ in range(...):
       # Генерируем значение последовательности и останавливаем функцию
       yield ...
       # Код здесь выполнится при последующем вызове функции (генерации нового элемента)
   # И код здесь выполнится при последующем вызове функции (генерации нового элемента)


------------------
def fibonacci(n):
    #print(f"Начало функции:{n}")
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



"""

def fibonacci(n):
    x = 0
    y = 1
    for _ in range(n):
        yield x
        #x, y = y, x + y
        xTmp = x
        x = y
        y = xTmp + y


    #while count < n :
    #    nextf = i+j
    #    yield nextf
    #    i = j
    #    j = nextf
    #    count += 1

fibonacci_generator = fibonacci(7)
for number in fibonacci_generator:
   print(number)
# 0
# 1
# 1
# 2
# 3
# 5
# 8






#Задание 19.3.6 (External resource)
print("\n---------------------------------------->")

"""
И она должна сгенерировать последовательность из всех натуральных чисел до этого числа включительно.
Если число делится без остатка только на 1 и на само себя, оно считается простым.
"""

#2 3 4 5 6 7

#2 3 4 5 6 7

def primes(n):
    for i in range(1,n+1):
        primeflag = True
        for j in range(1, n+1):
            #print(i,j)
            #print(i % j == 0)
            if i != 1 and j!= 1 and i != j:
               #print(i, j)
               if i % j == 0:
                   primeflag = False
        if primeflag and i != 1:
            #print(i)
            yield i


prime_generator = primes(15)
for prime in prime_generator:
    print(prime)

# 2
# 3
# 5
# 7
