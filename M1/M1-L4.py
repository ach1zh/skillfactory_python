import math

print(len(str(666 ** 999)))
print(str(666 ** 999))
print("------------------------")
a = -66666 ** 99
print(a)
print("------------------------")
a = math.sqrt(64)
print(a)

print("------------------------")

print(15**42)
print("------------------------")
print("------------------------")

#20 / 5
#"4.0" ** 2

print(True == 1)

a = 10
if a >= 10:
    b = 1
else:
    b = 0
print(b)

print("------------------------\n")
z = 10
if (z % 2) == 0:
    print(str(z)+" является четным числом")
else:
    print(str(z)+" не является четным числом")

print("------------------------\n")
print(3 * 4 - 8 * 2 * (7 - 5.0) + 2)
#12 - 16*2 + 2
#12-32+2
#14-32
#-18

print((10 + 2) / 3 * (15.0 == 15) - 4)
#12 / 3 * 1 -4

print("------------------------\n")
print("------------------------\n")
print(0xb64 == 2916)
print(type(hex(0xb64)))
print("------------------------\n")

print(oct(99))
print(oct(256))
print(0o143)

print("------------------------\n")

#print(-30 ** 99999)
print(oct(-30 ** 99999))

###----------d

#M1_L4
from decimal import Decimal
import math

print(2.44 * 3.12)
print(2.44 * 3.122)
print(2.41 + 33.189)
print(Decimal("2.44") * Decimal("3.122"))
print("----------\n")

print(0.1 + 0.2 == 0.3)
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(0.8 - 0.1 > 0.7)
print("----------\n")
print(Decimal("0.8") - Decimal("0.1") > Decimal("0.7"))
print("----------\n")
print(Decimal("0.8") - Decimal("0.1") == Decimal("0.7"))

# Задание 16.4.13
print(">>----------\n")
#print(Decimal("5.55") == Decimal(5.55))

#print(Decimal("5.55"))
#print(Decimal(5.55))

print(Decimal("90") == 90)
print(99.1 < Decimal("99.1"))

print(Decimal("99.1"))
print(99.1)

print(">>----------\n")
a = 4.2
print(int(a))

print("----------\n")

a = round(12.5)
print(a)
print(type(a))

print(">>----------\n")

#Задание 16.4.14
#print(91*365*24*60*60)
seconds_since_birthdate = 2869776000

#seconds_since_birthdate <= 200
#hours_since_birthdate = seconds_since_birthdate / 60
#days_since_birthdate = hours_since_birthdate / 24
#years_since_birthdate = days_since_birthdate / 365
#years_since_birthdate = math.floor(years_since_birthdate)
#print(years_since_birthdate)


print(math.floor(seconds_since_birthdate/60/60/24/365))

#Лучший вариант
print(seconds_since_birthdate // (365 * 24 * 60 * 60))

#Задание 16.4.15*
#тоже самое, что и Задание 16.4.14