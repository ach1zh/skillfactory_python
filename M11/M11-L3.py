#M11-L3

#Задание 22.2
print("\n--> Задание 22.2 -->\n")


"""
Реализуйте систему таким образом, чтобы она позволяла:

- Добавлять новые заказы в очередь.
- Поварам брать заказы из очереди для выполнения.
- Отслеживать статус заказов.
- Выводить информацию о текущих заказах в очереди.

Также вы можете добавить следующий функционал:

- Возможность отмены заказа.
- Возможность изменения заказа.
- Возможность назначения приоритета заказам.
- Интерфейс пользователя для взаимодействия с системой.
"""
import random

class Order:

    #Конструктор для создания нового заказа.
    def __init__(self, customer_name, dishes, order_id):        
        
        # (имя клиента)
        self.__customer_name = customer_name
    
        #список блюд
        self.__dishes = dishes
    
        #статус заказа: «новый», «в процессе», «готов»
        self.__status = "New"

        self.__order_id = order_id

    @property
    def order_id(self):
        return self.__order_id
    
    @order_id.setter
    def order_id(self,value):
        self.__order_id = value

    @property
    def customer_name(self):
        return self.__customer_name
    
    @property
    def dishes(self):
        return self.__dishes

    @dishes.setter
    def dishes(self,value):
        self.__dishes = value


    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, value):
        self.__status = value


class RestaurantQueue:
    
    # очередь заказов, реализованная с помощью списка
    def __init__(self):
        self.queue = []

    # Проверяет, пуста ли очередь
    def is_empty(self):        
        return len(self.queue) == 0        

    # Добавляет новый заказ в очередь.
    def add_order(self, order):        
        self.queue.append(order)

    #Извлекает и возвращает первый заказ из очереди.
    def take_order(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    #Отмечает заказ как выполненный.
    def complete_order(self, order):
        if not self.is_empty():
            order.status = 'Сompleted'    
        else:
            print("Queue is empty")
            
 
    #Выводит информацию о текущих заказах в очереди.
    def print_queue(self):
        if not self.is_empty():
            for item in self.queue:                
                print(item.order_id)
                print(item.customer_name)
                print(item.dishes)
                print(item.status)
                print("-----")
                
        else:
            print("Queue is empty")
        
        #print(self.queue[0].__dict__)
        #print(self.queue[0].get_status())
        #print(self.queue[0].status)
      

    ###
    
    #Отменяет заказ по его идентификатору. Потребуется модификация класса Order и реализация поиска по очереди.
    def cancel_order(self, order_id):        
        if not self.is_empty():
            self.queue.pop(order_id - 1)
        else:
            print("Queue is empty")            
    
    #Изменяет список блюд в заказе по его идентификатору.
    def modify_order(self, order_id, new_dishes): 
        if not self.is_empty():
            self.queue[order_id].dishes = new_dishes
        else:
            print("Queue is empty")
    
    #Устанавливает приоритет заказа по его идентификатору.
    def set_priority(self, order_id, priority): 
        #мало времени делаем тяп ляп
        self.queue[order_id].order_id = priority 

### Использование ###

dishes_list = ["Пицца «Маргарита","Паста карбонара","Ризотто с грибами портобелло","Оссобуко по-милански","Тирамису","Суши «Дракон»","Брускетта с томатами","Салат капрезе","Панцанелла","Мороженое с солёной карамелью"]
customer_names_list = ["Анна","Мария","Елена","Ольга","Татьяна","Светлана","Наталья","Ирина","Юлия","Екатерина"]

#print(random.choice(dishes_list))
#print(random.choice(customer_names_list))

restaurant_queue = RestaurantQueue()

order_01 = Order(random.choice(customer_names_list),[random.choice(dishes_list),random.choice(dishes_list)],1)
order_02 = Order(random.choice(customer_names_list),[random.choice(dishes_list),random.choice(dishes_list)],2)
order_03 = Order(random.choice(customer_names_list),[random.choice(dishes_list),random.choice(dishes_list)],3)
order_04 = Order(random.choice(customer_names_list),[random.choice(dishes_list),random.choice(dishes_list)],4)
order_05 = Order(random.choice(customer_names_list),[random.choice(dishes_list),random.choice(dishes_list)],5)

#print(order_01.__dict__)
#print(order_01.status)

#print(restaurant_queue.is_empty())

restaurant_queue.add_order(order_01)
restaurant_queue.add_order(order_02)
restaurant_queue.add_order(order_03)
restaurant_queue.add_order(order_04)
restaurant_queue.add_order(order_05)

#print(restaurant_queue.is_empty())

#print(restaurant_queue.__dict__)

#restaurant_queue.print_queue()
order_to_cook = restaurant_queue.take_order()
#print(order_to_cook.__dict__)
restaurant_queue.complete_order(order_01)
restaurant_queue.modify_order(3,["Пицца три сыра","Пицца тридцать три сыра"])
restaurant_queue.cancel_order(2)
restaurant_queue.set_priority(3,0)

restaurant_queue.print_queue()