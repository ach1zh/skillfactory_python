#M4-2-L2

#def recursive_func(n=0):
#   print('Вывод до запуска рекурсии: ', n)
#   if n < 3:
#       recursive_func(n + 1)
#   print('Вывод после запуска рекурсии: ', n)

#recursive_func()

def myRecursiveFunc(n):
   if n == 0:
       return 1
   else:
       return n * myRecursiveFunc(n-1)

print(myRecursiveFunc(11))


#--------------------------------------------


#Задание 19.2.4 (External resource)
print("\n---------------------------------------->")

def fibonacci(n):
    #print(f"Начало функции:{n}")
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

"""
4
        3   2
     2   1    1  0
"""
print(fibonacci(4))

#Задание 19.2.5 (External resource)
print("\n---------------------------------------->")
def is_palindrome(check_str):
    #Базовое условие
    if len(check_str) <=1:
        return True
    # Рекурсивное условие
    if check_str[0] != check_str[-1]:
        return False
    else:
        #Что бы в дебаггере было видно значение
        result = is_palindrome(check_str[1:-1])
        return result


print(is_palindrome('anYna'))
#print(is_palindrome('racecar'))
#print(is_palindrome('raYecarg'))
# True
#print(is_palindrome('gong'))
# False


#Задание 19.2.6 (External resource)
print("\n---------------------------------------->")
print("\n---------------------------------------->")

"""
Бинарный поиск 
1.Определите средний элемент отсортированного списка.
2.Если средний элемент является искомым значением, то поиск завершён.
3.Если искомое значение меньше среднего элемента, повторите поиск в левой половине списка.
4.Если искомое значение больше среднего элемента, повторите поиск в правой половине списка.
5.Если список пуст (то есть начальная позиция больше конечной), значит, искомого элемента в списке нет.

Функция должна возвращать True, если такой элемент есть в списке, и False — если его нет.
"""

def binary_search(numbersList, x):
    if numbersList[0] > numbersList[-1] or len(numbersList) <= 1:
        return False
    mid = len(numbersList) // 2
    if numbersList[mid] == x:
        return True
    elif numbersList[mid] > x:
        return binary_search(numbersList[:mid], x)
    else:
        return binary_search(numbersList[mid:], x)

#print(binary_search([4, 5, 6, 7, 8, 9, 10], 12))
print(binary_search([4, 5],4))
#print(binary_search([4,5,6,7],7))
#print(binary_search([4, 5],5))
#print(binary_search([1, 2, 3, 4, 5], 4))
# True
#print(binary_search([1, 2, 3, 4, 5], 6))
# False

"""
##### Первое неверное решение ##### 
def binary_search(elemList, x):

        if elemList[0] > elemList[-1]:
            return False


        if (len(elemList)) <= 0:
            return False

        #Рекурсивное условие

        midl_element = 0
        if len(elemList) % 2 == 0:
            midl_element = (len(elemList) // 2) - 1
        else:
            midl_element = (len(elemList) // 2)

        if len(elemList) == 2:
            if x in elemList:
                return True
            #else: return False

        if elemList[midl_element] == x:
            return True
        else:
            if x < midl_element:
                return binary_search(elemList[:midl_element], x)
            else:
                return binary_search(elemList[midl_element:], x)

"""

