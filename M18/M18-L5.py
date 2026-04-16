#M18-L5 - W
#M18-L5

import numpy as np
import pandas as pd

#home
#melb_data = pd.read_csv('M18\Data\melb_data_ps.csv', sep=',')
#work
melb_data = pd.read_csv('data/melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()

'''
#---

def get_street_type(address):
    exclude_list = ['N', 'S', 'W', 'E']
    address_list = address.split(' ')
    street_type = address_list[-1]
    if street_type in exclude_list:
        street_type = address_list[-2]
    return street_type

street_types = melb_df['Address'].apply(get_street_type)
###
#print(street_types)
#print(street_types.nunique())
#print(street_types.value_counts())
melb_df['StreetType'] = street_types.apply(lambda x: 'Av' if x == 'Avenue' else ('Bvd' if x == 'Boulevard' else ('Pde' if x == 'Parade' else x)))
#print(melb_df['StreetType'].nunique())
#print(melb_df['StreetType'].value_counts())
###
popular_stypes =street_types.value_counts().nlargest(10).index
#print(popular_stypes)
# Index(['St', 'Rd', 'Ct', 'Dr', 'Av', 'Gr', 'Pde', 'Pl', 'Cr', 'Cl'], dtype='object')
melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
#print(melb_df['StreetType'])
#print(melb_df['StreetType'].nunique())
# 11

#-------------------------------------------

###
#Задание 4.2

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)

melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
#print(melb_df['WeekdaySale'].head(30))
#print(melb_df['WeekdaySale'].value_counts())
##print(melb_df['WeekdaySale'].value_counts()[5] + melb_df['WeekdaySale'].value_counts()[6])

def get_weekend(weekday):
    if weekday in [5,6]:
        return 1
    else:
        return 0
    
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
#print(melb_df['Weekend'].head(30))
f1 = (melb_df['Weekend'] == 1)
print(round(melb_df[f1]['Price'].mean()))


#-------------------------------------------

#Задание 4.3
#print(melb_df['SellerG'].head(20))
#print(melb_df['SellerG'].value_counts)

top_seller_g = melb_df['SellerG'].value_counts().nlargest(49).index
#print(top_seller_g)
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in top_seller_g else 'other')
#print(melb_df['SellerG'].value_counts)
#print(melb_df['SellerG'].head(50))
min_price_nelson = melb_df[(melb_df['SellerG'] == 'Nelson')]['Price'].min()
min_price_s_other = melb_df[(melb_df['SellerG'] == 'other')]['Price'].min()

#print(s_nelson.value_counts()[0])

#print(s_nelson.value_counts()[0] - s_other.value_counts()[0])
##print(melb_df['WeekdaySale'].value_counts()[5] + melb_df['WeekdaySale'].value_counts()[6])c

#Ответ
print(round(min_price_nelson / min_price_s_other,2))

'''
#-------------------------------------------

#Задание 4.4 (External resource)

def get_experience(arg):    
    arg_str = arg.split(' ')
    #print(f"{arg_str[2]},{arg_str[4]}")
    #print(len(arg_str))
    if len(arg_str) == 6:
        return int(arg_str[2]) * 12 + int(arg_str[4])
    else:
        if 'год' in arg_str[3] or 'лет' in arg_str[3]:
            return int(arg_str[2]) * 12
        else:
            return int(arg_str[2])

test_series_1 = pd.Series([
    'Опыт работы 8 лет 3 месяца',
    'Опыт работы 3 года 5 месяцев',
    'Опыт работы 1 год 9 месяцев',
    'Опыт работы 3 месяца',
    'Опыт работы 6 лет'
])

test_series_2 = pd.Series([
    'Опыт работы 5 лет',
    'Опыт работы 5 месяцев',
    'Опыт работы 1 год 1 месяц',
    'Опыт работы 3 месяца',
    'Опыт работы 7 лет'
])

'''
Ожидаемый ответ:

0    99
1    41
2    21
3     3
4    72
dtype: int64

Ожидаемый ответ:

0    60
1     5
2    13
3     3
4    84
dtype: int64
'''

print(test_series_1.apply(get_experience))
print(test_series_2.apply(get_experience))