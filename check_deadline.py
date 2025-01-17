import datetime


today_date = datetime.datetime.today() # текущая дата
print(f"Текущая дата: {today_date.strftime("%d-%m-%Y")}")  # выводим дату в нужный формат


while True:
    try:
        issue_date = input("Введите дату истечения заметки в формате \"дд-мм-гггг\": ")# получаем от пользователя дату
        issue_date = (datetime.datetime.strptime(issue_date, "%d-%m-%Y"))  # конвертируем дату в объект
        break
    except (ValueError):
        print("Неверный формат, попробуйте снова.")


def scss(): # функция сравнения даты создания и даты истечения заметки
    dead_line = issue_date - today_date
    if dead_line.days < -4:
        print(f"Заметка истекла {dead_line.days} дней назад.")
    elif dead_line.days > -5 and dead_line.days < -1:
        print(f"Заметка истекла {dead_line.days} дня назад.")
    elif dead_line.days == -1:
        print(f"Заметка истекла {dead_line.days} день назад.")
    elif dead_line.days == 0:
        print("Заметка истекает сегодня")
    elif dead_line.days == 1:
        print(f"До истечения заметки осталось {dead_line.days} день.")
    elif dead_line.days < 5:
        print(f"До истечения заметки осталось {dead_line.days} дня.")
    else:
        print(f"До истечения заметки осталось {dead_line.days} дней.")



scss()
