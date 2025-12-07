#M3-L3

numbers_tuple = (1, 2, 3, 4, 5, 6)
numbers_list = [1, 2, 3, 4, 5, 6]

# определим размер с помощью .__sizeof__()
print(f'''Размер кортежа: {numbers_tuple.__sizeof__()} Размер списка: {numbers_list.__sizeof__()}''')

user = ('Michael', 'Scott', 40,) #'asdasd', 'asdasdasd', 99)

# разложим кортеж на отдельные переменные
name, surname, age = user
print(name)
print(surname)
print(age)

print("\n|>----------------\n")
#Итоговое задание M3-L3

#1
#2
tuple_family = ("Алексей Чижов", "Вероника Чижова", "Екатерина Чижова", "Никита Чижов", "Ирина Чижова")
#3
print(tuple_family[0],tuple_family[-1])
#4
print(tuple_family[::2])
#?
print(len(tuple_family))

print("\n|>----------------\n")
#5
numbers_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#number = int(input("Введите целое число: \n"))
number = 122
if number in numbers_set:
    print("True")
    numbers_set.remove(number)
else:
    numbers_set.add(number)
    print("False")
print(f"Длина множества: {len(numbers_set)}")
print(numbers_set)