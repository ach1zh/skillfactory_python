#M12-L2

'''
HTTP response status codes
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
'''


"""

import requests
 
 
r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)

#r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.status_code)  # узнаем статус полученного ответа

#r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
#print(r.content)

print("--->")

import requests
import json  # импортируем необходимую библиотеку
 
 
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных
 
for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль, оставим только первые 50 символов.
    #print(text[:50], '\n')
    print(text)


r = requests.get('https://api.github.com') 
print(r.content)

print("--->")

import requests
import json
 
 
data = {'key': 'value'}
 
r = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON 
print(r.content)
"""

#Задание 5.2.3
print("\n--> Задание 5.2.3 -->\n")

'''
Напишите программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис).
Выведите первый из сгенерированных текстов.
'''
import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# делаем из полученных байтов Python-объект для удобной работы
data_baconipsum = json.loads(r.content)
print(data_baconipsum[0])