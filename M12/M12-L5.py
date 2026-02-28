#M12-L5

#Задание 5.5.1
print("\n--> Задание 5.5.1 -->\n")

import redis

# Basic connection param.
r = redis.Redis(
<<<<<<< HEAD
    host='***',
    port=12509,
    decode_responses=True,
    username="default",
    password="***",
=======
    host='redis-12509.c328.europe-west3-1.gce.cloud.redislabs.com',
    port=12509,
    decode_responses=True,
    username="default",
    password="DjDOmGpgXH2gPCogmawsZjwfW3nUw1hX",
>>>>>>> 0a50c1beaa265cd85c9fca5b4f4b6e735aea4453
)

# Test connection
#r.set('foo', 'bar')
#print(r.get('foo'))


#Задание 5.5.4
print("\n--> Задание 5.5.4 -->\n")

class Contact:
    def __init__(self,person,phone_number):
        self.person = person
        self.phone_number = phone_number

class PhoneBook:

    def __init__(self):
        PhoneBook = dict()
        # add connection to redis cloud DB        

    def add_contact(self, contact):
        r.set(contact.person, contact.phone_number)        

    def get_contact(self, person):
        print(f"Person: {person}, phone_number: {r.get(person)}")

    def get_all_contact(self):        
        
        print('\nAll data:\n')
        
        for key in r.keys('*'):
            print(f"Person: {key}, phone_number: {r.get(key)}")     

    def del_contact(self, person):
        r.delete(person)

    def write_PhoneBook_to_redis_cloud_db():
        ...

    def read_PhoneBook_from_redis_cloud_db():
        ...        

contact_01 = Contact('user1','12345')
contact_02 = Contact('user2','678910')
contact_03 = Contact('user3','593541')
phone_book = PhoneBook()

phone_book.add_contact(contact_01)
phone_book.add_contact(contact_02)
phone_book.add_contact(contact_03)

phone_book.get_contact(contact_01.person)
phone_book.get_contact(contact_02.person)
phone_book.get_contact(contact_03.person)

phone_book.del_contact(contact_02.person)
phone_book.get_all_contact()

"""
# Записать данные 
red.set('var1', 'value1')  # записываем в кеш строку "value1"
print(red.get('var1'))  # считываем из кеша данные

# Удаление данных
red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))

# Запись словаря через json
dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание
"""

""" Решение
red = redis.Redis(
    host='ваш хост', 
    port=ваш порт, 
    password=пароль 
)
 
cont = True
 
while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break
"""