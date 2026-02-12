#M11-L2

#Задание 22.1
print("\n--> Задание 22.1 -->\n")

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates

def find_duplicates2(arr):
    duplicates = []
    seen = set()
    for i in arr:
        if i in seen:
            duplicates.append(i)
        else:
            seen.add(i)
    return duplicates

arr = [1,2,3,4,5,4,5]
print(find_duplicates(arr))
print(find_duplicates2(arr))