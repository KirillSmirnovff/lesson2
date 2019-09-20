"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_info = [
        {'school_class' : '4а', 'scores': [3,4,4,5,2]},
        {'school_class' : '4б', 'scores': [5,4,4,5,5]},
        {'school_class' : '5a', 'scores': [3,4,3,4,3]},
        {'school_class' : '5б', 'scores': [4,4,4,4,4]}
]

    for student_scores in school_info:
        avg_score_each_class = sum(student_scores['scores'])/len(student_scores['scores'])
        print (f"Средняя оценка по {student_scores['school_class']} классу: {avg_score_each_class}")
        avg_scores_all_school += avg_score_each_class
    print (f"Средняя оценка по всей школе: {avg_scores_all_school/len(school_info)}")

    
if __name__ == "__main__":
    main()
