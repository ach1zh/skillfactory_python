#M14-L2
# src/order_management_system.py

class Order:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.items = []
        
    def add_item(self, product_id, quantity):
        self.items.append({"product_id": product_id, "quantity": quantity})

    def update_item_quantity(self, product_id, quantity):
        for item in self.items:
            if item["product_id"] == product_id:
                item["quantity"] = quantity
                return
        raise ValueError("Товар не найден в заказе.")

    def remove_item(self, product_id):
        for item in self.items:
            if item["product_id"] == product_id:
                self.items.remove(item)
                return
        raise ValueError("Товар не найден в заказе.")

    def cancel(self):
        self.items = []


class OrderManagementSystem:
    def __init__(self):
        self.orders = {}

    def create_order(self, customer_id):
        order_id = len(self.orders) + 1
        self.orders[order_id] = Order(customer_id)
        return order_id

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def add_item_to_order(self, order_id, product_id, quantity):
        order = self.get_order(order_id)
        if order is None:
            raise ValueError("Заказ не найден.")
        order.add_item(product_id, quantity)

    def update_item_quantity(self, order_id, product_id, quantity):
        order = self.get_order(order_id)
        if order is None:
            raise ValueError("Заказ не найден.")
        order.update_item_quantity(product_id, quantity)

    def remove_item_from_order(self, order_id, product_id):
        order = self.get_order(order_id)
        if order is None:
            raise ValueError("Заказ не найден.")
        order.remove_item(product_id)

    def cancel_order(self, order_id):
        order = self.get_order(order_id)
        if order is None:
            raise ValueError("Заказ не найден.")
        order.cancel()