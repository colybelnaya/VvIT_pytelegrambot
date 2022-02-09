import telebot
from telebot import types
token = "5108856844:AAFG1kpNaEjzr3aNA2Jl1c-i_1KGZ3f8hLE"
bot = telebot.TeleBot(token)
 
@bot.message_handler(commands=['start'])
def start(message):
   keyboard = types.ReplyKeyboardMarkup()
   keyboard.row("Хочу", "/help")
   bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
   
@bot.message_handler(commands=['help'])
def start_message(message):
   bot.send_message(message.chat.id, 'Я могу рассказать тебе один анекдот (команда /anek) и выдать гороскоп (команда /deb)')
 
@bot.message_handler(commands=['anek'])
def start_message(message):
   bot.send_message(message.chat.id, 'Купил мужик шляпу а она ему как раз')
 
@bot.message_handler(commands=['deb'])
def start_message(message):
   bot.send_message(message.chat.id, 'goroskop.ru')
 
@bot.message_handler(content_types=['text'])
def answer(message):
   if message.text.lower() == "хочу":
       bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
   if message.text.lower() == "как дела?":
       bot.send_message(message.chat.id, 'Конечно супер!')
   if message.text.lower() == "пока":
       bot.send_message(message.chat.id, 'До свидания!')
 
bot.infinity_polling()
