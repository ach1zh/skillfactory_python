#M11-L6

#Задание 22.5
print("\n--> Задание 22.5 -->\n")

"""
Находим наименьший элемент в массиве.
Обмениваем его с элементом на первой позиции.
Повторяем это для подмассива, начиная со второго элемента, и ищем наименьший элемент.
Обмениваем его с элементом на второй позиции.
Продолжаем так до тех пор, пока весь массив не будет отсортирован.

Для i от 0 до n-1:
    Ищем наименьший элемент в массиве от i до n-1.
    Обмениваем его с элементом на позиции i.
"""

#v1
import random

#[4, 31, 47, 8, 2, 1, 1, 12, 2, 40]

def select_sort(array):

  min_element_index = 0
  for i in range(0,len(array)):
    #print(array)  
        
    def get_min_element(arr):
      min_element_index = 0
      for i in range(0,len(arr)):
        if arr[i] < arr[min_element_index]:
          min_element_index = i
      return min_element_index  

    min_element = i + get_min_element(array[i:])  

    #print(f"array[i:]: {array[i:]}")
    #print(f"min_element_index: {min_element}")
    #print(f"min_element_value: {array[min_element]}")

    #temp = array[i]
    #array[i] = array[min_element]
    #array[min_element] = temp

    array[i],array[min_element] = array[min_element],array[i]
    
    #print(array)
    #print("\n")
    
  
  return array

not_sorted = [random.randint(1, 50) for _ in range(10)]
#not_sorted = [11, 18, 39, 7, 28, 20, 32, 5, 40, 34]
#not_sorted = [4, 31, 47, 8, 2, 1, 1, 12, 2, 40]

print(not_sorted)
print(select_sort(not_sorted))


#Ответ задачи

def selection_sort(arr):
    n = len(arr)  # Определение длины массива
    for i in range(n - 1):  # Перебор всех элементов массива, кроме последнего
        min_index = i  # Предполагаем, что первый неотсортированный элемент является минимальным
        for j in range(i + 1, n):  # Перебор элементов, следующих за текущим i, для поиска наименьшего
            if arr[j] < arr[min_index]:  # Если найден элемент меньше, чем предполагаемый минимальный, то: 
                min_index = j  # Обновляем индекс минимального элемента
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Меняем местами текущий элемента с наименьшим найденным
    return arr