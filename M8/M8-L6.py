#M8-L6

#Задание 21.5.2 (External resource)
print("\nЗадание 21.5.2 (External resource) -->\n")

class Team():
    def __init__(self, name, team_size, capital):
        self.name =  name
        self.team_size = team_size
        self.capital = capital

    def show_info(self):        
        #Team name: <значение атрибута name>, team size: <значение атрибута team_size>, capital: <значение атрибута capital>
        print(f"Team name: {self.name}, team size: {self.team_size}, capital: {self.capital}")


team1 = Team('OpenAI', 100, 1000000)
team1.show_info()
# Team name: OpenAI, team size: 100, capital: 1000000
# Team name: OpenAI, team size: 100, capital: 1000000



#Задание 21.5.3 (External resource)
print("\nЗадание 21.5.3 (External resource) -->\n")

class AreaPoint():
    def __init__(self, i, j, height=15):
        self.i = i
        self.j = j
        self.height = height

area_list = []
for k in range(0,3):
    arr_str = []
    for m in range(0,3):
        nextAreaPoint = AreaPoint(m,k)
        arr_str.append(nextAreaPoint)
        #print(m,k)
    area_list.append(arr_str)

#print(area_list)

#Задание 21.5.4 (External resource)
print("\nЗадание 21.5.4 (External resource) -->\n")

class Person():
    def __init__(self, name=None, age=None, gender=None, occupation=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
    def set_attributes(self,attr_list:dict):        
        for attr_name, attr_value in attr_list.items():
            if attr_name == 'name':
                self.name = attr_value
            elif attr_name == 'age':
                self.age = attr_value
            elif attr_name == 'gender':
                self.gender = attr_value
            elif attr_name == 'occupation':
                self.occupation = attr_value
            else:
                self.attr_name = attr_value

    '''
    Решение преподавателя
    def set_attributes(self, attr_dict):
       if 'name' in attr_dict:
           self.name = attr_dict['name']
       if 'age' in attr_dict:
           self.age = attr_dict['age']
       if 'gender' in attr_dict:
           self.gender = attr_dict['gender']
       if 'occupation' in attr_dict:
           self.occupation = attr_dict['occupation']
    '''

    def show_card(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}")
        #...

p1 = Person()
p1.set_attributes({'name': 'Elon', 'age': 51, 'gender': 'Male', 'occupation': 'CEO', 'company': 'Tesla'})
p1.show_card()
# Name: Elon
# Age: 51
# Gender: Male
# Occupation: CEO
print("---")
p2 = Person(name='Mark', occupation='Expert')
p2.set_attributes({'name': 'Bob', 'occupation': 'Worker', 'company': 'StenWoods'})
p2.show_card()
# Name: Bob
# Age: None
# Gender: None
# Occupation: Worker

#Задание 21.5.5 (External resource)
print("\nЗадание 21.5.5 (External resource) -->\n")

import math

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):                   
        if  self.a < (self.b + self.c)\
            and self.b < (self.a + self.c)\
            and self.c < (self.a + self.b):
            #print('True')
            return True
        else:
            #print('False')
            return False

    
    def get_triangle_area(self):
        if self.is_triangle():
            p = (self.a + self.b + self.c) / 2
            S = math.sqrt( (p * (p - self.a) * (p - self.b) * (p - self.c)) )
            return S
        else:
            #print("0")
            return 0    


t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())

# True

print(t1.get_triangle_area())

# 6.0

t2 = Triangle(a=10, b=5, c=5)
print(t2.is_triangle())

# False

#Задание 21.5.6 (External resource)
print("\nЗадание 21.5.6 (External resource) -->\n")

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,id):
        self.items.append(id)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False        

    def dequeue(self):
        return self.items.pop(0)

    def show_queue(self):
        print(*self.items)
      

# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()  

# 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()  

# 3

#Задание 21.5.7 (External resource)
print("\nЗадание 21.5.7 (External resource) -->\n")

class User():
    
    def __init__(self,email,password,balance):
        self.email = email
        self.password = password
        self.balance = balance

    def login(self,email,password):
        return self.email == email and self.password == password

    def update_balance(self,amount):
        self.balance += amount  

user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# False
print(user.login("gosha@roskino.org", "qwerty"))
# True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# 19700


#Задание 21.5.8 (External resource)
print("\nЗадание 21.5.8 (External resource) -->\n")

class IntDataFrame():
    def __init__(self,int_list):
        self.column = [int(value) for value in int_list]

    def count(self):
        not_null_elements = list(filter(lambda x: x!=0, self.column))        
        return len(not_null_elements)

    def unique(self):
        unique_list = [x for i,x in enumerate(self.column) if x not in self.column[:i]]        
        #print(unique_list)
        return len(unique_list)

df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)
# [4, 4, 3, 0, 2, 0, 4]

print(df.count())
# 5

print(df.unique())
# 4
