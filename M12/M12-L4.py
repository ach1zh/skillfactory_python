#M12-L4

#Задание 5.4.4
print("\n--> Задание 5.4.4 -->\n")

"""
Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
"""

'''
import requests
import lxml.html
from lxml import etree

tree = etree.parse("M12\M12-L4.html", lxml.html.HTMLParser())
text = tree.xpath('/html/body/tag1/tag2/text()')
print(text)

tag2 = tree.find("/body/tag1/tag2")
print(tag2.text)
'''

#Задание 5.4.5
print("\n--> Задание 5.4.4 -->\n")

'''
допишите сделанный в начале юнита скрипт (где мы доставали заголовки новостей о Python с Python.org) так, 
чтобы он показывал ещё и дату добавления новости.
Примечание: для получения атрибутов тега (т. е. его дополнительных параметров) используется метод .get(<имя атрибута>).
'''

import requests
import lxml.html
from lxml import etree
import time
'''
# Получаем HTML-код страницы
#web_site_html = requests.get('https://www.python.org/').content
web_site_html = requests.get('https://www.python.org/').text

# Парсим HTML из строки
tree = lxml.html.document_fromstring(web_site_html)

# Помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей.
# (Все заголовки и их даты)  
ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тег <a>)
    print(a.text)  # из этого тега забираем текст, это и будет нашим названием


# Пример использования: находим заголовок страницы
#title = tree.xpath('//title/text()')
#print(title[0] if title else "Заголовок не найден")

 '''


tree = etree.parse('M12\M12-L4_python_org_HTML.html', lxml.html.HTMLParser())

ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')
for li in ul:
    a_attr = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тег <a>)
    
    print(a_attr.text)  # из этого тега забираем текст, это и будет нашим названием
    print(a_attr.get('href'))        
    time_attr = li.find('time').get('datetime')
    print(str(time_attr).split("T")[0])
    print("---")

    #print(time_attr.get('datetime'))

    #/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[2]/time
    #//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[2]/time