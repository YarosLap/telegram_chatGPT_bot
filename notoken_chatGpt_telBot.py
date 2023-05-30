import openai
import telebot

openai.api_key = ''
bot = telebot.TeleBot('')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Как я могу Вам помочь?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Расскажи мне о ' + message.text + '?',
        max_tokens=3500,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response["choices"][0]["text"])

bot.polling()
