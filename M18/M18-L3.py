#M18-L3

import numpy as np
import pandas as pd

melb_data = pd.read_csv('M18\Data\melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()
#print(melb_df.head())

#Задание 2.3 (External resource)
import numpy as np
import pandas as pd

def delete_columns(df, col=[]):
    for c in col:
        if c not in df.columns:
            return None
    return df.drop(col, axis=1)    

customer_df = pd.DataFrame({
            'number': [0, 1, 2, 3, 4],
            'cust_id': [128, 1201, 9832, 4392, 7472],
            'cust_age': [13, 21, 19, 21, 60],
            'cust_sale': [0, 0, 0.2, 0.15, 0.3],
            'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
            'cust_order': [1400, 14142, 900, 1240, 8430]
        })
test_df_2 = pd.DataFrame({
            'number2': [0, 1, 2, 3, 4],
            'cust_id2': [128, 1201, 9832, 4392, 7472],
            'cust_age2': [13, 21, 19, 21, 60],
            'cust_sale2': [0, 0, 0.2, 0.15, 0.3],
            'cust_year_birth2': [2008, 2000, 2002, 2000, 1961],
            'cust_order2': [1400, 14142, 900, 1240, 8430]
        })

print(delete_columns(customer_df,['number','cust_age']))
print(delete_columns(col = ['cust_sale2', 'not_existing_col'], df = test_df_2))


#Задание 2.4

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'area': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

countries_df['pop_density'] = countries_df['population'] * 1000000 / countries_df['area']
print( round(countries_df['pop_density'].mean(),2))