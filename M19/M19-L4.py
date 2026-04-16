#M19-L4

import numpy as np
import pandas as pd

#import
melb_data = pd.read_csv('M19\Data\melb_data_fe.csv', sep=',') #home

#copy
melb_df = melb_data.copy()

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date']) #~~dayfirst=True~~

#----------#----------#----------#----------#----------#

#Задание 3.1
print(melb_df.groupby(by='Rooms')['Price'].mean().sort_values())

#Задание 3.2
print(melb_df.groupby('Regionname')['Lattitude'].std().sort_values())

#Задание 3.3
#print(melb_df['Price'].shape[0])
#print(pd.to_datetime('2017-05-01'))
#print(melb_df['Date'])

#Не работает. Что бы работало, можно делать как в ответе:
#f1 = pd.to_datetime('2017-05-01') < melb_df['Date'] > pd.to_datetime('2017-09-01')

'''
Ответ:
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_df['Date']) & (melb_df['Date']<= date2)
melb_df[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True)
'''

f1 =melb_df['Date'].between('2017-05-01','2017-09-01')
#print(melb_df[f1]['Price'].shape[0])

#Ответ
print(melb_df[f1].groupby(by='SellerG')['Price'].sum().sort_values())