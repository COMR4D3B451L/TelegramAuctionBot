import os, requests
from telebot import TeleBot, types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = TeleBot(API_KEY)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'ابدء', 'ابدي'])
def send_welcome(message):
    print(message.from_user.id)
    print(message.from_user.username)
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['test'])
def test(message):
    photo = open('./tmp/56.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    
@bot.message_handler(commands=['test2'])
def key(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    
    
@bot.message_handler(commands=['api'])
def key(message):
    response = requests.get('http://localhost:8000/')
    response.raise_for_status()
    data = response.json()
    
    bot.send_message(message.chat.id, data['message'])
    
    
    
bot.polling()