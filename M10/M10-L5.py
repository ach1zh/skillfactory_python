#M10-L5
#Задание 3.5.6
print("\n--> Задание 3.5.6 -->\n")

'''
Напишите контекстный менеджер, который умеет безопасно работать с файлами.
В конструктор объекта контекстного менеджера передаются два аргумента: первый — путь к файлу, 
который надо открыть, второй — тип открываемого файла (для записи, для чтения и т. д.).
При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
При выходе из контекстного менеджера файл должен закрываться. (Эталоном работы можно считать контекстный менеджер open).
'''
import os

class FileContextManager:
    
    def __init__(self, file_path, open_mode='tr', file_encoding='utf8'):        
        self.file = open(file_path, open_mode, encoding=file_encoding)

    # этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто верните этот объект через return
    def __enter__(self):        
        return self.file
    
    # этот метод срабатывает при выходе из контекстного менеджера
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

### main()

dir_path = 'C:\Temp'
file_name = 'python_test_file.txt'
file_path = os.path.join(dir_path, file_name)
file_open_mode = 'rt'
file_encoding = 'utf8'

with FileContextManager(file_path, file_open_mode, file_encoding) as input_file:    
    for line in input_file.readlines():
        print(line.strip())
