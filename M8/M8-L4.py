#M8-L4
class User:
   login = 'user_login'
   role = 'Python Developer'


u1 = User()
u2 = User()

print(u1.login, u1.role)
print(u2.login, u2.role)

# user_login Python Developer
# user_login Python Developer

User.login = 'form_login'
User.role = 'Designer'

print(u1.login, u1.role)
print(u2.login, u2.role)

# form_login Designer
# form_login Designer

#Задание 21.3.1 (External resource)

class Student:
   name = "name"
   surname = "surname"
   semester = 0
   course = "Data Science"

s1 = Student()
s1.name = "Иван"
s1.surname = "Иванов"
s1.semester = 1
#s1.semester2 = 1

#result = s1.__dict__
#print(result)

#Задание 21.3.2 (External resource)

class Group:
   members = []

s2 = Student()
s2.name = 'Лев'
s2.surname = 'Сергеев'
s2.semester = 1

Group.members.append(s1)
Group.members.append(s2)
result = Group.members
#print("--->")
#print(result)