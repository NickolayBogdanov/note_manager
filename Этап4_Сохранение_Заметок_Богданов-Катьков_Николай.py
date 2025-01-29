import yaml

notes = [
    {
        "username": "Павел",
        "title": "Дела на завтра",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '12-01-25',
        "issue_date": '15-01-25',
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
        "created_date": '10-01-25',
        "issue_date": '20-01-25',
    }
]


def save_notes_to_file(filename = input("Введите название файла: ")):
    with open(filename, mode='w', encoding='utf-8') as filename:
        notes_yaml = yaml.dump(notes, allow_unicode=True, sort_keys=False)
        filename.write(notes_yaml)
        filename.close()
        print("Фаил успешно записан.")


save_notes_to_file()
# while info: == while len(info) > 0:
# mode= 'w' == запись
