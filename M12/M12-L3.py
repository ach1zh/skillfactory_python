#M12-L3
'''
You can use this token to access HTTP API:
***
'''

'''
https://core.telegram.org/bots/api#chat
'''

import telebot

TOKEN = '***'

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass
 
# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

#Задание 5.3.1
print("\n--> Задание 5.3.1 -->\n")

'''
Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение с привязкой к пользователю.
'''

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['text',])
def handle_text(message):
    #bot.reply_to(message, "This is a message handler")
    #bot.send_message(message.chat.id, 'test-test')
    bot.send_message(message.chat.id, f"Привет {message.from_user.username} !")
    
    #print(message.from_user.username)
    print(message.chat.username)
    print(message.from_user.id)
    print(message.from_user.first_name)
    print(message.from_user.last_name)
    print(message.from_user.username)

'''
#Решение
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")
'''

#Задание 5.3.2
print("\n--> Задание 5.3.2 -->\n")

"""
Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
Бот должен отвечать не отдельным сообщением, а с привязкой к картинке.
"""

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['photo',])
def handle_photo(message):
    print("asdasdasd")
    bot.reply_to(message, "Nice meme XDD")
    #bot.send_message(message.chat.id, f"Nice meme XDD {message.from_user.username} !")

bot.polling(none_stop=True)

"""
#Решение
import telebot 
bot = telebot.TeleBot('TOKEN') 
@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')
bot.polling(none_stop=True)
"""