#M10-L4

#Задание 3.4.3
print("\n--> Задание 3.4.3 -->\n")

'''
Сделайте функцию, которая принимает от пользователя путь и выводит всю информацию о содержимом этой папки. 
Для реализации используйте функцию встроенного модуля os.walk(). 
Если путь не указан, то сравнение начинается с текущей директории
'''
import os

def list_dir(dir_path:str = None) -> None:
    
    if(dir_path == None):
        dir_path = os.getcwd()

    #print(os.listdir(dir_path))
    #print(os.walk(dir_path))
    
    #v0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        print(dirpath)
        print(dirnames)
        print(filenames)
        print('-------------------------')

    print('==============================')
    
    #v1
    tree = list(os.walk(dir_path))
    print(tree)

    print('==============================')
    
    #v2 + join
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            print(os.path.join(dirpath, filename))

    print('==============================')

# Ответ из учебника
def walk_desc(path=None):
   start_path = path if path is not None else os.getcwd()

   for root, dirs, files in os.walk(start_path):
       print("Текущая директория", root)
       print("---")
      
       if dirs:
           print("Список папок", dirs)
       else:
           print("Папок нет")
       print("---")
      
       if files:
           print("Список файлов", files)
       else:
           print("Файлов нет")
       print("---")
      
       if files and dirs:
           print("Все пути:")
       for f in files:
           print("Файл ", os.path.join(root, f))
       for d in dirs:
           print("Папка ", os.path.join(root, d))
       print("===")

list_dir('C:\\Temp')
walk_desc('C:\\Temp')

#Задание 3.4.4
print("\n--> Задание 3.4.4 -->\n")
'''
Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
'''

dir_path = 'C:\Temp'
file_name = 'python_test_file.txt'
file_input_name = 'python_test_file_input.txt'
file_output_name = 'python_test_file_output.txt'
file_path = os.path.join(dir_path, file_name)
file_input_path = os.path.join(dir_path, file_input_name)
file_output_path = os.path.join(dir_path, file_output_name)

str1 = 'test string 1\n'
str2 = 'test string 2\n'

#write1
file = open(file_input_path, 'wt', encoding='utf8')
file.write(str1)
file.write(str2)
file.close

#read
file = open(file_input_path, 'rt', encoding='utf8')
#print(file.readlines())
for line in file.readlines():
    print(line.strip())
file.close


#read and write
file_i = open(file_input_path, 'rt', encoding='utf8')
file_o = open(file_output_path, 'wt', encoding='utf8')
for line in file_i.readlines():
    print(line.strip())
    file_o.write(line)
file_i.close
file_o.close

#read
file_o = open(file_output_path, 'rt', encoding='utf8')
#print(file.readlines())
for line in file.readlines():
    print(line.strip())
file_o.close

'''Ответ
with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in input_file:
           output_file.write(line)
'''


#Задание 3.4.5
print("\n--> Задание 3.4.5 -->\n")

'''
Дан файл numbers.txt, компоненты которого являются действительными числами
(файл создайте самостоятельно и заполните любыми числами,
в одной строке одно число). Найдите сумму наибольшего и наименьшего из значений 
и запишите результат в файл output.txt.
'''

dir_path = 'C:\Temp'
file_input_name = 'python_test_file_input_345.txt'
file_output_name = 'python_test_file_output_345.txt'
file_input_path = os.path.join(dir_path, file_input_name)
file_output_path = os.path.join(dir_path, file_output_name)

#write
with open(file_input_path, 'w') as input_file:    
    for i in range(1,11):
        input_file.write(str(i)+"\n")

#read and write
with open(file_input_path, 'rt') as input_file:
    #print(input_file.read())
    data = input_file.readlines()

data_int = list(map(lambda line: int(line.strip()), data))
#print(max(data_int))
#print(min(data_int))
with open(file_output_path, 'w') as output_file:
    output_file.write(str(max(data_int)+min(data_int)))

#read 
with open(file_output_path, 'rt') as output_file:
    print(output_file.read())
    
"""
Ответ из учебника
filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
   min_ = max_ = float(f.readline())  # считали первое число
   for line in f:
       num =  float(line)
       if num > max_:
           max_ = num
       elif num < min_:
           min_ = num

   sum_ = min_ + max_

with open(output, 'w') as f:
   f.write(str(sum_))
   f.write('\n')
"""

#Задание 3.4.6
print("\n--> Задание 3.4.6 -->\n")

'''
В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
Выведите на экран всех учащихся, чья оценка меньше 3 баллов. Cодержание файла:
'''

dir_path = 'C:\Temp'
file_input_name = 'python_test_file_input_346.txt'
file_input_path = os.path.join(dir_path, file_input_name)

with open(file_input_path, 'rt',encoding='utf-8') as input_file:
    #print(input_file.read())
    data = input_file.readlines()
    data_strip = list(map(lambda line: line.strip(), data))    

student_list = []
for line in data_strip:
    l_split = line.split(' ')
    student = {"surname": l_split[0], "name": l_split[1], "assessment": l_split[2]}
    student_list.append(student)

student_filter = list(filter(lambda student: int(student["assessment"]) > 3  ,student_list))
print(student_filter)

'''Ответ
with open('input.txt', encoding="utf8") as file:
    for line in file:
        points = int(line.split()[-1])
        if points < 3:
            name = " ".join(line.split()[:-1])
            print(name)
'''

#Задание 3.4.7
print("\n--> Задание 3.4.7 -->\n")

dir_path = 'C:\Temp'
file_input_name = 'python_test_file_input_345.txt'
file_input_path = os.path.join(dir_path, file_input_name)

with open(file_input_path, 'rt',encoding='utf-8') as input_file:
    #print(input_file.read())
    data = input_file.readlines()
    #data_strip = list(map(lambda line: line.strip(), data))
    print(list(reversed(data)))
    print(data[::-1])

'''Ответ
with open('input.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)
'''