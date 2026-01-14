#M9-L3

#Задание 21.8.1 (External resource)
print("\nЗадание 21.8.1 (External resource) -->\n")

class SellItem:
    def __init__(self, name: str, price):
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name, price, material, square):
       super().__init__(name,price)
       self.material = material
       self.square = square

class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name,price)
        self.size = size
        self.rooms = rooms
        
class Agency:
    def __init__(self, name):
        self.name = name
        self.objs = []

    def add_object(self, obj):
        self.objs.append(obj)

    def remove_obj(self, obj):
        self.objs.remove(obj)

    def get_objects(self):        
        return(self.objs)

#
# Создаём агентство недвижимости
real_estate_agency = Agency("Best Homes Agency")

# Создаём объекты недвижимости
house1 = House(name="Уютный дом", price=200000, material="Кирпич", square=150)
flat1 = Flat(name="Современная квартира", price=100000, size=80, rooms=2)

# Добавляем объекты недвижимости в агентство
real_estate_agency.add_object(house1)
real_estate_agency.add_object(flat1)

# Получаем список доступных объектов недвижимости
properties = real_estate_agency.get_objects()

for p in properties:
   print(type(p), p.__dict__)

# <class '__main__.House'> {'name': 'Уютный дом', 'price': 200000, 'material': 'Кирпич', 'square': 150}
# <class '__main__.Flat'> {'name': 'Современная квартира', 'price': 100000, 'size': 80, 'rooms': 2}
