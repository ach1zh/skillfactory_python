#M2-L7
#Задание 17.7.1 (HW-04)

multipl = 1
for i in range(1,11,1):
    if i% 2 == 0:
        #print(str(i) + " - четное")
        continue
    else:
        print(str(i) + " -нечетное")
        multipl = multipl*i
print(multipl)
print(multipl == (1*3*5*7*9))



###################
test = 0
for i in range(2):
    #print (i)
    for j in range(2):
        #print (i)
        for k in range(2):
            print (k)
        print("-----------")