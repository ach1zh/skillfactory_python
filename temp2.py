import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2

# Получаем содержимое страницы
url = 'https://ru.wikipedia.org/wiki/Города-миллионеры_России'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()

# Парсим HTML
soup = BeautifulSoup(response.content, 'html.parser')
# Находим нужную таблицу по ID
table = soup.find(id="mwFw")
if table is None:
    raise ValueError("Таблица с id='mwFw' не найдена на странице")

#Ручной парсинг таблицы
def parse_table_to_dataframe(table):
    """Парсит HTML-таблицу в DataFrame вручную"""
    # Извлекаем заголовки
    headers = []
    for th in table.find_all('th'):
        headers.append(th.get_text(strip=True))
    
    # Извлекаем строки
    rows = []
    for tr in table.find_all('tr')[1:]:  # пропускаем заголовок
        cells = tr.find_all(['td', 'th'])
        row = [cell.get_text(strip=True) for cell in cells]
        if len(row) == len(headers):  # проверяем, что строка полная
            rows.append(row)

    return pd.DataFrame(rows, columns=headers)

# Используем функцию
table_df = parse_table_to_dataframe(table)
print(table_df['Город'])
