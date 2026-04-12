#M16-L11
"""
#Задание 10.5
# Ваш код здесь
import numpy as np

print(x)
print(y)
print(type(x))
print(type(y))

a = np.int64(x) + np.int64(y)

print(type(a))
print(a)
"""
#M16-L11
#Задание 10.6 (External resource)

import numpy as np

def get_chess(a):
    zeros = np.zeros((a,a))    
    zeros[::2,1::2] = 1
    zeros[1::2,0::2] = 1
    return(zeros)

#print(get_chess(4))

# Введите свое решение ниже
#M16-L11
#Задание 10.7 (External resource)
import numpy as np

def shuffle_seed(array):
    seed = np.random.randint(0,2**32-1)
    np.random.seed(seed)        
    #print(seed)    
    shuffled = np.random.permutation(array)
    return (shuffled,seed)
    
#array = [1, 2, 3, 4, 5]
#print(shuffle_seed(array))

# Введите свое решение ниже
#M16-L11
#Задание 10.8 (External resource)
import numpy as np

def min_max_dist(*vectors):
    all_distances = []
    for vec1 in vectors:
        for vec2 in vectors:
            if vec2 is not vec1:
                distance = np.linalg.norm(vec1 - vec2)
                all_distances.append(distance)
    
    all_distances2 = np.array(all_distances)
    return np.min(all_distances2), np.max(all_distances2)    

#vec1 = np.array([1,2,3])
#vec2 = np.array([4,5,6])
#vec3 = np.array([7, 8, 9])

#print(min_max_dist(vec1, vec2, vec3))

# Введите свое решение ниже
#M16-L11
#Задание 10.9 (External resource)
import numpy as np

def any_normal(*vectors):    
    for vec1 in vectors:
        for vec2 in vectors:
            if vec2 is not vec1:
               if np.dot(vec1,vec2) == 0:
                return True
    return False
    
#vec1 = np.array([2, 1])
#vec2 = np.array([-1, 2])
#vec3 = np.array([3,4])
#print(any_normal(vec1, vec2, vec3))

#Задание 10.10 (External resource)
import numpy as np

def get_loto(num):
    return np.random.randint(0,100,size=((num, 5, 5)))

#print(get_loto(3))

#Задание 10.11 (External resource)
print("-->")

import numpy as np

def get_unique_loto(num):
    #return np.random.randint(0,100,size=((num, 5, 5)))
    result_arr = []
    for _ in range(num):    
        flag = True
        while flag:
            try:
                result_arr.append(np.random.choice(np.random.randint(0,101),size=(5, 5), replace=False))
                flag = False
            except:
                ...            

    return np.array(result_arr)

ans = get_unique_loto(10)
print(ans)
print(np.shape(ans))

"""
Решение из ответа

import numpy as np
def get_unique_loto(num):
    sample = np.arange(1, 101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample,
            replace=False, size=(5, 5)))
    res = np.array(res)
    return res

"""