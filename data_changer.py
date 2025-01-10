import datetime


created_date = datetime.datetime.today() # текущая дата
print(f'''Дата создания заметки в формате \"дд-мм-гггг\":{created_date.strftime('%d-%m-%Y')}''') # выводим дату в нужный формат
while True:
    try:
        issue_date = input("Введите дату истечения заметки в формате \'дд-мм-гггг\': ")# получаем от пользователя дату
        issue_date = (datetime.datetime.strptime(issue_date, '%d-%m-%Y'))  # конвертируем дату в объект
        break
    except (ValueError):
        print("Неверный формат, попробуйте снова.")
temp_created_date = f"дата создания заметки: {created_date.strftime('%d-%m')}" # выводимая пользователю информация в удобном формате
temp_issue_date = f"дата создания заметки: {issue_date.strftime('%d-%m')}" # выводимая пользователю информация в удобном формате

print(created_date)
print(issue_date)
print(temp_created_date)
print(temp_issue_date)