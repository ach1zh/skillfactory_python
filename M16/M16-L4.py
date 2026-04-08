#M16-L4

#Задание 3.2 (External resource)
print("\n -----> \n")

"""
Напишите функцию check(temps), которая будет выводить словарь, в котором ключи — годы, а значения — показатели температуры. Ключи необходимо отсортировать в порядке убывания соответствующих им температур.
"""

from collections import OrderedDict

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps):
    od = OrderedDict(sorted(temps, key=lambda x: x[1],reverse=True))   
    print(od)

check(temps)

#OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])

#Задание 3.5
print("\n -----> \n")
from collections import deque

users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]
deq_users = deque(users)
print(deq_users)

deq_users.popleft()
deq_users.rotate(-5)
deq_users.count("8")
print(deq_users.pop())
print(deq_users.count(8))