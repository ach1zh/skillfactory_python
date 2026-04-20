#M19-L5 notebook

import numpy as np
import pandas as pd

#import
melb_data = pd.read_csv('M19\Data\melb_data_fe.csv', sep=',') #home

#copy
melb_df = melb_data.copy()

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date'])

#----------#----------#----------#----------#----------#----------#----------#

#Задание 4.2
"""
Составьте сводную таблицу, которая показывает зависимость медианной площади (BuildingArea) здания
от типа объекта недвижимости (Type) и количества жилых комнат в доме (Rooms). 
Для какой комбинации признаков площадь здания наибольшая?
В качестве ответа запишите эту комбинацию (тип здания, число комнат) через запятую, без пробелов.
"""
res = melb_df.pivot_table(
    values='BuildingArea',
    index=['Type',],
    columns='Rooms',
    aggfunc='median',
    fill_value=0
)

#print(res)

#Задание 4.3
"""
Составьте сводную таблицу, которая показывает зависимость медианной цены объекта недвижимости (Price)
 от риелторского агентства (SellerG) и типа здания (Type).
Во вновь созданной таблице найдите агентство, у которого медианная цена для зданий типа unit максимальна.
В качестве ответа запишите название этого агентства.
"""

res2 = melb_df.pivot_table(
    values='Price',
    index=['SellerG',],
    columns='Type',
    aggfunc='median',
    fill_value=0
)

print(res2['unit'].sort_values())