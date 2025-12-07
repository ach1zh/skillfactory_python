#M4-2-L5

#Задание 19.5.3 (External resource)
print("\n--------------------------------------------->")

tests_run = 0
tests_failed = 0

def run_test(test):
    # Представим, что test — это функция, которая возвращает True, если тест прошёл, и False в противном случае
    global tests_run
    global tests_failed

    testF_result = test()

    if testF_result == True:
        tests_run += 1
    else:
        tests_failed += 1

#Задание 19.5.4 (External resource)
print("\n--------------------------------------------->")

def generate_test_case():
    case_id = 0

    def next_case():
        nonlocal case_id
        case_id += 1
        return case_id

    return next_case

#Задание 19.5.5 (External resource)
print("\n--------------------------------------------->")

tests_run = 0
tests_failed = 0

def test_case_generator():

    case_id = 0

    def run_test(test):
        # Ваш код здесь
        global tests_run
        global tests_failed
        nonlocal case_id

        case_id += 1

        testF_result = test()
        #print(testF_result)

        tests_run += 1

        if testF_result != True:
            tests_failed += 1

        return case_id
    return run_test


run_test = test_case_generator()

# Определение тестовых функций
def test1():
    return True  # Успешный тест

def test2():
    return False  # Провальный тест

def test3():
    return True  # Успешный тест

def test4():
    return False  # Провальный тест

def test5():
    return True  # Успешный тест

# Запуск тестов
print(run_test(test1))  # Ожидаемый вывод: 1
print(run_test(test2))  # Ожидаемый вывод: 2
print(run_test(test3))  # Ожидаемый вывод: 3
print(run_test(test4))  # Ожидаемый вывод: 4
print(run_test(test5))  # Ожидаемый вывод: 5

# Проверка глобальных переменных
print(f"Tests run: {tests_run}")       # Ожидаемый вывод: Tests run: 5
print(f"Tests failed: {tests_failed}") # Ожидаемый вывод: Tests failed: 2