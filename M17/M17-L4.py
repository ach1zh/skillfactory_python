#M17-L4

#Задание 3.5 (External resource)

import numpy as np
import pandas as pd

def create_companyDF(income, expenses, years):
    #v1
    #data_frame = pd.DataFrame(data = [ (item1, item2) for item1, item2 in zip(income,expenses) ], columns=['Income','Expenses'], index=years)
    
    #v2    
    merged = []
    max_len = max(len(income), len(expenses))
    
    for i in range(max_len):
        row = []
        row.append(income[i] if i < len(income) else None)
        row.append(expenses[i] if i < len(expenses) else None)
        merged.append(row)
    data_frame = pd.DataFrame(data=merged, columns=['Income','Expenses'], index=years)    
    return data_frame

"""
Также напишите функцию get_profit(df, year), которая возвращает разницу 
между доходом и расходом, записанными в таблице df, за год year.
"""
def get_profit(df, year):
    #print(df.index)
    if year in df.index:
        #print(df.loc[year],'Income')
        #print(df.loc[year],'Expenses')
        #print(478-156)
        return (df.loc[[year],'Income'] - df.loc[[year],'Expenses'])[year]
    else:
        return None




income = [478, 512]
#income = [478, 512, 196]
expenses = [156, 130, 270]
years = [2018, 2019, 2020]

df = create_companyDF(income,expenses,years)
print(df)
print('--->')
print(get_profit(df, years[0]))
print('--->')
print(get_profit(year = 2018, df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])))
#print(get_profit(year = 2013, df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])))
"""
    Income  Expenses
2018    478     156
2019    512     130
2020    196     270
"""