def binary_search(numbersList, x):

    if numbersList[0] > numbersList[-1] or len(numbersList) <= 1:
        return False
    mid = len(numbersList) // 2
    if numbersList[mid] == x:
        return True
    elif numbersList[mid] > x:
        return binary_search(numbersList[:mid], x)
    else:
        return binary_search(numbersList[mid:], x)

print(binary_search([4, 5, 6, 7, 8, 9, 10], 4))
#print(binary_search([4, 5],4))

