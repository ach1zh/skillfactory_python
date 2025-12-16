#M7-L4

#def linear_solve(a, b):
#    return b / a

#Задание 5.4.2

# 0*x = 1
#print(linear_solve(0,1))

"""
# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня
"""


#Задание 5.4.3


#quadratic_equation
def calcD(a,b,c):
    D = b**2 - 4*a*c
    return D

def checkD(D):
    if D < 0:
        return "Нет вещественных корней"

    
#M = {'a': 1,
#     'b': 0,
#     'c': -1}
#
#print(**M)


#Задание 5.4.9

'''
Напишите рекурсивную функцию, находящую минимальный элемент списка без использования циклов и встроенной функции min().
'''

list_data = [1,2,3,4,5,"aaa","bbb"]
list_data = [10,2,3,4,5]

# Не правильно понял задание
def r_get_min_elem(list_data, i=0):
    
    if len(list_data) == i:
        return list_data[i-1]
    else:
        return r_get_min_elem(list_data,i+1)
print(r_get_min_elem(list_data))

L = [1,2,3]

def recursionF2(L):
    #В базовом случае, когда список содержит только один элемент, возвращается этот элемент
    if len(L) == 1:
        return L[0]
    #В рекурсивном случае
    else:
        #Сравнивается первый элемент списка с минимальным элементом из оставшейся части списка
        print(recursionF2(L[:1]))
        if recursionF2(L[:1]) < recursionF2(L[1:]):
            return L[0]
        else:
            #Функция вызывается рекурсивно для оставшейся части списка (без первого элемента)
            return recursionF2(L[1:])

print(recursionF2(L))
print("----->>\n")

#Задание 5.4.10
'''
Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.
'''
num = "12345"
#print(num[:-1])
def recursionF3(num):
    #print(num[-1])
    
    if len(num) == 1:        
        return num[0]
    else:
        return recursionF3(num[:-1])
print(recursionF3(num))

print("----->>\n")
a = 12345
#print(a // 10)
#print(a % 10)

def mirror(a, res=0):
    print(f"a // 10 = {a // 10}")
    print(f"res*10 = {res*10}")
    print(f"a%10 = {a % 10}")
    print(f"res_result = {res*10 + a % 10}")
    print("---")
    
    return mirror(a // 10, res*10 + a % 10) if a else res 

print(mirror(a))

#Задание 5.4.11

"""
Сейчас попробуем реализовать функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N с числом S. 
При написании программы следует обратить внимание на то, что, если S стала отрицательной, то необходимо сразу вернуть False.
"""
#v1
'''
def equal(N, S):
    if S < 0:
        return False
    else:
        if N < 10:
            return N
        else:            
            result = equal( N//10 ,S) + N % 10
            #return result
            return True if result == S else result
'''

#v2 решение из курса, сам не решил
def equal(N, S):
    
    #print(f">{N}")

    if S < 0:
        return False
    
    if N < 10:
        #print(f">>{N}")
        return N == S
    res = equal( N//10 , S - N % 10)
    return res

N = 179
S = 6

print(equal(N,S))

#Задание 5.4.13
print("---------->>\n")

'''
#v1
def e(n):
    e_n = (1 + 1/n)**n
    yield e_n
'''

#v2
def e():
    n = 1    
    while True:
        yield (1 + 1 / n) ** n
        n += 1

last = 0

for a in e(): # e() - генератор
    #print(a)
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение 
#print(last)


iter_obj = iter("Hello!")
print(next(iter_obj))
print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))
#print(next(iter_obj))

#Задание 5.4.15
print("---------->>\n")

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться, или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

def has_access(func):
    def wrapper():
        if username in USERS:
            print(f"Доступ пользователю {username} разрешен")
            func()
        else:
            print(f"Доступ пользователю {username} запрещен !")
    return wrapper                

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()