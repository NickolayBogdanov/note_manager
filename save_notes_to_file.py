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
        "username": "Nickolay",
        "title": "Study",
        "content": "Get books from the library",
        "status": "In process",
        "created_date": '10-01-25',
        "issue_date": '20-01-25',
    }
]


def save_notes_to_file(file = open('notes.txt', mode='w', encoding='utf-8')):
    notes_yaml = yaml.dump(notes)

    file.write(notes_yaml)
    file.close()


save_notes_to_file()
# while info: == while len(info) > 0:
# mode= 'w' == запись
