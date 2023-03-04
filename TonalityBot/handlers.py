from bot import bot
from messages import *
from functions import *


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(commands=['tonality'])
def get_tonality(message):
    bot.send_message(message.chat.id, TONALITY_MESSAGE)


@bot.message_handler(content_types=['audio'])
def get_audio(message):
    bot.send_message(message.chat.id, THANKS_MESSAGE)
    bot.send_message(message.chat.id, f'{RESULT_MESSAGE}\n{define_tonality(message)}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
