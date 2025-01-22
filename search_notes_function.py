from operator import itemgetter
from colorama import Fore, init



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
def search_notes(keyword=None, status=None):
    init(autoreset=True)
    note_number = 1
    search_notes = []
    for i in range(len(notes)):
        for k in notes[i].values():
            if k.upper() == keyword.upper() and notes[i]["status"].upper() == status.upper():
                search_notes.append(notes[i])

    for i in range(len(search_notes)):
        print(Fore.RED + "----------------------------------------------------")
        print(Fore.YELLOW + f"Note №{note_number}")
        note_number = note_number + 1
        string_namber = 1
        for k in search_notes[i].items():
            name, val = k
            print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
            string_namber = string_namber + 1

search_notes(input("Please, entered keyword: "), input("please, entered status: "))