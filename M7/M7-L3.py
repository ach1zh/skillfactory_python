#M7-L3

some_var = None
some_var = (2,)
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))

a = None # пустая строка
b = a or 1
print(b)

print( 1 and "hello" and [False])

print(42 and 0 and '' and False)

print("---------->")

#Задание 5.3.6
print("\n---------->>")
# пусть a и b - переменные, которые мы хотим проверить
if a and b : # проверка истинности обеих переменных
    print("Обе переменные истинные")
    print(a,b)

a = ''
b = ""

#Задание 5.3.7
print("\n---------->>")
if a and b:
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print( a or b ) # печать значения одной переменной, которая является истинной
else:
    print("Обе переменные ложные")

#Задание 5.3.9
print("\n---------->>")
#a = input()
a = 4

if type(a) == int:    
    if a in range(100,999):
        if a % 2 == 0 and a % 3 == 0:
            print("Число удовлетворяет условиям")


if type(a) == int and a in range(100,999) and a % 2 == 0 and a % 3 == 0:
    print("Число удовлетворяет условиям")

if all([type(a) == int,
    100 <= a <= 999,
    a % 2 == 0,
    a % 3 == 0]):
    print("Число удовлетворяет условиям")

print("---------->")

nums = 1,2,3,0
resFlag = True
for n in nums:
   if n == 0:
       resFlag = False

print(resFlag) 

#a = input()
#a = 13
#L = list(map(int, input().split()))
#print(all(L))

#Задание 5.3.12
print("\n---------->>")
numbers = [0, 1, 2, 3, 0]

print(any(i == 0 for i in numbers))
print(any(list(i == 0 for i in numbers)))

#Задание 5.3.13
print("\n---------->>")
list_tuples = [(i, i**2) for i in range(1,11)]
M = [[i+j for j in range(5)] for i in range(5)]

mTable = [ [(i,j,j*i)  for j in range(1,10)] for i in range(1,10) ]
#Ответ из курса
T = [[i*j for j in range(1,11)] for i in range(1,11)]

print(mTable)
print("\n")
print(T)

#Задание 5.3.14
print("\n---------->>")

#L = [int(input()) for i in range(3)]
#L1 = [int(input()) for i in range(3) if int(input()) % 2 == 0 ]
#L2 = [int(input()) % 2 == 0 for i in range(3)]

#print(L1)
#print(L2)

#Задание 5.3.15
print("\n---------->>")
#L = [int(input()) % 2 == 0 for i in range(5)]
#print(any(L))
#Задание 5.3.16
#any(L) and not all(L)


#Задание 5.3.17
print("\n---------->>")
L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
R = [ a*b for a, b in zip (L,M) ]
print(R)

#Задание 5.3.18
print("\n---------->>")

"""
Необходимо вывести строку, где каждая последовательность из одинаковых символов, идущих подряд, 
заменяется на один символ, и длину этой последовательности (включая последовательности единичной длины). 
Вывод должен выглядеть так
a3b2c4d1a2
"""
symbols = 'aaabbccccdaa'


#v1
result = ''
count = 1
lastSymbol = ''
lenCount = len(symbols)

for s in symbols:    
    if lastSymbol == s:
        count += 1
    else:
        if lastSymbol != '':
            result += lastSymbol + str(count)
            count = 1    
    lastSymbol = s
    lenCount -= 1
    if lenCount == 0:
        result += lastSymbol + str(count)

print(result)
print("a3b2c4d1a2")