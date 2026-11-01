import json
import time

# функция расчёта средней оценки фильма и кол-ва уникальных пользователей в отзывах, на входе .json файл, на выходе .txt файл с рез-ми
def assessment(input_file_name, output_file_name):
    
    start_time = time.time()
    
    # читаем файл .json
    with open(input_file_name, "r") as file:
        data = json.load(file)  

    score = [] # вводим список для сбора оценок
    users = set() # вводим множество для сбора имён пользователей (сохраняются только уникальные)
    error = 0 # вводим счётчик ошибок в отзывах
    duplicate = 0 # вводим счётчик дубликатов - отзывов от одного пользователя
    
    for element in data: # element - это словарь из 2 ключей и их значений. {"user": "Alex469904", "rating": 3}
        
        # проверяем наличие обоих ключей (в отзыве есть и имя пользователя, и оценка)
        try:
            rating = element["rating"]
            user = element["user"]
        except:
            error += 1
            continue
        
        # для правильности считаем среднюю оценку только уникальных пользователей (при повторной оценке пользователем мы учитываем первую - первое слово дороже :) )
        if user in users:
            duplicate += 1
        else:
            score.append(rating)
        
        users.add(user)
    
    
    # проверка ошибки деления на 0, если оценок в списке нет и далее поиск средней оценки
    if len(score) != 0:
        avg_score = sum(score) / len(score)
    
    # составляем отчет
    report = (
        f"Средняя оценка фильма {avg_score}\n"
        f"Количество уникальных пользователей, оценивших фильм - {len(users)}\n"
        f"Неверно составленных отзывов - {error}\n"
        f"Дубликатов отзывов (количество оценок, оставленных несколько раз одним пользователем) - {duplicate}"
    )
    
    # сохраняем отчёт в .txt файле
    with open(output_file_name, "w", encoding="utf8") as report_file:
        report_file.write(report)
    
    end_time = time.time() - start_time
    
    print("="*75)
    print(f"Файл с отчётом успешно сохранён, затраченное время - {end_time} секунд")
    print("="*75)

assessment("reviews.json", "report.txt")