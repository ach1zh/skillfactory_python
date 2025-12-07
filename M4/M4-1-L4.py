# M4-1-L4

def create_start_list(start_value, lst=[]):
    lst.append(start_value)
    return lst


l1 = create_start_list(1)
# print(l1)

l2 = create_start_list(2)
# print(l2)

"""
В объявлении функции параметр lst ссылается на объект — пустой список, и ссылка эта за время работы программы никуда не исчезала. При первом вызове функции мы добавили объект в список, на который ссылался параметр lst и вернули его. При втором вызове функции lst по-прежнему ссылается на тот же самый список, который уже не пустой, добавляет в него значение и возвращает его нам.
"""


# Задание 19.4.3 (External resource)


def is_valid_password(pass_str, min_length=8, require_upper=True, require_lower=True, require_digit=True):
    pass_len = False
    if len(pass_str) >= min_length:
        pass_len = True
    # else:
    # print(f"Пароль должен быть не менее {min_length} символов")
    # pass_len = False

    pass_UPcase = False
    if require_upper:
        for char in pass_str:
            if char.isupper():
                pass_UPcase = True
                break
    else:
        # print("Пароль должен содержать хотя бы одну заглавную букву")
        pass_UPcase = True

    if require_lower:
        pass_LOWcase = False
        for char in pass_str:
            if char.islower():
                pass_LOWcase = True
                break
    else:
        # print("Пароль должен содержать хотя бы одну строчную букву")
        pass_LOWcase = True

    pass_number = False
    if require_digit:
        for char in pass_str:
            if char.isnumeric():
                pass_number = True
                break
    else:
        # print("Пароль должен содержать хотя бы одну цифру")
        pass_number = True

    if pass_len and pass_UPcase and pass_LOWcase and pass_number:
        # print("Условия соблюдены")
        return True
    else:
        return False


print(is_valid_password("Password123"))
# True
print(is_valid_password("password"))
# False
print(is_valid_password("Password123", min_length=12))
# False

print("---------->")

# Задание 19.4.4 (External resource)
import random


def generate_test_data(n=5, min_value=1, max_value=10):
    lst = []
    lst = [random.randint(min_value, max_value) for _ in range(n)]
    return lst


print(generate_test_data())
# [6, 6, 5, 10, 10]

print(generate_test_data(n=3, min_value=-5, max_value=5))
# [3, 4, 3]

print("\n---------->")

# Задание 19.4.5 (External resource)
# гггг-мм-дд
from datetime import datetime


def format_date(date_str, dFormat_in="%Y-%m-%d", format='dmy'):
    date_object = datetime.strptime(date_str, dFormat_in).date()

    if format == "dmy":
        date_object = date_object.strftime("%d%m%Y")
    if format == "mdy":
        date_object = date_object.strftime("%m%d%Y")
    if format == "ymd":
        date_object = date_object.strftime("%Y%m%d")

    return date_object


print(format_date("2023-07-01"))
# 01072023
print(format_date("2023-07-01", format="dmy"))
# 01072023
print(format_date("2023-07-01", format="mdy"))
# 07012023
print(format_date("2023-07-01", format="ymd"))
# 20230701

print("\n---------->")


# Задание 19.4.6 (External resource)

def compare_lists(list1, list2, ignore_case=False):
    resultList = []

    for i in list1:
        inFlag = False
        for j in list2:
            if ignore_case:
                if i.lower() == j.lower():
                    inFlag = True
                    # break
            else:
                if i == j:
                    inFlag = True
                    # break
        if inFlag == False:
            resultList.append(i)

    return resultList


print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"]))
# ["apple", "banana"]
print(compare_lists(["apple", "banana", "cherry"], ["Banana", "cherry", "date"], ignore_case=True))
# ["apple"]