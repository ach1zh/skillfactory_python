#M7_L2

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

###

print("\n---------->")

a = 5
b = 3+2

print(id(a))
print(id(b))
print(id(a)-id(b))

print("\n---------->")

a = 0
b = 0

while id(a) == id(b):
    a += 1
    b += 1

print(a)

print("\n---------->")

a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)

print("\n---------->")

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_before == list_id_after )


#Задание 5.2.9
print("\n---------->")

def getUniqS(str_to_check):
    return len(set(str_to_check))

str_to_check = "asdadsfgsdfgsdfggdjnghj"
str_to_check = "The Zen of Python"

print(getUniqS(str_to_check))

print("\n---------->")
#Задание 5.2.12

s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {2, 4, 6, 8, 10, 12}

print (s1.symmetric_difference(s2))