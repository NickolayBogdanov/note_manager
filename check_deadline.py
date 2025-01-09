import datetime

today_date = datetime.datetime.today() # текущая дата
print(f"Дата создания заметки: {today_date.strftime("%d-%m-%Y")}")  # выводим дату в нужный формат

while True:
    try:
        issue_date = input("Введите дату истечения заметки в формате \"дд-мм-гггг\": ")# получаем от пользователя дату
        issue_date = (datetime.datetime.strptime(issue_date, "%d-%m-%Y"))  # конвертируем дату в объект
        break
    except (ValueError):
        print("Неверный формат, попробуйте снова.")


def scss(): # функция сравнения даты создания и даты истечения заметки
    dead_line = issue_date - today_date
    if dead_line.days == 1:
        print(f"До истечения заметки осталось {dead_line.days} день.")
    if dead_line.days == 2 or dead_line == 3 or dead_line == 4:
        print(f"До истечения заметки осталось {dead_line.days} дня.")
    if dead_line.days > 4:
        print(f"До истечения заметки осталось {dead_line.days} дней.")
    if dead_line.days == 0:
        print("Заметка истекает сегодня")
    if dead_line.days < 0:
        print("Срок заметки истек")


scss()
