#M10-L2

#Задание 3.2.5
print("\n--> Задание 3.2.5 -->\n")

"""
Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException, 
унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.
"""

class NonPositiveDigitException(ValueError):
    print("!!! NonPositiveDigitException !!!")
    #pass

class Square:
    def __init__(self,a):        
        try:
            if a <= 0:
                print("aaa")                
                raise NonPositiveDigitException('!!Exception!!')
            
            s = a**2
        
        except NonPositiveDigitException as ex:
            print(ex)

""" Эталон решения
class NonPositiveDigitException(ValueError):
    pass
 
class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указана сторона квадрата')
"""