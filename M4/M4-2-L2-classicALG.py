# Классическое решение
def binary_search_recursive(lst, target, low, high):
    # Базовый случай: если границы пересеклись, элемента нет
    if low > high:
        return False

        # Находим средний индекс
    mid = (low + high) // 2

    # Проверяем средний элемент
    if lst[mid] == target:
        return True
        # Если искомый элемент меньше среднего, ищем в левой половине
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, low, mid - 1)
        # Иначе ищем в правой половине
    else:
        return binary_search_recursive(lst, target, mid + 1, high)

    # Удобная обертка для вызова


def contains_element(lst, target):
    return binary_search_recursive(lst, target, 0, len(lst) - 1)


# Пример использования:
my_list = [1, 3, 5, 7, 9, 11, 13]
print(contains_element(my_list, 7))  # True
print(contains_element(my_list, 4))  # False
