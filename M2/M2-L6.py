#Задание 17.6.3 (External resource)

number = 5
sum = 0

for i in range(number,0,-1):
    sum += i
print(f'sum = {sum}')

sum = 0

while True:
    if number == 0:
        break
    else:
        sum += number
    number = number - 1
print(sum)