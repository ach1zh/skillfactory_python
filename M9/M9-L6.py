#M9-L6

#Задание 21.11.1 (External resource)
print("\n--> Задание 21.11.1 (External resource) -->\n")

class Model:
    
    NAME_MIN_LEN = 3
    NAME_MAX_LEN = 15

    def __init__(self):
        self.__name = None

    @classmethod
    def __validate_name(cls,name):        
        if not (cls.NAME_MIN_LEN <= len(name) <= cls.NAME_MAX_LEN):
            #raise AttributeError('Name not valid')
            return False
        else:
            return True

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if self.__validate_name(name):            
            self.__name = name

###>

# Создаем экземпляр класса Model
m = Model()

# Проверяем начальное значение имени модели (должно быть None)
print(m.name) 
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "AB"
print(m.name) 
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "A" * 16
print(m.name) 
# Выведет: None

# Устанавливаем корректное значение имени
#m.name = "ValidModelName"
m.name = "ValidName"
print(m.name) 
# Выведет: ValidModelName





#Задание 21.11.2 (External resource)
print("\n--> Задание 21.11.2 (External resource) -->\n")

'''
геттер и сеттер свойства radius, реализованные через декораторы @property и @radius.setter.
В сеттере свойства radius должна происходить проверка на то, что значение больше нуля, 
иначе должна вызываться ошибка ValueError("Radius cannot be negative").

Также добавьте геттер (также через декоратор) с именем area, который возвращает площадь круга. 
Напомним, площадь рассчитывается по формуле: S = pi*r^2 == S = 3.14*r^2
В качестве числа возьмите значение 3.14.

Также добавьте геттер (также через декоратор) с именем diameter, который возвращает диаметр круга (удвоенный радиус):
d = 2r
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @classmethod
    def __validate_radius(cls, radius):
        if not radius > 0:
            raise AttributeError('Radius cannot be negative')    

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):        
        self.__validate_radius(radius)
        self._radius = radius
    
    @property
    def area(self):        
        return 3.14 * self.radius**2
    
    @property
    def diameter(self):        
        return 2*self.radius

###>

# Создадим экземпляр класса Circle с радиусом 5
circle_1 = Circle(5)
print(f"Радиус круга: {circle_1.radius}")
print(f"Площадь круга: {circle_1.area}")
print(f"Диаметр круга: {circle_1.diameter}")


# Изменим радиус круга на 10
circle_1.radius = 10
print(f"Площадь круга после изменения радиуса: {circle_1.area}")
print(f"Диаметр круга после изменения радиуса: {circle_1.diameter}")


# Попробуем установить отрицательный радиус
try:
    circle_1.radius = -5
except ValueError as ve:
    print(ve)


# Радиус круга: 5
# Площадь круга: 78.5
# Диаметр круга: 10
# Площадь круга после изменения радиуса: 314.0
# Диаметр круга после изменения радиуса: 20
# Radius cannot be negative


# Создадим экземпляр класса Circle с радиусом 15 для другого проекта
circle_2 = Circle(15)
print(f"Радиус другого круга: {circle_2.radius}")
print(f"Площадь другого круга: {circle_2.area}")
print(f"Диаметр другого круга: {circle_2.diameter}")


# Радиус другого круга: 15
# Площадь другого круга: 706.5
# Диаметр другого круга: 30
