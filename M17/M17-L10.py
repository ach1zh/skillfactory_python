#M17-L10
import numpy as np
import pandas as pd

student_data = pd.read_csv('M17\data\students_performance.csv', sep=',')

#Задание 9.1
#print(student_data.shape)


#Задание 9.2
#res = student_data.iloc[155]['writing score']
#print(res)

#Задание 9.3
#print(student_data.info())


#Задание 9.4
#print(student_data.info())


#Задание 9.5
#print(student_data.info())

#Задание 9.6
#res = student_data['math score'].mean()
#print(res)

#Задание 9.7
#res = student_data['race/ethnicity'].mode()
#print(res)

#Задание 9.8
#f1 = (student_data['test preparation course'] == 'completed')
#res = student_data[f1]['reading score'].mean()
#print(res)

#Задание 9.9
#f1 = (student_data['math score'] == 0)
#res = student_data[f1].shape[0]
#print(res)

#Задание 9.10
#standard — платный, free/reduced — бесплатный
#f1 = (student_data['lunch'] == 'standard')
#f2 = (student_data['lunch'] == 'free/reduced')
#res1 = student_data[f1]['math score'].mean()
#res2 = student_data[f2]['math score'].mean()
#print(res1)
#print(res2)

#Задание 9.11
#f1 = (student_data['parental level of education'] == '''bachelor's degree''')
#res = student_data[f1].shape[0]
##1000 100
##118 118*100/1000
#print(res*100/1000)

#Задание 9.12

f_a = (student_data['race/ethnicity'] == 'group A')
f_c = (student_data['race/ethnicity'] == 'group C')

res_a = student_data[f_a]['writing score'].median()
res_c = student_data[f_c]['writing score'].mean()
 
result = abs(round(res_a - res_c))
print(result)
