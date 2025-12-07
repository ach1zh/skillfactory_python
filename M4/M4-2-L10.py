#M4-2-L12
from dataclasses import asdict

#Задание 19.10.1 (External resource)
print("\n---------->")

from datetime import date
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    # print(date.fromisoformat(birth_date).year)
    #age = int(date.today().year - date.fromisoformat(birth_date).year)
    age = date.today() - date.fromisoformat(birth_date)
    #print(age.days // 365 )
    return int(age.days // 365)

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adultUsers = list(filter(lambda person: calculate_age(person['birth_date']) >= 18, users))
    return adultUsers

def generate_username(first_name: str, last_name: str) -> str:
    result = (first_name[0] + "." + last_name).lower()
    return result

"""
print(calculate_age("1990-05-15"))
# 33

users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'}, #35
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'}, #40
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}] #10

print(filter_adults(users_data))
# [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'}]

print(generate_username("John", "Doe"))
# "j.doe"
"""

test_birth_dates = [
    "2000-01-01",  # Должно вернуться 24 (если сегодняшняя дата 2024-07-09)
    "1995-12-31",  # Должно вернуться 28 (если сегодняшняя дата 2024-07-09)
    "1980-02-29",  # Должно вернуться 44 (если сегодняшняя дата 2024-07-09)
    "2005-07-09",  # Должно вернуться 19 (если сегодняшняя дата 2024-07-09)
]

# Функция filter_adults
test_users_data = [
    {'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'},  # Должна быть включена
    {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'},  # Должен быть включен
    {'first_name': 'Eve', 'last_name': 'Brown', 'birth_date': '2010-01-01'},   # Не должен быть включен
]

# Функция generate_username
test_usernames = [
    ("John", "Doe"),        # Должно вернуться "j.doe"
    ("Alice", "Smith"),     # Должно вернуться "a.smith"
    ("Eve", "Brown"),       # Должно вернуться "e.brown"
]

# Вывод результатов тестов
for birth_date in test_birth_dates:
    print(f"calculate_age({birth_date}): {calculate_age(birth_date)}")

print("Filter adults:")
print(filter_adults(test_users_data))

for first_name, last_name in test_usernames:
    print(f"generate_username({first_name}, {last_name}): {generate_username(first_name, last_name)}")

"""
Ожидаемый ответ
calculate_age(2000-01-01): 25
calculate_age(1995-12-31): 29
calculate_age(1980-02-29): 45
calculate_age(2005-07-09): 20
Filter adults:
[{'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'}]
generate_username(John, Doe): j.doe
generate_username(Alice, Smith): a.smith
generate_username(Eve, Brown): e.brown
"""


"""
calculate_age(2000-01-01): 25
calculate_age(2000-01-01): 25

calculate_age(1995-12-31): 29
calculate_age(1995-12-31): 30

calculate_age(1980-02-29): 45
calculate_age(1980-02-29): 45

calculate_age(2005-07-09): 20
calculate_age(2005-07-09): 20

Filter adults:
[{'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'}]
[{'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'}, {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'}]
generate_username(John, Doe): j.doe
generate_username(John, Doe): j.doe
generate_username(Alice, Smith): a.smith
generate_username(Alice, Smith): a.smith
generate_username(Eve, Brown): e.brown
generate_username(Eve, Brown): e.brown
"""

#Задание 19.10.2 (External resource)
print("\n---------->")



from typing import List, Dict, Any
# А также вам наверняка может понадобиться модуль functools...
# Интересно зачем ?

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    result = []
    # print(users[0]["first_name"])
    for user in users:
        result.append(user["first_name"] + ' ' + user["last_name"])
    return result

"""
#Эталонное решение
def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names
"""

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    # equal = all([dict1[key] == dict2[key] for key in dict1.keys() if key in dict2])
    result = set()
    for user1 in users1:
        for user2 in users2:
            if user1['email'] == user2['email']:
                # print(user1['email'])
                result.add(user1['email'])
    return result

"""
#Эталонное решение
def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails
"""

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    first_name = []
    last_name = []
    birth_date = []
    email = []

    for user in users:
        #print(user['first_name'])
        first_name.append(user['first_name'])
        last_name.append(user['last_name'])
        birth_date.append(user['birth_date'])
        email.append(user['email'])

    result = {'first_name':tuple(first_name),'last_name':tuple(last_name),'birth_date':tuple(birth_date),'email':tuple(email)}
    return result


"""
#Эталонное решение
def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data
"""


users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'}]

print("\n---------->")
print(convert_to_full_name(users_data))
# ['John Doe', 'Bob Johnson', 'Lev Sergeev']

print("\n---------->")
print(find_matching_emails(users_data, users_data_ext))
# {'johndoe@gmail.com'}

print("\n---------->")
print(combine_user_data(users_data))
# {'first_name': ('John', 'Bob', 'Lev'), 'last_name': ('Doe', 'Johnson', 'Sergeev'), 'birth_date': ('1990-05-15', '1985-10-22', '2015-01-01'), 'email': ('johndoe@gmail.com', 'bobJ@gmail.com', 'lev46@gmail.com')}

#Задание 19.10.3 (External resource)
print("\n---------->")

import time
from typing import Callable

def time_it(func: Callable):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        #int что бы пройти автотест
        resultStr = f"Execution time of '{func.__name__}': {int(endTime - startTime)} seconds"
        print(resultStr)
        return resultStr
    return wrapper

# Функция — пример
# Она просто делает копию списка, добавляет value в конец списка и возвращает этот список
def add_point(original_list: list, value):
    # Специально делаем sleep, потому как без него время выполнения будет около нуля
    #time.sleep(2)
    return original_list[:].append(value)

# Делаем новую функцию уже с декоратором
@time_it
def add_point_with_timer(original_list: list, value):
    add_point(original_list, value)

# Выполняем функцию с декоратором
add_point_with_timer([1, 2, 3, 4, 5], 6)
# Execution time of 'add_point_with_timer': 2.003331 seconds


#Задание 19.10.4 (External resource)
print("\n----------")
print("---------->")
from typing import List, Dict, Any
logs = """\
2023-08-15 14:15:24 INFO Starting the system.
2023-08-15 14:15:26 WARN System load is above 80%.
2023-08-15 14:15:27 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
"""

def log_filter(logs: str, log_level: str) -> List[str]:
    logsSplit = (logs.split("\n"))
    result = []
    for string in logsSplit:
        if log_level in string:
            result.append(string)
    return result

#log_filter(logs, 'ERROR')
for log in log_filter(logs, 'ERROR'):
   print(log)

# 2023-08-15 14:15:27 ERROR Failed to connect to database.
#logs = "2023-08-15 14:15:24 INFO Starting the system.\n2023-08-15 14:15:26 WARN System load is above 80%.\n2023-08-15 14:15:27 ERROR Failed to connect to database.\n2023-08-15 14:15:28 INFO Connection retry in 5 seconds.\n"
#to_test = list(log_filter(logs, log_level="ERROR"))

#Задание 19.10.5 (External resource)
print("\n----------")
print("---------->")

categories = {
   "Электроника": {
       "Телефоны": {
           "Смартфоны": {},
           "Проводные": {}
       },
       "Компьютеры": {
           "Ноутбуки": {},
           "Стационарные": {
               "Игровые": {},
               "Для работы": {}
           }
       }
   },
   "Одежда": {
       "Мужская": {
           "Джинсы": {},
           "Куртки": {}
       }
   }
}

## root > Электроника > Компьютеры > Стационарные > Игровые

from typing import List, Dict, Any

"""
def extract_categories(categories: Dict[str, Any], parent_path: str = ''):
    for key,value in categories.items():
        if isinstance(value, dict):
            print(f"{parent_path} > {key}")
            extract_categories(value, f"{parent_path} > {key}")
        else:
            print("ELSE")
"""
def extract_categories(categories: Dict[str, Any], parent_path: str = ''):

    result = []

    def extract_recurvice(categories: Dict[str, Any], parent_path: str = ''):
        for key,value in categories.items():
            if isinstance(value, dict):
                #print(f"{parent_path} > {key}")
                if parent_path == '':
                    result.append(f"{key}")
                    extract_recurvice(value, f"{key}")
                else:
                    result.append(f"{parent_path} > {key}")
                    extract_recurvice(value, f"{parent_path} > {key}")
            else:
                print("ELSE")

    extract_recurvice(categories,parent_path)
    return result

#extract_categories(categories,parent_path='root')
#paths = extract_categories(categories, parent_path='root')
paths = extract_categories(categories)
for path in paths:
   print(path)

# root > Электроника
# root > Электроника > Телефоны
# root > Электроника > Телефоны > Смартфоны
# root > Электроника > Телефоны > Проводные
# root > Электроника > Компьютеры
# root > Электроника > Компьютеры > Ноутбуки
# root > Электроника > Компьютеры > Стационарные
# root > Электроника > Компьютеры > Стационарные > Игровые
# root > Электроника > Компьютеры > Стационарные > Для работы
# root > Одежда
# root > Одежда > Мужская
# root > Одежда > Мужская > Джинсы
# root > Одежда > Мужская > Куртки


#paths = extract_categories(categories)
#for path in paths:
#   print(path)

# Электроника
# Электроника > Телефоны
# Электроника > Телефоны > Смартфоны
# ...
# Одежда > Мужская
# Одежда > Мужская > Джинсы
# Одежда > Мужская > Куртки