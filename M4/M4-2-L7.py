#M4-2-L7
from dataclasses import asdict

#Задание 19.7.5 (External resource)
print("\n-------------------------------------------------->")


import time

def time_it(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() - start_time
        print(f'Function {func.__name__} took {int(work_time)} seconds to run')
        #print(f'args: {args}')
        #print(f'kwargs: {kwargs}')
        return res

    return wrapper


@time_it
def test_function():
    time.sleep(2)

test_function()
# Function test_function took 2 seconds to run





#Задание 19.7.6 (External resource)
print("\n-------------------------------------------------->")

import random

def retry_if_result_is_none(times=1):

    def decorator(func):

        def wrapper(*args, **kwargs):
            stopFlag = times
            while stopFlag > 0:
                res = func()
                if res:
                    return res
                else:
                    stopFlag -= 1
                    if stopFlag == 0:
                        return None
        return wrapper

    return decorator

@retry_if_result_is_none(times=2)
def test_function():
    return random.choice([None, "Passed"])

# Получилось получить значение за 2 вызова
print(test_function())
# Passed

# Не получилось получить значение за 2 вызова
print(test_function())
# None

#Задание 19.7.7 (External resource)
print("\n-------------------------------------------------->")

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function {func.__name__} raised an exception: {e}")
    return wrapper

@handle_exceptions
def test_function():
    raise ValueError("Some value error")

test_function()
# Function test_function raised an exception: Some value error





#Задание 19.7.8 (External resource)
print("\n-------------------------------------------------->")

import random
def ensure_result_is_number(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) == int or type(res) == float:
            return res
        else:
            return None
    return wrapper


@ensure_result_is_number
def test_function():
    return random.choice(["Passed", 10, "Failed", 5.5])

# Функция вернула не int и не float
print(test_function())
# None

# Функция вернула float
print(test_function())
# 5.5

# Функция вернула int
print(test_function())
# 10
