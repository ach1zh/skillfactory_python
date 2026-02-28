# M12_L6_HW_03
# Итоговое задание 5.6.1 (PJ-02)# 
# Telegram-бот
# Чижов А.С.

'''
Python 3.13.7
cd M:\YandexDisk\-Sync-\Dev\python_projects\skillfactory_python\M12\crypto_bot
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
.\venv\Scripts\activate
pip3 install pyTelegramBotAPI
pip show pyTelegramBotAPI
pip3 install requests

coindesk.com
https://developers.coindesk.com/settings/api-keys
***
***

skillfactory_hw
#API_KEY = '***'
#https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,RUB
'''

import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter
#M12\crypto_bot\config.py


bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' или '/help'
@bot.message_handler(commands=['start', 'help'])
def handle_help(message):
    text = 'Список доступных команд: /help\nСписок доступных валют: /values\n Для конвертация валюты введите запрос в следующем формате:\n<валюта_из> <валюта_в> <количество>'
    bot.reply_to(message,text)

# Обрабатываются все сообщения, содержащие команду '/values'
@bot.message_handler(commands=['values'])
def handle_values(message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key))     
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])  
def covert(message: telebot.types.Message):
    try:    
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException("Ошибка обработки параметров")
        
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:    
        text = f"Цена {amount} {quote} в {base} - {total_base}"    
        bot.send_message(message.chat.id, text)

#Запуск бота
bot.polling(none_stop=True)

"""
доллар рубль 1
крузейро юань 100
"""