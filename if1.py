"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную 
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = abs(int(input('Введите ваш возраст : ')))
    
    if user_age < 2:
        print ('Вам еще рано куда-то отправляться!')
    elif 2 <= user_age < 7:
         print ('Пора ходить в садик')
    elif 7 <= user_age < 18:
        print ('Вам впору ходить в школу')
    elif 18 <= user_age < 23:
        print ('В этом возрасте желательно учиться в ВУЗе')
    elif 23 <= user_age < 70:
        print ('Взрослая жизнь в разгаре - надо ходить на работку')
    else:
        print ('Пора на пенсию!')
 
 
 
if __name__ == "__main__":
    main()
    
