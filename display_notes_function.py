from operator import itemgetter
from colorama import Fore, init



notes = [
    {
        "username": "Павел",
        "title": "Дела на завтра",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '11-01-25',
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
        "created_date": '11-01-25',
        "issue_date": '20-01-25',
    }
]




def display_all_notes(note_number = 1):
    sorted_list = sorted(notes, key=itemgetter("issue_date"))
    init(autoreset=True)
    for i in range(len(sorted_list)):
        print(Fore.RED + "---------------------------------")
        print(Fore.YELLOW + f"Note №{note_number}")
        note_number = note_number + 1
        string_namber = 1
        for k in sorted_list[i].items():
            print(Fore.GREEN + f"{string_namber})", *k)
            string_namber = string_namber + 1
    if sorted_list == []:
        print(Fore.RED + "You don't have any saved notes.")

display_all_notes()


def display_signs_notes(note_number = 1):
    init(autoreset=True)
    notes_based_on = []
    based  = input(("Enter the search object (recommended name or status): "))
    for i in range(len(notes)):
        for k in notes[i].values():
            if str.upper(k) == str.upper(based):
                notes_based_on.append(notes[i])

    sorted_list = sorted(notes_based_on, key=itemgetter("issue_date"))
    for i in range(len(sorted_list)):
        print(Fore.RED + "---------------------------------")
        print(Fore.YELLOW + f"Note №{note_number}")
        note_number = note_number + 1
        string_namber = 1

        for k in sorted_list[i].items():
            print(Fore.GREEN + f"{string_namber})", *k)
            string_namber = string_namber + 1
    if sorted_list == []:
        print(Fore.RED + "You don't have any saved notes.")

display_signs_notes()