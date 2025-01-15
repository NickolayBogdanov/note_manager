

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

def delete():
    while True:
        delete_title = input("Введите заголовок заметки которую желаете удалить: ")
        try:
            for i in range(len(notes)):  # цикл переборщик для поиска и сравнения
                for k in notes[i].values():
                    if str.upper(k) == str.upper(delete_title):  # действия в случае совпадения
                        notes.pop(i)
        except IndexError:
            print("Заметка успешно удалена!")
            break

#-----------------------------------------------------------------------------------------------------------------------

def delete_all():
    stop = True
    while stop == True:
        try:
            for i in range(len(notes)):  # цикл переборщик для поиска и сравнения
                for k in notes[i].values():
                    if str.upper(k) == str.upper(search):
                        stop = True
                        notes.pop(i)
                    else:
                        stop = False
        except IndexError: # страховка от ошибки по индексу
            print(f"Заметка успешно удалена")
            stop = True


#-----------------------------------------------------------------------------------------------------------------------
def searcher():
    print("Текущие заметки:")
    print(notes)
    global search
    search = input("Введите имя пользователя или заголовок заметки которую желаете удалить: ")# переменная для сравнения
    for i in range(len(notes)):  # цикл переборщик для поиска и сравнения
        for k in notes[i].values():
            if str.upper(k) == str.upper(search):  # действия в случае совпадения
                print("Найдены следующие заметки:")
                print(notes[i].items())
    while True:
        yes_no = input("Желаете удалить все найденые заметки? \"да\" \"нет\": ")
        try:
            if yes_no == "да":
                delete_all()
                print("Текущие заметки:")
                print(notes)
                break
            elif yes_no == "нет":
                delete()
                print("Текущие заметки:")
                print(notes)
                break
            else:
                print("Неверно введено значение, попробуйте снова.")
        except ValueError:
            print("Неверный формат введенного значения, попробуйте снова.")

#-----------------------------------------------------------------------------------------------------------------------
searcher()


