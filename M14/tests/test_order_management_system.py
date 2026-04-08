#M14-L2
"""
Напишите тесты для системы управления заказами, используя pytest.

Ваши тесты должны:
Использовать фикстуры для настройки и очистки тестовых данных.
Использовать параметризацию для тестирования системы с различными наборами входных данных.
Использовать маркеры для категоризации тестов.
Также вам необходимо сгенерировать HTML-отчет о результатах тестов с помощью плагина pytest-html.
"""

#Что бы работал импорт пр
import os
import sys
# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from M14.src.order_management_system import Order, OrderManagementSystem

@pytest.fixture
def order_management_system():   
    yield OrderManagementSystem()

#@pytest.mark.parametrize("customer_id, expected_result", [(1,1),(2,1)])
#def test_create_order(customer_id, expected_result):    
#    oms = OrderManagementSystem()
#    assert oms.create_order(customer_id) == expected_result

#@pytest.mark.parametrize("order_id, expected_result", [(1,True),(2,True)])
#def test_get_order(order_management_system,order_id, expected_result):    
#    oms = order_management_system
#    #oms.create_order(12345)
#    #oms.create_order(45678)
#    #oms.create_order(9101112)
#    order1 = oms.create_order(12345)
#    order2 = oms.create_order(67890)
#    assert oms.get_order(order_id) == expected_result

@pytest.mark.parametrize("customer_id, expected_result", [(1,1),(2,1)])
def test_create_order(order_management_system, customer_id, expected_result):     
    assert order_management_system.create_order(customer_id) == expected_result    

"""
#Ответ к заданию
@pytest.mark.parametrize("customer_id", [1, 2, 3])
def test_create_order(order_management_system, customer_id):
    order_id = order_management_system.create_order(customer_id)
    order = order_management_system.get_order(order_id)
    assert order is not None
    assert order.customer_id == customer_id
    assert order.items == []   
"""
@pytest.mark.parametrize("customer_id, product_id, quantity", [(111,11,1),(222,22,2)])
def test_add_item_to_order(order_management_system,customer_id, product_id, quantity):    
    order_id = order_management_system.create_order(customer_id)
    order_management_system.add_item_to_order(order_id, product_id, quantity)
    order = order_management_system.get_order(order_id)

    #print("\n--->>>>>>>>>>>>>>\n")
    #print(order.items)
    #print("\n------>>>>>>>>>>>>>>\n")

    assert order.items == [{"product_id": product_id, "quantity": quantity}]

"""
#Ответ к заданию
@pytest.mark.parametrize("customer_id, product_id, quantity", [
    (1, 1, 1),
    (2, 2, 3),
    (3, 1, 2),
])
def test_add_item_to_order(order_management_system, customer_id, product_id, quantity):
    order_id = order_management_system.create_order(customer_id)  # Создаем заказ
    order_management_system.add_item_to_order(order_id, product_id, quantity)
    order = order_management_system.get_order(order_id)
    assert order.items == [{"product_id": product_id, "quantity": quantity}]

"""
@pytest.mark.parametrize("customer_id, product_id, quantity", [(1001,33,1),(222,44,2)])
def test_update_item_quantity(order_management_system,customer_id,product_id,quantity):
     
    # Создаем заказ, добавляем продукт
    order_id =  order_management_system.create_order(customer_id)
    order_management_system.add_item_to_order(order_id, product_id, quantity)
    order = order_management_system.get_order(order_id)

    #Выполняем тестируемую функцию
    order_management_system.update_item_quantity(order_id, product_id, (quantity+10))
    #print("----->")
    #print(order.items)
    #print("----->")
    #Проверяем результат    
    assert order.items == [{"product_id": product_id, "quantity": (quantity+10)}]


"""
#Ответ к заданию
@pytest.mark.parametrize("customer_id, product_id, quantity", [
    (1, 1, 2),
    (2, 2, 1),
])
def test_update_item_quantity(order_management_system, customer_id, product_id, quantity):
    order_id = order_management_system.create_order(customer_id)  # Создаем заказ
    order_management_system.add_item_to_order(order_id, product_id, 1)  # Добавляем товар
    order_management_system.update_item_quantity(order_id, product_id, quantity)
    order = order_management_system.get_order(order_id)
    assert order.items == [{"product_id": product_id, "quantity": quantity}]
"""


@pytest.mark.parametrize("customer_id, product_id, quantity", [(2001,55,1),(2002,66,2)])
def test_remove_item_from_order(order_management_system,customer_id,product_id,quantity):
     
    # Создаем заказ, добавляем продукт
    order_id =  order_management_system.create_order(customer_id)
    order_management_system.add_item_to_order(order_id, product_id, quantity)
    order = order_management_system.get_order(order_id)

    #print("-----")
    #print(order.items)
    #print("-----")

    #Выполняем тестируемую функцию
    order_management_system.remove_item_from_order(order_id, product_id)
    
    #print("----->>")
    #print(order.items)
    #print("----->>")
    #Проверяем результат 

    #Проверяем результат    
    assert len(order.items) == 0
    #or
    assert (order.items) == []

"""
#Ответ к заданию
def test_remove_item_from_order(order_management_system, customer_id, product_id):
    order_id = order_management_system.create_order(customer_id)  # Создаем заказ
    order_management_system.add_item_to_order(order_id, product_id, 1)  # Добавляем товар
    order_management_system.remove_item_from_order(order_id, product_id)
    order = order_management_system.get_order(order_id)
    assert order.items == []
"""

@pytest.mark.parametrize("customer_id,product_id,quantity", [(10007,90004,300),(10008,90005,400)])
def test_cancel_order(order_management_system,customer_id,product_id,quantity):
    order_id = order_management_system.create_order(customer_id)
    order_management_system.add_item_to_order(order_id,product_id,quantity)
    order = order_management_system.get_order(order_id)

    assert order is not False
    
    order_management_system.cancel_order(order_id)

    #Проверяем результат    
    assert len(order.items) == 0
    #or
    assert (order.items) == []



"""
#Ответ к заданию
@pytest.mark.parametrize("customer_id", [1, 2, 3])
def test_cancel_order(order_management_system, customer_id):
    order_id = order_management_system.create_order(customer_id)  # Создаем заказ
    order_management_system.add_item_to_order(order_id, 1, 1)  # Добавляем товар
    order_management_system.cancel_order(order_id)
    order = order_management_system.get_order(order_id)
    assert order.items == []
"""