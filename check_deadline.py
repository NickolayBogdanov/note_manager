import datetime

created_date = datetime.datetime.today() # текущая дата
print(f"Дата создания заметки: {created_date.strftime("%d-%m-%Y")}")  # выводим дату в нужный формат
temp_created_date = (f"Дата создания заметки: {created_date.strftime("%d-%m")}")

while True:
    try:
        issue_date = input("Введите дату истечения заметки в формате \"дд-мм-гггг\": ")# получаем от пользователя дату
        issue_date = (datetime.datetime.strptime(issue_date, "%d-%m-%Y"))  # конвертируем дату в объект
        temp_issue_date = f"Дата создания заметки: {issue_date.strftime("%d-%m")}"  # выводимая пользователю информация в удобном формате
        break
    except (ValueError):
        print("Неверный формат, попробуйте снова.")


def scss():
    dead_line = issue_date - created_date
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
