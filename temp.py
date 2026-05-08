
import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2

#v1 - работает на рабочем ПК, не работает на домашнем. Вероятно проблемы с версиями.
# Получаем содержимое страницы
#url = 'https://ru.wikipedia.org/wiki/Города-миллионеры_России'
#response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#response.raise_for_status()

# Парсим HTML
#soup = BeautifulSoup(response.content, 'html.parser')

# Находим нужную таблицу по ID
#table = soup.find(id="mwFw")
#if table is None:
#    raise ValueError("Таблица с id='mwFw' не найдена на странице")

# Конвертируем в строку и читаем через read_html
#table_html = str(table)
#table_df = pd.read_html(table_html)[0]

#print(table_df.info())