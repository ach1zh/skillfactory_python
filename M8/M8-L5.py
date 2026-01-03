#M8-L5

"""
### Пример
class User:
   def set_attrs(self, login, password, name, email, role):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role

   def create_task(self, project, description):
       project.add_task(self, description)

class Team:
   def init_team(self, name, members=[]):
       self.name = name
       self.members = members

   def add_member(self, user):
       self.members.append(user)

   def show_members(self):
       print(f'Team {self.name} members:')
       for i, user in enumerate(self.members):
           print(f'№{i + 1}, login: {user.login}, name: {user.name}')

   def get_team_size(self):
       return len(self.members)

class Task:
   def create_task(self, description):
       self.description = description


class Project:
   def create_project(self, name, team):
       self.name = name
       self.team = team
       self.tasks = []

   def add_task(self, user, description):
       if user in self.team.members:
           task = Task()
           task.create_task(description)
           self.tasks.append(task)
           print(f"Task '{description}' added to project '{self.name}'")
       else:
           print(f"User '{user.name}' is not a member of the team working on project '{self.name}'")

#
user1 = User()
user1.set_attrs("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')

user2 = User()
user2.set_attrs("JaneD", "qw1lbz", "Jane Doe", "jane.doe@example.com", 'Python Developer')

user3 = User()
user3.set_attrs("BobS", "gnsJqw12", "Bob Smith", "bob.smith@example.com", 'Python Developer')

team = Team()
team.init_team("Research Group")
team.add_member(user1)
team.add_member(user2)

team.show_members()

project = Project()
project.create_project("UAV Detectron", team)

user1.create_task(project, "Find best model")
user2.create_task(project, "Setup Environment")
user3.create_task(project, "Optimization")
	
# Team Research Group members:
# №1, login: JohnD, name: John Doe
# №2, login: JaneD, name: Jane Doe
# Task 'Find best model' added to project 'UAV Detectron' 
# Task 'Setup Environment' added to project 'UAV Detectron' 
# User 'Bob Smith' is not a member of the team working on project 'UAV Detectron'

###

"""

#Задание 21.4.1 (External resource)

class User:
    def set_private_key(self, private_key):
        self.private_key = private_key    
    
    def show_private_key(self):
        print(f"Приватный ключ пользователя: {self.private_key}")
#
user1 = User()
user1.set_private_key('uox00b_12x')
user1.show_private_key() 

print("----->")
#Задание 21.4.2 (External resource)

class PasswordChecker:
    def set_password_range(self, min_len, max_len):
        self.min_len = min_len 
        self.max_len = max_len
    
    def check_passwords(self, passwords_list=[]):
        result_list = []

        for pass_str in passwords_list:            
            if self.min_len <= len(pass_str) <= self.max_len:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list  
        # в ответе в одну строчку
        # return [self.min_len <= len(p) <= self.max_len for p in passwords]
        
checker1 = PasswordChecker()
#checker1.set_password_range(5, 10)
checker1.set_password_range(6, 10)
print(checker1.min_len, checker1.max_len)

# 5 10

print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))
print(checker1.check_passwords(['afaaffhkjllgg', 'affsbbaf', 'gafg', 'fajkfa']))  

# [False, True, False]
# [False, True, False, True]