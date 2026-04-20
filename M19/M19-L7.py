#M19-L7

import numpy as np
import pandas as pd

#import
m_data_dates = pd.read_csv(r'M19\Data\movies_data\dates.csv', sep=',')
m_data_movies = pd.read_csv(r'M19\Data\movies_data\movies.csv', sep=',')
m_data_ratings1 = pd.read_csv(r'M19\Data\movies_data\ratings1.csv', sep=',')
m_data_ratings2 = pd.read_csv(r'M19\Data\movies_data\ratings2.csv', sep=',')

#copy
m_data_dates_df = m_data_dates.copy()
m_data_movies_df = m_data_movies.copy()
m_data_ratings1_df = m_data_ratings1.copy()
m_data_ratings2_df = m_data_ratings2.copy()

#Преобразуем Date в формат pandas.datetime
m_data_dates_df['date'] = pd.to_datetime(m_data_dates_df['date'])

#----------#----------#----------#----------#----------#----------#----------#

#Задание 6.3 (External resource)

'''
В ваше распоряжение предоставлена директория users ('./Root/users'). В данной директории содержатся csv-файлы, в каждом из которых хранится информация об идентификаторах пользователей (user_id) и ссылках на их фотографии (image_url). Количество файлов в директории может быть любым.

Вам необходимо написать функцию concat_user_files(path), параметром которой является path — путь до директории.

Функция должна:

Объединить информацию из всех csv-файлов в единый DataFrame.
Удалить дубликаты.
Обновить индексы результирующей таблицы.
Отсортировать пользователей по числовой части user_id (игнорируя буквенную часть).
Например, если в директории users есть несколько csv-файлов, то результирующая таблица должна выглядеть так:
'''
# Введите свое решение ниже

import numpy as np
import pandas as pd
import glob

def concat_user_files(path):
    # Получаем список всех CSV-файлов в указанной директории
    p = f"{path}/*.csv"
    files = glob.glob(p)

    result_df = pd.DataFrame()
    for filename in files:
        df = pd.read_csv(filename)
        result_df = pd.concat([result_df, df],axis=0, ignore_index=True)
    result_df = result_df.drop_duplicates(ignore_index=True)
    # Нормальный вариант не заработал. Тестить не удобно.
    '''
    l = ['A1', 'A10', 'A3', 'A2', 'A11', 'A12', 'B1', 'B2', 'B3']
    sorted(l,key = lambda x: (x[0],int(x[1:])))
    '''
    #result_df = result_df.sort_values(by='user_id',key=(lambda x: x.str.split('id')[1]).astype(int))    
    #Делаем через создание доп столбца
    result_df['sort_key'] = result_df['user_id'].str.extract('(\d+)').astype(int) 
    result_df = result_df.sort_values('sort_key',ignore_index=True).drop('sort_key', axis=1)
    
    return result_df

#print(concat_user_files(path = './Root/users'))
#Ответ в курсе кривой, задачу не решает.

'''
def concat_users_files(path):
    data = pd.DataFrame()
    file_names = os.listdir(path)
    file_names.sort()
    for file in file_names:
        tmp_data = pd.read_csv(path + '/' + file)
        data = pd.concat([data, tmp_data], axis=0, ignore_index=True)
    data = data.drop_duplicates()
    return data
'''
'''
import numpy as np
import pandas as pd
import glob

def concat_user_files(path):
    # Получаем список всех CSV-файлов в указанной директории
    p = f"{path}/*.csv"
    files = glob.glob(p)

    result_df = pd.DataFrame()
    for filename in files:
        df = pd.read_csv(filename)
        result_df = pd.concat([result_df, df], ignore_index=True)
    result_df = result_df.drop_duplicates(ignore_index=True)
    result_df = result_df.sort_values(by='user_id')

    return result_df

'''


"""
Ожидаемый ответ:

user_id                          image_url
0   id001   http://example.com/img/id001.png
1   id002   http://example.com/img/id002.jpg
2   id003   http://example.com/img/id003.bmp
3   id004   http://example.com/img/id004.jpg
4   id005   http://example.com/img/id005.png
5   id006   http://example.com/img/id006.png
6   id007   http://example.com/img/id007.png
7   id008   http://example.com/img/id008.png
8   id009   http://example.com/img/id009.png
9  id0010  http://example.com/img/id0010.png

Ваш ответ:

user_id                          image_url
0   id001   http://example.com/img/id001.png
7  id0010  http://example.com/img/id0010.png
1   id002   http://example.com/img/id002.jpg
2   id003   http://example.com/img/id003.bmp
3   id004   http://example.com/img/id004.jpg
4   id005   http://example.com/img/id005.png
5   id006   http://example.com/img/id006.png
8   id007   http://example.com/img/id007.png
9   id008   http://example.com/img/id008.png
6   id009   http://example.com/img/id009.png



###

Ожидаемый ответ:

user_id                          image_url
0   id001   http://example.com/img/id001.png
1   id002   http://example.com/img/id002.jpg
2   id003   http://example.com/img/id003.bmp
3   id004   http://example.com/img/id004.jpg
4   id005   http://example.com/img/id005.png
5   id006   http://example.com/img/id006.png
6   id007   http://example.com/img/id007.png
7   id008   http://example.com/img/id008.png
8   id009   http://example.com/img/id009.png
9  id0010  http://example.com/img/id0010.png

Ваш ответ:

user_id                          image_url
0   id001   http://example.com/img/id001.png
7  id0010  http://example.com/img/id0010.png
1   id002   http://example.com/img/id002.jpg
2   id003   http://example.com/img/id003.bmp
3   id004   http://example.com/img/id004.jpg
4   id005   http://example.com/img/id005.png
5   id006   http://example.com/img/id006.png
8   id007   http://example.com/img/id007.png
9   id008   http://example.com/img/id008.png
6   id009   http://example.com/img/id009.png
 

"""