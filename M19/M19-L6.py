#M19-L6 notebook

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

#print(m_data_movies_df.info())
#print()

#Задание 5.2
#print(m_data_movies_df.title.unique().shape[0])

#Задание 5.3
#print(m_data_ratings1_df.info())
#print(m_data_ratings1_df.userId.unique().shape[0])

#Задание 5.4
print(m_data_dates_df['date'].dt.year.value_counts().sort_values())