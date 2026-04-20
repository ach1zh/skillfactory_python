#M19-L9

import numpy as np
import pandas as pd

#import
ratings_movies_data = pd.read_csv(r'M19\Data\ratings_movies\ratings_movies.csv', sep=',')

#copy
ratings_movies_data_df = ratings_movies_data.copy()

#Преобразуем Date в формат pandas.datetime
ratings_movies_data_df['date'] = pd.to_datetime(ratings_movies_data_df['date'])

'''
Для решения задач нам понадобится выделить из признака title год выпуска фильма. 
Для этого напишем функцию get_year_release(arg).
'''
#библиотека для регулярных выражений
import re 
def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

#----------#----------#----------#----------#----------#----------#----------#

#Задание 8.1
ratings_movies_data_df['year_release'] = ratings_movies_data_df['title'].apply(get_year_release)
#print(ratings_movies_data_df.info())
#print(100836-100818)

#Задание 8.2
f1 = ratings_movies_data_df['year_release'] == 1999
#print(ratings_movies_data_df[f1].groupby('title')['rating'].mean().sort_values())

#Задание 8.3
f1 = ratings_movies_data_df['year_release'] == 2010 
#print(ratings_movies_data_df[f1].groupby('genres')['rating'].mean().sort_values())

#Задание 8.4
#print(ratings_movies_data_df.groupby('userId')['genres'].agg('nunique').sort_values())

#Задание 8.5
#print(ratings_movies_data_df.groupby('userId')['rating'].agg(['count','mean']).sort_values(by=['count','mean']).head(30))


#Задание 8.6
f1 = ratings_movies_data_df['year_release'] == 2018
res = ratings_movies_data_df[f1].groupby('genres')['rating'].agg(['count','mean'])
f2 = res['count'] > 10
#print(res[f2].sort_values(by='mean'))
# or
#print(ratings_movies_data_df[f1].groupby('genres')['rating'].agg(['count','mean']).sort_values(by=['count','mean']).tail(30))

#Задание 8.7

ratings_movies_data_df['year_rating'] = ratings_movies_data_df['date'].dt.year
result_table1 = ratings_movies_data_df.groupby(['year_rating','genres'])['rating'].mean().unstack()
result_table2 = ratings_movies_data_df.groupby(['year_rating','genres'])['rating'].mean()


#A:TRUE
#print(result_table1['Action|Adventure'].sort_values())

#B:False
#print(result_table1['Action|Adventure|Animation|Children|Comedy|IMAX'].sort_values())

#C:TRUE
#print(result_table1['Animation|Children|Mystery'].sort_values())
#OR
#print(result_table2[2018].sort_values().tail(30))

#D: FALSE
#print(result_table1['Comedy'])

#А теперь поговорим о заказах в интернет-магазине.

#----------#----------#----------#----------#----------#----------#----------#
#import
orders_data = pd.read_csv(r'M19\Data\orders_and_products\orders.csv', sep=';')
products_data = pd.read_csv(r'M19\Data\orders_and_products\products.csv', sep=';')

#copy
orders_data_df = orders_data.copy()
products_data_df = products_data.copy()
orders_products = orders_data_df.merge(products_data_df,left_on='ID товара', right_on='Product_ID', how='left')

#----------#----------#----------#----------#----------#----------#----------#

#Задание 8.8
#print(orders_products)

#Задание 8.9
#print(orders_products)

#Задание 8.10
f1 = orders_products['Оплачен'] == 'Да'
orders_products['m'] = orders_products['Количество'] * orders_products['Price']
#print(orders_products[f1].sort_values(by='m'))
print(orders_products[f1].groupby('ID Покупателя')['m'].sum().sort_values())