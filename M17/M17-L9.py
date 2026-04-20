#M17-L9

import numpy as np
import pandas as pd

melb_data = pd.read_csv('M17\data\melb_data.csv', sep=',')
#melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Rooms'] = melb_data['Rooms'].astype('int64')

#Задание 8.1
#Bathroom
#print(melb_data[melb_data['Bathroom'] == 0].shape[0])

#Задание 8.2
#print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3000000)].shape[0])

#Задание 8.3
#print((melb_data[melb_data['BuildingArea'] == 0]).min()['Price'])

#Задание 8.4
#ans = melb_data[ (melb_data['Price'] < 1000000) & ( (melb_data['Rooms'] > 5) | (melb_data['YearBuilt'] > 2015) )]
#print( ans['Price'].mean() )

#OR

#f1 = melb_data[(melb_data['Price'] < 1000000)]
#print(f1.shape[0])

#f2 = f1[(melb_data['Rooms'] > 5) | (melb_data['YearBuilt'] > 2015)]
#print(f2.shape[0])
#print(f2['Price'].mean())

#Задание 8.5
result = melb_data[ (melb_data['Price'] < 3000000) & (melb_data['Type'] == 'h') ]
print(result['Regionname'].mode())

