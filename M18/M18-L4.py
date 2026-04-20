#M18-L4 _w_
import numpy as np
import pandas as pd

melb_data = pd.read_csv('data/melb_data_ps.csv', sep=',')
melb_df = melb_data.copy()

'''
Задание 3.3
Создайте в таблице melb_df признак WeekdaySale (день недели). Найдите, сколько объектов недвижимости было продано в выходные (суббота и воскресенье), 
результат занесите в переменную weekend_count. В качестве ответа введите результат вывода переменной weekend_count.
'''

#melb_df.info()

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)

melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
#print(melb_df['WeekdaySale'].tail(30))
##print(melb_df['WeekdaySale'].value_counts()[5] + melb_df['WeekdaySale'].value_counts()[6])


'''
Задание 3.4
В каком году отмечается наибольшее количество случаев наблюдения НЛО в США?
'''

ufo_data = pd.read_csv('data/ufo.csv', sep=',')
ufo_data_df = ufo_data.copy()
#print(ufo_data_df.info())

#Преобразуем столбец Date в формат pandas.datetime
#print(ufo_data_df['Time'].head(10))
##ufo_data_df['Time'] = pd.to_datetime(ufo_data_df['Time'], dayfirst=True)
#print(ufo_data_df['Time'].head(10))

##ufo_data_df['Year'] = ufo_data_df['Time'].dt.year
##print(ufo_data_df.head(5))

#Ответ
##print(ufo_data_df['Year'].mode())

'''
Задание 3.5
Найдите средний интервал времени (в днях) между двумя последовательными случаями наблюдения НЛО в штате Невада (NV).
- Чтобы выделить дату из столбца Time, можно воспользоваться атрибутом datetime date.
- Чтобы вычислить разницу между двумя соседними датами в столбце, примените к нему метод diff().
- Чтобы перевести интервал времени в дни, воспользуйтесь атрибутом timedelta days.
'''

#Преобразуем столбец Date в формат pandas.datetime
ufo_data_df['Time'] = pd.to_datetime(ufo_data_df['Time'], dayfirst=True)
'''
#Выделяем дату из столбца Time (убираем время)
ufo_data_df['Date'] = ufo_data_df['Time'].dt.date

# Фильтруем данные для штата Невада (NV)
f1 = (ufo_data_df['State'] == 'NV')
nv_data = ufo_data_df[f1]

# Сортируем данные по дате
#nv_data = nv_data.sort_values('Date')

# Вычисляем разницу между последовательными датами
##nv_data['Diff'] = nv_data['Date'].diff()
nv_data['Diff'] = nv_data['Time'].diff()

#print(nv_data)
#print(nv_data[['Time','Diff']].head(20))

nv_data['Diff_days'] = nv_data['Diff'].dt.days

#print(nv_data)
#print(nv_data[['Time','Diff','Diff_days']].head(20))

#Рассчитываем средний интервал времени в днях (игнорируем NaN — первую строку)
average_interval = nv_data['Diff_days'].mean()
print(round(average_interval))
print(nv_data['Diff'].mean())
'''
# Фильтруем данные для штата Невада (NV)
f1 = (ufo_data_df['State'] == 'NV')
nv_data = ufo_data_df[f1]

nv_data['Diff'] = nv_data['Time'].diff()
#print(nv_data[['Time','Diff']].head(40))

print(nv_data['Diff'].mean())