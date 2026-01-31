#M10-L3

#import os
#help(os)

import math
import time

#Задание 3.3.3
print("\n--> Задание 3.3.3 -->\n")
print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))

#Задание 3.3.5
print("\n--> Задание 3.3.5 -->\n")

'''
попробуйте вывести следующие данные:
только время;
только минуты;
только дату;
только месяц.
'''

current_localtime = time.localtime()

print(time.strftime("%H:%M:%S", current_localtime))
print(time.strftime("%M", current_localtime))
print(time.strftime("%d.%m.%Y", current_localtime))
print(time.strftime("%B", current_localtime))

time_struct = time.localtime(time.time())
print(time_struct.tm_min)


 