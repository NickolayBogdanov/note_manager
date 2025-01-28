import yaml

notes = [
    {
        "username": "Pavel",
        "title": "Business for tomorrow",
        "content": "Wash the dishes, do your homework, go to the pool by 18:30",
        "status": "In process",
        "created_date": '12-01-25',
        "issue_date": '15-01-25',
    },
    {
        "username": "Pavel",
        "title": "Business for the day after tomorrow",
        "content": "Take out the trash, walk the dog",
        "status": "In process",
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


def save_notes_to_file(file = open(input("Введите название файла: "), mode='w', encoding='utf-8')):
    notes_yaml = yaml.dump(notes)

    file.write(notes_yaml)
    file.close()
    print("Фаил успешно записан.")


save_notes_to_file()
# while info: == while len(info) > 0:
# mode= 'w' == запись
