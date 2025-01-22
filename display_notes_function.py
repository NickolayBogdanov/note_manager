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
        "title": "Дела на завтра1",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '13-01-25',
        "issue_date": '16-01-25',
    },
    {
        "username": "Павел",
        "title": "Дела на завтра2",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '14-01-25',
        "issue_date": '17-01-25',
    },
    {
        "username": "Павел",
        "title": "Дела на завтра3",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '15-01-25',
        "issue_date": '18-01-25',
    },
    {
        "username": "Павел",
        "title": "Дела на завтра4",
        "content": "Помыть посуду, сделать уроки, в бассейн к 18:30",
        "status": "В процессе",
        "created_date": '12-01-25',
        "issue_date": '15-01-25',
    },
    {
        "username": "Павел",
        "title": "Дела на завтра5",
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




def display_notes(note_number = 1):
    init(autoreset=True)
    sorted_list_1 = sorted(notes, key=itemgetter("created_date"))
    sorted_list_2 = sorted(notes, key=itemgetter("issue_date"))
    sorted_option = {"1": "created_date", "2": "issue_date"}

    while True:
        print(sorted_option)
        option = input("Enter a note sorting option \"1\" or \"2\": ")
        if option == "1":
            page_namber = 1
            items_per_page = 5
            index = items_per_page * page_namber
            list_1 = []
            for page in sorted_list_1[index - 5:index]:
                list_1.append(page)

            for i in range(len(list_1)):
                print(Fore.RED + "----------------------------------------------------")
                print(Fore.YELLOW + f"Note №{note_number}")
                note_number = note_number + 1
                string_namber = 1
                for k in list_1[i].items():
                    name, val = k
                    print(Fore.GREEN + f"{string_namber})", "{:<20} {:<15}".format(name, val))
                    string_namber = string_namber + 1
            break
        elif notes == []:
            print(Fore.RED + "You don't have any saved notes.")
        elif option == "2":

            page_namber = 1
            items_per_page = 5
            index = items_per_page * page_namber
            list_1 = []
            for page in sorted_list_2[index - 5:index]:
                list_1.append(page)

            for i in range(len(list_1)):
                print(Fore.RED + "----------------------------------------------------")
                print(Fore.YELLOW + f"Note №{note_number}")
                note_number = note_number + 1
                string_namber = 1
                for k in list_1[i].items():
                    name, val = k
                    print(Fore.GREEN + f"{string_namber})", "{:<20} {:<15}".format(name, val))
                    string_namber = string_namber + 1
            break
        elif notes == []:
            print(Fore.RED + "You don't have any saved notes.")
        else:
            print("Incorrect value entered, please try again.")

display_notes()
