#M4-2-L4
from dataclasses import asdict

#Задание 19.4.1 (External resource)
print("\n-------------------------------------------------->")

prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85
prices_in_euro = list(map(lambda x: x * exchange_rate, prices_in_usd))
print(prices_in_euro)

#Задание 19.4.2 (External resource)
print("\n-------------------------------------------------->")

phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
   result = list(filter(lambda x: x.isdigit(), number))
   #result = int(''.join(result))
   result = ''.join(result)
   #print(result)
   return result

formatted_numbers = list(map(format_phone_number, phone_numbers))
print(formatted_numbers)

#Задание 19.4.3 (External resource)
print("\n-------------------------------------------------->")

def filter_high_severity(bugs):
    result = list(filter(lambda x: x['severity']=='high', bugs))
    #print(result)
    return result

bugs = [
    {"id": 1, "description": "Баг №1", "severity": "low"},
    {"id": 2, "description": "Баг №2", "severity": "medium"},
    {"id": 3, "description": "Баг №3", "severity": "high"},
    {"id": 4, "description": "Баг №4", "severity": "high"},
]

filtered_bugs = filter_high_severity(bugs)
print(filtered_bugs)
# [{'id': 3, 'description': 'Баг №3', 'severity': 'high'}, {'id': 4, 'description': 'Баг №4', 'severity': 'high'}]

#Задание 19.4.4 (External resource) - Ошибка в задании
print("\n-------------------------------------------------->")

def filter_api_tests(test_case):
    #result = list(filter(lambda x: x['type'] == "UI" or x['type'] == "API",test_case))
    result = list(filter(lambda x: x['type'] == "API", test_case))
    #print(result)
    return result


test_cases = [
   {"id": 1, "description": "Тест №1", "type": "UI"},
   {"id": 2, "description": "Тест №2", "type": "API"},
   {"id": 3, "description": "Тест №3", "type": "API"},
   {"id": 4, "description": "Тест №4", "type": "Performance"},
]

filtered_test_cases = filter_api_tests(test_cases)
print(filtered_test_cases)
# [{'id': 2, 'description': 'Тест №2', 'type': 'API'}, {'id': 3, 'description': 'Тест №3', 'type': 'API'}

#Задание 19.4.5 (External resource)
print("\n-------------------------------------------------->")

def assign_tasks_to_engineers(engineers, tasks):
    result = list(zip(engineers, tasks))
    #print(result)
    return result

engineers = ["Анна", "Иван", "Елена", "Олег"]
tasks = ["Тестирование UI", "Тестирование API", "Написание тестовых сценариев"]

pairs = assign_tasks_to_engineers(engineers, tasks)
print(pairs)
# [('Анна', 'Тестирование UI'), ('Иван', 'Тестирование API'), ('Елена', 'Написание тестовых сценариев')]

#Задание 19.4.6 (External resource)
print("\n-------------------------------------------------->")
def compare_test_results(expected, actual):
    zipped = zip(expected, actual)
    result = []
    for a, b in zipped:
        if a == b:
            result.append(True)
        else:
            result.append(False)
    return result

expected_results = ["pass", "fail", "pass", "pass"]
actual_results = ["pass", "pass", "pass", "fail"]

comparison = compare_test_results(expected_results, actual_results)
print(comparison)
# [True, False, True, False]

#Задание 19.4.7 (External resource)
print("\n-------------------------------------------------->")


def has_failures(test_results):
    if any(x =='fail' for x in test_results):
        return True
    else:
        return False

def all_passed_or_skipped(test_results):
    if all(x =='pass' or x == 'skip' for x in test_results):
        return True
    else:
        return False



test_results = ["pass", "pass", "skip", "fail", "pass"]
print(has_failures(test_results))
# True
print(all_passed_or_skipped(test_results))
# False
