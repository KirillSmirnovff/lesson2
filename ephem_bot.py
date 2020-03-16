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

import random

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

cities_list = ['Москва', 'Архангельск', 'Курск', 'Кострома']
game_list = []
uses_cities_list = []


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

def cities (bot, update):
    user_city = update.message.text.split()[1].capitalize()

    if user_city not in cities_list:
        update.message.reply_text(f'Города "{user_city}" я не знаю или он уже был, попробуй другой город.')
    else:
        cities_list.remove(user_city)
        answer_list = []
        for city in cities_list:
            if user_city[len(user_city) - 1].capitalize() == city[0]:
                answer_list.append(city)
        if answer_list == []:
            update.message.reply_text(f'Больше городов на букву "{user_city[len(user_city) - 1].capitalize()}" я не знаю, ты победил!')    
        else:
            answer_city = random.choice(answer_list)
            update.message.reply_text(f'"{answer_city}". Твоя очередь. Город на букву "{answer_city[len(answer_city) - 1]}"')
            cities_list.remove(answer_city)
        
def calculator(bot,update):
    user_request = update.message.text.replace(' ','')[5:]
    print(user_request)
    numbers = user_request.replace('+',' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
    print(numbers)
    if '+' in user_request:
        update.message.reply_text(f'{int(numbers[0])+int(numbers[1])}')
    elif '-' in user_request:
        update.message.reply_text(f'{int(numbers[0])-int(numbers[1])}')
    elif '*' in user_request:
        update.message.reply_text(f'{int(numbers[0])*int(numbers[1])}')
    elif '/' in user_request:
        update.message.reply_text(f'{int(numbers[0])/int(numbers[1])}')
    

 

def main():
    mybot = Updater('934801973:AAFR-ybwGVkb46UUZPJaYxv1jMNfpWK13tY', request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_position))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("nextfullmoon", next_full_moon))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(CommandHandler("calc", calculator))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
