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
    def school_scores_avg():

        score_count_all = 0
        score_sum_all = 0
        
        for student_scores in school_info:
            scores_sum = 0
           
            for score in student_scores['scores']:
                scores_sum += score
            score_sum_all += scores_sum
            score_count_all += len(student_scores['scores'])
            scores_avg = scores_sum/len(student_scores['scores'])
            print(f"Средняя оценка по {student_scores['school_class']} классу: {scores_avg}")
        
        scores_avg_all = score_sum_all/score_count_all
        print(f"Средняя оценка по всей школе: {scores_avg_all}")
    school_scores_avg()


    
if __name__ == "__main__":
    main()
