"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user()из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    dictionary = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'Как тебя зовут?': 'Просто программа'}
    while True:
        try:
            user_say = input('\n')
            if user_say in dictionary:
                 print(dictionary[user_say])
            elif user_say == 'Пока':
                print('Ну пока')
                break
            else:
                print('Не понимаю')
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    ask_user()
