#M16-L6

import numpy as np

# Можно применить к самому
# названию типа данных
#print(np.iinfo(np.int64))
#print('---')
#np.iinfo(np.int64)

# iinfo(min=-128, max=127, dtype=int8)

# Можно применить к существующему
# конкретному объекту
#np.iinfo(a)
# iinfo(min=-128, max=127, dtype=int8)

#b = np.uint64(124)
#print(b)
## 124
#print(type(b))
## <class 'numpy.uint8'>
#print(np.iinfo(b))
## iinfo(min=0, max=255, dtype=uint8)

#x = np.uint8(-456)
#print(x)
#print(-456 % 256)

#Задание 6.6
arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
print(step)
#Задание 6.7
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)

#Задание 6.8 и остальные в тренеровочном редакторе
# Ваш код здесь
import numpy as np
#print(mystery1)
#print(mystery1.shape)
#print(mystery1.size)
#print(mystery1.dtype)
#print(mystery1.itemsize)
