#M17-L8

import numpy as np
import pandas as pd

melb_data = pd.read_csv('M17\data\melb_data.csv', sep=',')

#Задание 7.2
print(melb_data['Propertycount'].max())

#Задание 7.3
print(melb_data['Distance'].std())

#Задание 7.4
"""
Чему равно отклонение (в процентах) медианного значения площади здания от его среднего значения?
"""
building_area_median = melb_data['BuildingArea'].median() 
building_area_mean =  melb_data['BuildingArea'].mean()
print((abs(building_area_median - building_area_mean)/building_area_mean)*100)

#Задание 7.5
#[1, 2, 4, 2, 3, 2, 1, 5, 6]
...

#Задание 7.6
print(melb_data['Bedroom'].mode())