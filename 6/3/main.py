# https://pypi.org/project/pyTelegramBotAPI/
# https://habr.com/ru/post/580408/


import telebot
from gtts import gTTS
import os
from telebot import types

TOKEN = "1256196990:AAGCalknYpBNEhXD5KTSrbe6xBOCNZy4jRQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет ✌️  qwe")


@bot.message_handler(commands=['hello'])
def hello(message):
    text = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(commands=['audio'])
def audio(message):
    text = message.text.replace("/audio ", "")
    voice_path = f'{message.from_user.id}.MP3'

    speech = gTTS(text=text, lang='ru', slow=False)
    speech.save(voice_path)

    bot.send_audio(message.chat.id, audio=open('/Users/genrikh.metlov/Projects/python/6/3/' + voice_path, 'rb'))
    os.remove(voice_path)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Мои заметки")
    item2 = types.KeyboardButton("Кнопка 2")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text.upper() == "Мои заметки".upper():
        bot.send_message(message.chat.id, """
            - Заметка 1
            - Заметка 2
            - Заметка 3
        """, parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


bot.infinity_polling()