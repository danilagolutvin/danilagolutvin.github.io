import requests
import random
import telebot

from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good'
API_KEY = '5704988815:AAF1pgjBajm7JpwpdtWA71WUmZIS0d9-UHs'


def parser(url):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Для вызова анекдота набери любую цифру:')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Ты рофлишь? Введи блять любую цифру.')

bot.polling()
