#M18-L6 - W

import numpy as np
import pandas as pd

#melb_data = pd.read_csv('M18\Data\melb_data_ps.csv', sep=',') #home
melb_data = pd.read_csv('data/melb_data_ps.csv', sep=',') #work

#COPY
melb_df = melb_data.copy()

#Преобразуем столбец Date в формат pandas.datetime
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)

#----------#----------#----------#----------#----------#


#print(melb_df.info())
#memory usage: 2.4+ MB

top_suburb = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in top_suburb else 'other')

# преобразуем тип столбца в category
melb_df['Suburb'] = melb_df['Suburb'].astype('category')

print(melb_df.info())
#memory usage: 2.3+ MB

#Ответ: 0.1