#M10L3_HW337
"""
Должен содержать число Пи в виде константы 3.14, и две функции, 
которые будут считать площадь круга и прямоугольника.
"""

import math

# Константы
PI = 3.14159

# Функции
def add(a, b):
    """Сложение двух чисел."""
    return a + b

def subtract(a, b):
    """Вычитание одного числа из другого."""
    return a - b

def multiply(a, b):
    """Умножение двух чисел."""
    return a * b

def divide(a, b):
    """Деление одного числа на другое."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def area_circle(radius:int) -> float:
    return PI * radius**2

def area_square(side_a:int, side_b:int) -> int:
    return side_a * side_b

if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert area_circle(5) == 78.53975  # если ответы будут отличаться, то будет вызвана ошибка
   assert area_square(5, 4) == 20