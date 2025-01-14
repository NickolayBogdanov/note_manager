import json
notes = []


#-----------------------------------------------------------------------------------------------------------------------
# функция ввода имени
def add_name():
    notes[-1].get("username") # добавление ключа
    notes[-1]["username"] = input("Введите ваше имя: ") # присвоение значения

#-----------------------------------------------------------------------------------------------------------------------
# функция ввода заголовка
def add_title():
    notes[-1].get("title") # добавление ключа
    notes[-1]["title"] = input("Введите заголовок: ") # присвоение значения

#-----------------------------------------------------------------------------------------------------------------------
# функция ввода заметки
def add_content():
    notes[-1].get("content") # добавление ключа
    notes[-1]["content"] = input('Введите заметку: ') # присвоение значения

#-----------------------------------------------------------------------------------------------------------------------
# функция назначения статуса
def add_status():
    notes[-1].get("status")
    while True:
        status_base = {1: "Выполнено", 2: "В процессе", 3: "Отложено"}  # предусмотренные статусы
        try:
            status = status_base.get(int(input(
                "Выберите статус заметки \"1\" - Выполнено, \"2\" - В процессе или \"3\" - Отложено: ")))
            # запрос данных от пользователя
            if  status != status_base.get(1) and status != status_base.get(2) and status != status_base.get(3):
                print("неверно введено значение") # проверка правельности ввода значений
            else:
                notes[-1]["status"] = status
                print("Стаус успешно изменен, текущий статус: ", (status))
                break # завершение цикла при правельном вводе
        except ValueError: # страховка от ошибки, при введении некорректных данных
            print("Неверный формат, попробуйте снова")

#-----------------------------------------------------------------------------------------------------------------------
# # функция ввода даты
def add_date():
    import datetime
    created_date = datetime.datetime.today()  # текущая дата
    while True:
        try:
            issue_date = input("Введите дату истечения заметки в формате \'дд-мм-гггг\': ")
            # получаем от пользователя дату
            issue_date = (datetime.datetime.strptime(issue_date, '%d-%m-%Y'))
            # конвертируем дату в объект
            break # завершение цикла при правельном вводе
        except (ValueError): # страховка от ошибки, при введении некорректных данных
            print("Неверный формат, попробуйте снова.")
    notes[-1]["created_date"] = str(created_date.strftime("%d-%m-%Y"))
    notes[-1]["issue_date"] = str(issue_date.strftime("%d-%m-%Y"))

#-----------------------------------------------------------------------------------------------------------------------
# цикл добавления заметок
while True:
    print('Добро пожаловать в "Менеджер заметок"')
    yes_no = input('Желаете добавить заметку? \"да\" \"нет\" : ')
    try:
        if yes_no == "нет":
            print("До новых встреч.")
            break
        elif yes_no == "да":
            notes.append(dict())  # создание нового словаря
            add_name()
            add_title()
            add_content()
            add_status()
            add_date()
            print("Заметка создана успешно!")
        else:
            print("Неверно введено значение, попробуйте снова.")
    except ValueError:
        print("Неверный формат, попробуйте снова.")
#-----------------------------------------------------------------------------------------------------------------------
print(notes)

