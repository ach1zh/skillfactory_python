#M7-L5

#Задание 5.5.1
L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(lambda x: x.lower(), L)))
#Ответ из учебника
print(list(map(str.lower, L)))

#Задание 5.5.2

# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False
result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

L2 = [-2, -1, 0, 1, -3, 2, -3]
print(list(filter(lambda x: x>0 ,L2)))
print(list(filter(lambda x: x%2==0 ,L2)))


#M7-L5 TEMP

#Задание 5.5.3

# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]
#print(data[0][0])
print(sorted(data, key=lambda x: x[0]/x[1]**2))

#Задание 5.5.4
'''
Из списка в предыдущем задании найти кортеж с минимальным индексом массы тела.
'''
print(min(data, key=lambda x: x[0]/x[1]**2))

#Задание 5.5.5
a = ["asd", "bbd", "ddfa", "mcsa"]

#print(list(map(lambda x: len(x),a)))
#Что бы ответ прокатил в вебе нужен ебучий пробел в начале !
print(  list(map(len,a))  )

#map(lambda x: len(x),a)

#Задание 5.5.6
a = ["это", "маленький", "текст", "обидно"]
print( list(map(str.upper, a)) )