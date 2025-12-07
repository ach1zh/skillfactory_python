#M4-1-L3
import string


#Задание 19.3.3 (External resource)

def is_success_code(code):
    if code >= 200 and code <= 299:
        return True
    else:
        return False

print(is_success_code(200))
print(is_success_code(404))

print("-------------->")
#Задание 19.3.4 (External resource)

def is_valid_email(email):

    dog = False
    dot = False
    space = True

    for char in email:
        if char == '@':
            dog = True
        if dog == True:
            if char == '.' and email.index('@') < email.index('.'):
                dot = True
        if char == ' ':
            space = False
    if dog and dot and space:
        return True
    else:
        return False

print(is_valid_email("user@example.com"))
print(is_valid_email("user at example dot com"))
print(is_valid_email("borya.gmail.com"))

#Задание 19.3.5 (External resource)
print("-------------->")

def square(n):
    return n ** 2

def test_function(function,arg1,arg2):
    result = function(arg1)
    if result == arg2:
        return True
    else:
        return False

# Пример функции для тестирования
print(test_function(square, 4, 16))  # Передаем имя функции
print(test_function(square, 5, 20))

# True
# False