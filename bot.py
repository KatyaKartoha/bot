from config import token
import random
import telebot

bot = telebot.TeleBot(token)


# Handle '/start' and '/help'

@bot.message_handler(commands=['motivation'])

def motive_handler(message):

    mot = ["Люди, которые достаточно сумасшедшие, чтобы думать, что они могут изменить мир — это те, кто действительно на это способен.", "Когда я освобождаюсь от того, кто я есть, я становлюсь тем, кем я могу быть.","В любой момент у нас есть два варианта: сделать шаг вперёд к росту или вернуться в безопасное место.", "Секрет перемен состоит в том, чтобы сосредоточиться на создании нового, а не на борьбе со старым."]
    n = random.choice(mot)
    bot.reply_to(message, n)
    print(len(mot))

@bot.message_handler(commands=['help', 'start'])

def send_welcome(message):
    #bot.reply_to(message, "Hi")
    bot.send_message(message.chat.id, "Hello")
 
@bot.message_handler(commands=['random'])

def random_handler(message):
    n = random.randint(1,100)
    bot.reply_to(message, f'случайное число - {n}')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(func=lambda message: True)

def echo_message(message):
    string = 'Ты сказал: ' + message.text
    bot.reply_to(message, string)
bot.infinity_polling()
