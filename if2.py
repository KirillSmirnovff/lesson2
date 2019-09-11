"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def string_compare(string_one, string_two):
        if type(string_one) is not str or type(string_two) is not str:
            return '0'
        else:
            if string_one == string_two:
                return '1'
            elif len(string_one) > len(string_two):
                return '2'
            elif string_two == 'learn':
                return '3'
            else:
                return 'Этот случай не предусмотрен'
    print(string_compare(1,'100'))
    print(string_compare('1','100'))
    print(string_compare('100','100'))
    print(string_compare('1000','100'))
    print(string_compare('1','learn'))
    
if __name__ == "__main__":
    main()
