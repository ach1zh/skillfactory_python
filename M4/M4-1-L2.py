#M4-1-L2

#def count_elements(input_list):
   #print('Считаю элементы в {}'.format(input_list)) # Используем полученный input_list

#list1 = [1, 2, 3, 2, 1]
#count_elements(list1) # Передаем функции аргумент

# Считаю элементы в [1, 2, 3, 2, 1]

#print('{}'.format(list1))

#print_copy = print

#Задание 19.2.5 (External resource)

def check_password(pass_str):

    pass_len = False
    if len(pass_str) >= 8:
        pass_len = True
    else:
        print("Пароль должен быть не менее 8 символов")

    pass_UPcase = False
    for char in pass_str:
        if char.isupper():
            pass_UPcase = True
            break
    else:
        print("Пароль должен содержать хотя бы одну заглавную букву")

    pass_LOWcase = False
    for char in pass_str:
        if char.islower():
            pass_LOWcase = True
            break
    else:
        print("Пароль должен содержать хотя бы одну строчную букву")

    pass_number = False
    for char in pass_str:
        if char.isnumeric():
            pass_number = True
            break
    else:
        print("Пароль должен содержать хотя бы одну цифру")

    if pass_len and pass_UPcase and pass_LOWcase and pass_number:
        print("Условия соблюдены")

#check_password("_")
# Пароль должен быть не менее 8 символов
# Пароль должен содержать хотя бы одну заглавную букву
# Пароль должен содержать хотя бы одну строчную букву
# Пароль должен содержать хотя бы одну цифру

#check_password("password")
# Пароль должен содержать хотя бы одну заглавную букву
# Пароль должен содержать хотя бы одну цифру

#Условия соблюдены
#check_password("Password1")
#

#Задание 19.2.6 (External resource)

def test_range(number,r1,r2):
    if (number >= r1 and number <= r2) == False:
        print(f"Число {number} не попадает в диапазон между {r1} и {r2}")

test_range(15, 1, 10)
test_range(5, 1, 10)
