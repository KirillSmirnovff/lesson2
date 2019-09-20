from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
def name_count():

    names = {}
    for name in students:
        if name['first_name'] not in names:
            names[name['first_name']] = 1
        else:
            names[name['first_name']] += 1
    return names
names_repeat = name_count()
for each_name in names_repeat:
    print(f'{each_name}: {names_repeat[each_name]}')
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names = []
for name in students:
    names.append(name['first_name'])
def most_frequent(names_list):
    most_counter = 0
    most_freq_name = names_list[0]
    for word in names_list:
        current_freq = names_list.count(word)
        if current_freq > most_counter:
            most_counter = current_freq
            most_freq_name = word
    return most_freq_name
print(f'Самое частое имя среди учеников: {most_frequent(names)}')
            



# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

names_first_class = []
names_second_class = []
for name in school_students[0]:
    names_first_class.append(name['first_name'])
print(f'Самое частое имя в классе 1: {most_frequent(names_first_class)}')
for name in school_students[1]:
    names_second_class.append(name['first_name'])
print(f'Самое частое имя в классе 2: {most_frequent(names_second_class)}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
first_class = school[0]
second_class = school[1]

def current_class_names(current_class):

    current_class_names = current_class['students']
    current_class_names_list =[]
    for current_class_name in current_class_names:
        current_class_names_list.append(current_class_name['first_name'])
        girls_count = 0
        boys_count = 0
    for name in current_class_names_list:
        if name in is_male:
            if is_male[name] == False:
                girls_count += 1
            else:
                boys_count += 1
    return [current_class['class'], girls_count, boys_count]

current_class_index = current_class_names(first_class)[0]
girls_count = current_class_names(first_class)[1]
boys_count = current_class_names(first_class)[2]

print(f'В классе {current_class_names(first_class)[0]} {current_class_names(first_class)[1]} девочки и {current_class_names(first_class)[2]} мальчика.')
print(f'В классе {current_class_names(second_class)[0]} {current_class_names(second_class)[1]} девочки и {current_class_names(second_class)[2]} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
first_class = school[0]
second_class = school[1]

current_class_index = current_class_names(first_class)[0]
if current_class_names(first_class)[1] < current_class_names(first_class)[2]:
    print(f'Больше всего мальчиков в классе {current_class_index}')
else:
    print(f'Больше всего девочек в классе {current_class_index}')

current_class_index = current_class_names(second_class)[0]
if current_class_names(second_class)[1] < current_class_names(second_class)[2]:
    print(f'Больше всего мальчиков в классе {current_class_index}')
else:
    print(f'Больше всего девочек в классе {current_class_index}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a