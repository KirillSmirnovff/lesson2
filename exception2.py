"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
из урока про функции так, чтобы она перехватывала исключения,
когда переданы некорректные аргументы (например, строки вместо чисел).
    
"""
phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65000, 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000, 'discount': 10 }

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except(ValueError,TypeError):
        return'Введите корректные данные'
            

dis_iphone = discounted(phone1['price'], phone1['discount'])
print(dis_iphone)
dis_android = discounted(phone2['price'], phone2['discount'])
print(dis_android)
