#M4-1-L6
funcs = [lambda *args : sum(args) / len(args), lambda x, y : x**y]
#print(funcs[0](15, 30, 24))
#print(funcs)
print(funcs[1](2, 8))


f1 = lambda x,y : x**y
#print(f1(2,2))

f2 = lambda *args : sum(args) / len(args)
#print(f2(2,3,4,5))

print("---------->")

test_reports = [
   {'name': 'test1', 'status': 'fail', 'time': 2.5, 'details': {'error': 'NullPointerException', 'attempt': 1}},
   {'name': 'test2', 'status': 'pass', 'time': 1.1, 'details': {'attempt': 1}},
   {'name': 'test3', 'status': 'fail', 'time': 3.1, 'details': {'error': 'AssertionError', 'attempt': 2}},
   {'name': 'test4', 'status': 'pass', 'time': 0.9, 'details': {'attempt': 1}}
]

#print(test_reports[0]['details']['error'])
#print(test_reports[0].get('details').get('error'))


def extract_data(reports, extraction_func):
   # Применяем переданную функцию к каждому словарю и генерируем новый список
   return [extraction_func(report) for report in reports]

execution_times = extract_data(test_reports, lambda x: x['time'])
print(execution_times)
# [2.5, 1.1, 3.1, 0.9]

attempt_counts = extract_data(test_reports, lambda x: x['details']['attempt'])
print(attempt_counts)
# [1, 1, 2, 1]


#Задание 19.6.1 (External resource)
print("\n---------->")
def sort_strings_by_last_char(strList):
    return sorted(strList, key=lambda x: x[-1])

strings = ["apple", "banana", "cherry", "date", "elderberry"]
print(sort_strings_by_last_char(strings))
# ['banana', 'apple', 'date', 'cherry', 'elderberry']

#Задание 19.6.2 (External resource)
print("\n---------->")

def apply_function(numbers,function):
    result = []
    for number in numbers:
        result.append(function(number))
    return result

numbers = [1, 2, 3, 4, 5]
print(apply_function(numbers, lambda x: x ** 2))
# [1, 4, 9, 16, 25]

#Задание 19.6.3 (External resource)
print("\n---------->>")

def sort_by_age(tupleList):
    return sorted(tupleList, key=lambda x: x[1])

people = [("Anna", 23), ("John", 21), ("Alice", 25)]
print(sort_by_age(people))

# [('John', 21), ('Anna', 23), ('Alice', 25)]
