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




def display_all_notes(note_number = 1):
    init(autoreset=True)
    sorted_list_1 = sorted(notes, key=itemgetter("created_date"))
    sorted_list_2 = sorted(notes, key=itemgetter("issue_date"))
    sorted_option = {"1": "created_date", "2": "issue_date"}
    print(sorted_option)
    option = input("Enter a note sorting option \"1\" or \"2\": ")
    if option == "1":
        for i in range(len(sorted_list_1)):
            print(Fore.RED + "----------------------------------------------------")
            print(Fore.YELLOW + f"Note №{note_number}")
            note_number = note_number + 1
            string_namber = 1
            for k in (sorted_list_1[i].items()):
                name, val = k
                print(Fore.GREEN + f"{string_namber})", "{:<20} {:<15}".format(name, val))
                string_namber = string_namber + 1
        if sorted_list_1 == []:
            print(Fore.RED + "You don't have any saved notes.")
    elif option == "2":
        for i in range(len(sorted_list_2)):
            print(Fore.RED + "----------------------------------------------------")
            print(Fore.YELLOW + f"Note №{note_number}")
            note_number = note_number + 1
            string_namber = 1
            for k in sorted_list_2[i].items():
                name, val = k
                print(Fore.GREEN + f"{string_namber})", "{:<20} {:<15}".format(name, val))
                string_namber = string_namber + 1
        if sorted_list_2 == []:
            print(Fore.RED + "You don't have any saved notes.")

display_all_notes()


