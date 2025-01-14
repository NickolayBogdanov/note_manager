

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
        "username": "Николай",
        "title": "Учеба",
        "content": "Взять книги в библиотеке",
        "status": "В процессе",
        "created_date": '11-01-25',
        "issue_date": '20-01-25',
    }

]

def delete():
    print("Текущие заметки:")
    print(notes)
    note_del = 0
    delete = input("Введите имя или заголовок заметки которую желаете удалить: ") # переменная для сравнения
    while True:
        for i in range(len(notes)): # цикл переборщик для поиска и сравнения
            for k in notes[i].values():
                if str.upper(k) == str.upper(delete): # действия в случае совпадения
                    ''' при удалении найденой заметки сразу, если она не в конце списка нарушается цикл и вылетает ошибка,
                    чтобы этого избежать переносим найденую заметку в конец списка'''
                    note_del = notes[i]
                    notes.append(note_del)
                    notes.pop(i)

        if note_del == 0:
            print("заметка не найдена.")
            break
        else:
            yes_no = input(f'Уверены, что хотите удалить: {note_del["title"]}  \"да\" \"нет\" : ')
            try:
                if yes_no == "нет":
                    print("До новых встреч.")
                    break
                elif yes_no == "да":
                    notes.pop(-1)
                    print("Заметка удалена. Остались следующие заметки")
                    print(notes)
                    break
                else:
                    print("Неверно введено значение, попробуйте снова.")
            except ValueError:
                print("Неверный формат, попробуйте снова.")




delete()


