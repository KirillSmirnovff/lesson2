"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

from datetime import datetime,date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Приветствую!'
    print(text)
    update.message.reply_text(text)

def planet_position(bot, update):
    current_date = date.today().strftime('%Y/%d/%m')
    user_planet = update.message.text.split()[1]
    planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn','Uran','Neptune', 'Pluto'] # Проверка правильности ввода, чтобы в else вывести ответ при неправильном вводе. 
    if user_planet in planet_list:
        planet = getattr(ephem, user_planet)
        planet = planet(current_date)
        update.message.reply_text(ephem.constellation(planet))
    else:
        update.message.reply_text('Где сегодня эта планета - мне неизвестно :(')


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def wordcount(bot, update):
    user_words = update.message.text.replace(',',' ').split()[1:]
    user_words_len = len(user_words)
    update.message.reply_text('Количество слов: {}'.format(user_words_len))

def next_full_moon (bot, update):
    user_date = update.message.text.split()[1]
    print(user_date)
    user_date = datetime.strptime(user_date, '%Y%d%m').date()
    update.message.reply_text('Дата следующего полнолуния : {}'.format(ephem.next_full_moon(user_date)))

 

def main():
    mybot = Updater('934801973:AAFR-ybwGVkb46UUZPJaYxv1jMNfpWK13tY', request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_position))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("nextfullmoon", next_full_moon))
   

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
