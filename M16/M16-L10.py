#M16-L10

# Введите свое решение ниже

import numpy as np
np.random.seed(2021)

#Задание 9.6 (External resource)

#В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand()

#Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)

#Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 100, size=(3, 2))
#print(table)

#В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.array([2,4,6,8,10,12,14,16])

#Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился
mix = np.random.permutation(even)
#print(mix)

#Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, size=3, replace=False)
#print(select)
#Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
#print(triplet)