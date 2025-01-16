

notes = [

    {
        "username": "Павел",
        "title": "Дела на завтра",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '11-01-25',
        "issue_date": '12-01-25',
    },
    {
        "username": "Павел",
        "title": "Дела на послезавтра",
        "content": "вынести мусор, погулять с собакой",
        "status": "В процессе",
        "created_date": '11-01-25',
        "issue_date": '12-01-25',
    },
    {
        "username": "Николай",
        "title": "Учеба",
        "content": "Взять книги в библиотеке",
        "status": "В процессе",
        "created_date": '11-01-25',
        "issue_date": '20-01-25',
    }
]
#-----------------------------------------------------------------------------------------------------------------------
def update_status():
    global status
    status_base = {1: "Выполнено", 2: "В процессе", 3: "Отложено"} # предусмотренные статусы
    print("выберите статус заметки: 1 - выполнено, 2 - в процессе, 3 - отложено")
    while True:
        try:
            status = status_base.get(int(input("Выберите статус заметки \"1\", \"2\" или \"3\": ")))
            if  status != status_base.get(1) and status != status_base.get(2) and status != status_base.get(3):
                status_base = {1: "Выполнено", 2: "В процессе", 3: "Отложено"}
                print("неверно введено значение")
            else:
                break
        except ValueError:
            print("Неверный формат, попробуйте снова.")

#-----------------------------------------------------------------------------------------------------------------------

def date():
    import datetime
    global issue_date
    while True:
        try:
            issue_date = input("Введите дату истечения заметки в формате \"дд-мм-гггг\": ")# получаем от пользователя дату
            issue_date = (datetime.datetime.strptime(issue_date, "%d-%m-%Y"))  # конвертируем дату в объект
            break
        except (ValueError):
            print("Неверный формат, попробуйте снова.")

#-----------------------------------------------------------------------------------------------------------------------

def yes_no():
    global y_n
    while True:
        y_n = input("Выберите: \"да\" \"нет\": ")
        try:
            if y_n == "да":
                break
            elif y_n == "нет":
                break
            else:
                print("Неверно введено значение, попробуйте снова.")
        except ValueError:  # страховка от ошибок
            print("Неверный формат введенного значения, попробуйте снова.")

def update_note():
    print("Текущие заметки:")
    print(notes)
    update = ["1 - username", "2 - title", "3 - content", "4 - status", "5 - issue_date"]
    search = input("Введите заголовок заметки которую желаете изменить: ")# переменная для сравнения
    for i in range(len(notes)):  # цикл переборщик для поиска и сравнения
        for k in notes[i].values():
            if str.upper(k) == str.upper(search):  # действия в случае совпадения
                print("Найдены следующие заметки:")
                print(notes[i].items())
                while True:
                    print(*update)
                    replace = input('Выберите поле для внесения изменений \"1\" \"2\" \"3\" \"4\" \"5\": ')
                    if replace == "1":
                        notes[i]["username"] = input("Введите новое имя: ")
                        print("Имя успешно изменено.")
                        print(notes[i])
                        print("Продолжить вносить изменения?")
                        yes_no()
                        if y_n == "да":
                            continue
                        else:
                            break
                    elif replace == "2":
                        notes[i]["title"] = input("Введите новый заголовок: ")
                        print("Заголовок успешно изменен.")
                        print(notes[i])
                        print("Продолжить вносить изменения?")
                        yes_no()
                        if y_n == "да":
                            continue
                        else:
                            break
                    elif replace == "3":
                        notes[i]["content"] = input("Введите текст заметки: ")
                        print("Заметка успешно изменена.")
                        print(notes[i])
                        print("Продолжить вносить изменения?")
                        yes_no()
                        if y_n == "да":
                            continue
                        else:
                            break
                    elif replace == "4":
                        update_status()
                        notes[i]["status"] = str(status)
                        print("Статус заметки успещно изменен.")
                        print(notes[i])
                        print("Продолжить вносить изменения?")
                        yes_no()
                        if y_n == "да":
                            continue
                        else:
                            break
                    elif replace == "5":
                        date()
                        notes[i]["issue_date"] = str(issue_date)
                        print("Дата истечения заметки успешно изменена.")
                        print(notes[i])
                        print("Продолжить вносить изменения?")
                        yes_no()
                        if y_n == "да":
                            continue
                        else:
                            break
                    else:
                        print("Неверное значение. Выберите из предложенного списка.")





update_note()