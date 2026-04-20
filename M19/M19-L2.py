#M19-L2

import numpy as np
import pandas as pd

#import
melb_data = pd.read_csv('M19\Data\melb_data_fe.csv', sep=',') #home

#copy
melb_df = melb_data.copy()

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date']) #~~dayfirst=True~~

#----------#----------#----------#----------#----------#

#Задание 1.1
print(melb_df['Date'].dt.quarter.value_counts())
#2    4359

#Задание 1.2

cols_to_exclude  = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150

for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')

print(melb_df.dtypes.value_counts())