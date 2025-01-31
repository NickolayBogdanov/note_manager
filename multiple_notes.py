
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
# функция ввода заголовка
def add_title():
    stop = True
    while stop == True:
        notes[-1]["title"] = input("Введите заголовок: ") # присвоение значения
        for i in range(len(notes[0:-1])):
            for k in notes[i].values():
                if str.upper(notes[i]) == str.upper(notes[-1]):
                    print("Такой заголовок уже существует, введите уникальный заголовок.")
                    stop = True
                else:
                    stop = False

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
            if  status is None:
                print("неверно введено значение") # проверка правельности ввода значений
            else:
                notes[-1]["status"] = status
                print("Стаус успешно изменен, текущий статус: ", (status))
                break # завершение цикла при правельном вводе
        except ValueError: # страховка от ошибки, при введении некорректных данных
            print("Неверный формат, попробуйте снова")

#-----------------------------------------------------------------------------------------------------------------------

# функция ввода даты
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
            notes.append(dict()) # создание нового словаря
            notes[-1]["username"] = input("Введите ваше имя: ")
            add_title()
            notes[-1]["content"] = input('Введите заметку: ')
            add_status()
            add_date()
            print("Заметка создана успешно!")
        else:
            print("Неверно введено значение, попробуйте снова.")
    except ValueError:
        print("Неверный формат, попробуйте снова.")

print(notes)

