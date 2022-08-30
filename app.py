from flask import Flask
import telebot

app = Flask(__name__)

@app.route('/')
def hello_world():

    bot = telebot.TeleBot("5606104004:AAHmj41cxFFm0eJMyHnnSRYA_Xgct7V9QvA", parse_mode=None)

    @bot.message_handler(commands=['Hi', 'Sikandar', "23"])
    def send_welcome(message):
        if message.text == "/Hi":
            bot.reply_to(message, "Hello, What is your name?")

        elif message.text == "/Sikandar":
            bot.reply_to(message, "What is your age?")

        elif message.text == "/23":
            bot.reply_to(message, "Hi Sikandar, Welcome to Telegram")

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.polling()

if __name__ == '__main__':
    app.run()
