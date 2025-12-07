#M4-1-L5
from traceback import format_exc

from unicodedata import digit


#list1, *list2 = [1, 2, 3, 4, 5]
#print(list2)

#Задание 19.5.2 (External resource)

def calculate_average(*args):
    return sum(args) / len(args)

print(calculate_average(1.2, 0.9, 1.3, 1.1, 1.7))
# 1.24



#Задание 19.5.3 (External resource)
print("\n---------->")

def check_data_format(**kwargs):

    #print(kwargs.keys())
    #print(kwargs.values())
    #print(kwargs.items())

    result = True
    for key, value in kwargs.items():
        if type(key) != str or (type(value) != int and type(value) != float):
            result = False
    return result

#check_data_format(uid=24891, age=30, height=180)

print(check_data_format(uid=24891, age=30, height=180))
print(check_data_format(uid=24191, age="30", height=156))
#check={"a":1,"b":2.5,"c":[3]}
print(check_data_format(a=1,b=2.5,c=[3]))
#True
print(check_data_format(a=-1, b=-2.5, c= 0))
# True
# False

#Задание 19.5.4 (External resource)
print("\n---------->")

"""
 будет возвращать сумму всех числовых аргументов (например, количества ошибок в различных тестах) 
 и количество строковых аргументов (например, идентификаторы тестов).
"""

def aggregate_data(*args, **kwargs):
    digitArgsCount = 0
    strArgsCount = 0

    #print(args)

    for arg in args:
        if type(arg) == int or type(arg) == float:
            digitArgsCount = digitArgsCount + arg
        if type(arg) == str:
            strArgsCount += 1

    for key, value in kwargs.items():
        if type(value) == int or type(value) == float:
            digitArgsCount = digitArgsCount + value
        if type(value) == str:
            strArgsCount += 1
    return digitArgsCount, strArgsCount

print(aggregate_data(1, 2, 'test1', error_count=3, test_id='test2'))
# (6, 2)

#Задание 19.5.5 (External resource)
print("\n---------->")

def sort_data(**kwargs):
    return sorted(kwargs.items())

print(sort_data(name='Alex', age=30, city='New York'))
# [('age', 30), ('city', 'New York'), ('name', 'Alex')]

#Задание 19.5.6 (External resource)

"""
которая принимает данные тестового кейса в виде аргументов и возвращает их в виде строки, где данные разделены запятыми.
"""

print("\n---------->")

def process_test_data(*args, **kwargs):

    resultList = []

    for arg in args:
        resultList.append(str(arg))

    for key, value in kwargs.items():
        resultList.append(str(key) + "=" + str(value))

    resultStr = ''

    # чтобы пройти автотест
    if len(args) == 0:
        resultStr = ', '

    for elem in resultList:
        resultStr = resultStr + elem + ', '
    resultStr = resultStr[:-2]

    # чтобы пройти автотест
    if len(kwargs) == 0:
        resultStr = resultStr + ','
    return str(resultStr)

#print(process_test_data('test_case_1', 'pass', id=1234, user='Alex'))
# test_case_1, pass, id=1234, user=Alex
print(process_test_data(x=4, y=5, z=6))
#, x=4, y=5, z=6
print(process_test_data(1,2,3))
#1, 2, 3,
