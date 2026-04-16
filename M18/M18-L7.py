#M18-L7

import numpy as np
import pandas as pd

#import
trip_data = pd.read_csv('M18\Data\citibike-tripdata.csv', sep=',') #home

#copy
trip_data_df = trip_data.copy()

#Преобразуем столбец Date в формат pandas.datetime
#melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)

#----------#----------#----------#----------#----------#


#Задание 6.1
#print(trip_data_df.info())
#print(300000-299831)
#Задание 6.2
#object

#Задание 6.3
#print(trip_data_df['start station id'].mode())

#Задание 6.4
#print(trip_data_df['bikeid'].mode())

#Задание 6.5
#f1 = (trip_data_df['usertype'] == 'Subscriber')
#f2 = (trip_data_df['usertype'] == 'Customer')
#print([trip_data_df][f1]['usertype'].value_counts())

#print(trip_data_df['usertype'].value_counts(normalize=True))

#Задание 6.6
#print(trip_data_df['gender'].value_counts())

#Задание 6.7
#print(trip_data_df['start station name'].nunique())
#print(trip_data_df['end station name'].nunique())
#
#print(trip_data_df['birth year'].max() - 2018)
#
#print(trip_data_df['start station name'].value_counts())
#
#print(trip_data_df['end station name'].value_counts())

#Задание 6.8
trip_data_df = trip_data_df.drop('start station id', axis=1)
trip_data_df = trip_data_df.drop('end station id', axis=1)
#print(len(trip_data_df.columns))

#Задание 6.9
#print(trip_data_df['birth year'])
trip_data_df['age'] = trip_data_df['birth year'].apply(lambda x: 2018-x) 
trip_data_df = trip_data_df.drop('birth year', axis=1)
#print(trip_data_df[trip_data_df['age'] > 60].shape[0])

#Задание 6.10
#print(trip_data_df['stoptime'])
trip_data_df['starttime'] = pd.to_datetime(trip_data_df['starttime'])
trip_data_df['stoptime'] = pd.to_datetime(trip_data_df['stoptime'])
#print(trip_data_df['stoptime'])
trip_data_df['trip duration'] = trip_data_df['stoptime'] - trip_data_df['starttime']
#print(trip_data_df['trip duration'].iloc[3])

#Задание 6.11
day_of_week = trip_data_df['starttime'].dt.day_of_week
trip_data_df['weekend'] = day_of_week.apply(lambda x: 1 if x in [5,6] else 0)
#print(trip_data_df[trip_data_df['weekend'] == 1].shape[0])

#Задание 6.12


def time_of_day(starttime):    
    if starttime.hour in [0,1,2,3,4,5,6]:
        return 'night'
    elif starttime.hour in [7,8,9,10,11,12]:
        return 'morning'
    elif starttime.hour in [13,14,15,16,17,18]:
        return 'day'
    else:
        starttime.hour in [19,20,21,22,23]
        return 'evening'

trip_data_df['time_of_day'] = trip_data_df['starttime'].apply(time_of_day)
#print(trip_data_df['time_of_day'].head(10))

day_ride = trip_data_df[trip_data_df['time_of_day'] == 'day']
night_ride = trip_data_df[trip_data_df['time_of_day'] == 'night']

print(round(day_ride.shape[0] / night_ride.shape[0]))