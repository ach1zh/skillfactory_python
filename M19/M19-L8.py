#M19_L8

import numpy as np
import pandas as pd

#Задание 7.4
a = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [103, 214, 124], 'C': [1, 4, 2]})
b = pd.DataFrame({'V': ['d', 'b', 'c'], 'U': [1393.7, 9382.2, 1904.5], 'C': [1, 3, 2]})

print(a)
print(b)
print("---")

##print(a.join(b, how='inner', r_suffix='_r'))
#print(a.merge(b, how='left', on='C'))
#print(a.merge(b, how='inner', right_on='А', left_on='V'))
#print(b.join(a.set_index('C'), how='right', on='C'))
#print(a.merge(b, how='right', on='C'))
#print(a.merge(b, how='inner', on='C'))

#Задание 7.5 (External resource)

"""
Информация в таблицах представлена в виде следующих столбцов:

item_id — идентификатор модели;
vendor — производитель модели;
stock_count — имеющееся на складе количество данных моделей (в штуках);
purchase_id — идентификатор покупки;
price — стоимость модели в покупке.
Вам необходимо сделать следующее:

Сформируйте DataFrame merged, так чтобы после объединения purchase_df и items_df остались модели, которые учтены на складе и имели продажи.

На основе таблицы merged найдите суммарную выручку, которую можно было бы получить от продажи всех товаров, имеющихся на складе.
 Результат занесите в переменную income.
"""

items_df = pd.DataFrame({
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
})

purchase_df = pd.DataFrame({
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
})


print(items_df)
print(purchase_df)

merged = items_df.merge(purchase_df, on='item_id',how='inner')
#print(merged)
#merged['total'] = merged['stock_count'] * merged['price']
#income = int(merged['total'].sum())
income = (merged['stock_count'] * merged['price']).sum()
print(income)

'''
Ожидаемый ответ:

item_id   vendor  stock_count  purchase_id  price
0   417283  Samsung           54          101  13900
1   849734       LG           33          101   5330
2   132223    Apple          122          101  38200
3   573943    Apple           18          112  49990
4    19475       LG          102          121   9890
5  3294095    Apple           43          145  33000
6   382043  Samsung           77          145  67500
7   302948  Samsung          143          145  34500
8   100132       LG           60          221  11400
'''