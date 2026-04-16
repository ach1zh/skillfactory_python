#M19-L3

import numpy as np
import pandas as pd

#import
melb_data = pd.read_csv('M19\Data\melb_data_fe.csv', sep=',') #home

#copy
melb_df = melb_data.copy()

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date']) #~~dayfirst=True~~

#----------#----------#----------#----------#----------#

#Задание 2.1
#kind

#Задание 2.2
# !!! +2 !!!
answer = melb_df.sort_values(by='AreaRatio', ascending=False, ignore_index=True).iloc[1558+2]
print(answer.BuildingArea)

#Ответ из задания
#print(int(melb_df.sort_values(by='AreaRatio', ignore_index=True, ascending=False).loc[1558, 'BuildingArea']))


#Задание 2.3

f1 = melb_df['Type'] == 'townhouse'
f2 = melb_df['Rooms'] > 2

answer3 = melb_df[f1 & f2].sort_values(by=['Rooms', 'MeanRoomsSquare'],ascending=[True, False],ignore_index=True)

print(answer3.iloc[18])
#18   Brighton East      3  townhouse  1300000.0
