#M4-2-L8 functools

#Задание Extra.1
from functools import lru_cache

@lru_cache
def calculate_factorial(n):
    """Функция вычисляет факториал числа n."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

@lru_cache
def fibonacci(n):
    """Функция вычисляет число Фибоначчи для n."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@lru_cache
def calculate_power(base, exponent):
    """Функция вычисляет значение степени числа base в степени exponent."""
    return base ** exponent

#Задание Extra.2

"""
Ваша задача — создать переменную form_post_request, которая будет ссылаться на новую функцию, порожденную от form_request
со статическим значением параметра method равным ‘POST’(c помощью functools.partial).
"""
from functools import partial

def form_request(url, method='GET', headers=None, data=None, params=None):
    dict_ = {"headers": headers,
           "data": data,
           "params": params}
    return f"{url}-::-{method}-::-{dict_}"

form_post_request = partial(form_request,method='POST' )

print(form_post_request('dummy_api'))
# dummy_api-::-POST-::-{'headers': None, 'data': None, 'params': None}


#Задание Extra.3
print("\n---------->")

"""
Для этого реализуйте функцию calculate_total_price, которая будет принимать список словарей,
представляющих товары в корзине, и возвращать общую стоимость всех товаров. 
"""
from functools import reduce
def calculate_total_price(cart):
    #print(cart)
    total_price = reduce(lambda sum,price: sum + price['price'], cart,0)
    return total_price


cart = [
    {'product_name': 'Мышка', 'price': 15.99},
    {'product_name': 'Клавиатура', 'price': 25.50},
    {'product_name': 'Наушники', 'price': 10.75}
]

total_price = calculate_total_price(cart)
print(f"Общая стоимость товаров в корзине: ${total_price:.2f}")
# Общая стоимость товаров в корзине: $52.24