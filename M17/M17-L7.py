#M17-L6
import numpy as np
import pandas as pd

melb_data = pd.read_csv('M17\data\melb_data.csv', sep=',')

#print(melb_data.head())
#print(melb_data.tail(7))
#print(melb_data.shape)
melb_data.info()

#print(pd.DataFrame([[0,1], [1, 0], [1, 1]], columns=['А', 'B']))
print(13580-12211)


###
#Преобразовние типов
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
###

melb_data.info()

print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])

print(melb_data.describe(include=['object']))

print(melb_data['Type'].value_counts(normalize=True))