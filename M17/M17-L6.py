#M17-L6
import numpy as np
import pandas as pd
#path_a = M17\data\melb_data.csv

melb_data = pd.read_csv('M17\data\melb_data.csv', sep=',')

#Задание 5.1
print(melb_data.iloc[15])

#Задание 5.2
print(melb_data.iloc[90].loc['Date'])

#Задание 5.3
print(melb_data.iloc[3521].loc['Landsize']/melb_data.iloc[1690].loc['Landsize'])