from colorama import Fore, init
from operator import itemgetter



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
    while True:
        sort_base = {"1": "username", "2": "created_date", "3": "issue_date" }
        print(f"Сортировать по: {sort_base}")
        sort_option = sort_base.get(input("Введите параметр сортировки \"1\", \"2\" или \"3\": "))
        if sort_option == "username" or sort_option == "created_date" or sort_option == "issue_date":
            sort_list = sorted(notes, key=itemgetter(sort_option))
            break
        # сортирует список словарей по выбранному ключу
        else:
            print("Неверно введено значение, попробуйте снова.")

    if sort_list == []:
        print(Fore.RED + "You don't have any saved notes.")
    else:
        page_namber = 1
        items_per_page = 5
        index = items_per_page * page_namber
        list_1 = []
        for page in sort_list[index - 5:index]: # вывод по 5 позиций на страницу
            list_1.append(page) # список сортированных заметок на странице
        for i in range(len(list_1)):
            print(Fore.RED + "----------------------------------------------------") # разделительная линния (красная)
            print(Fore.YELLOW + f"Note №{note_number}") # нумерация заметок (желтая)
            note_number = note_number + 1
            string_namber = 1
            for k in list_1[i].items():
                name, val = k
                print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
                # нумерация строк (зеленая) и габариты таблицы
                string_namber = string_namber + 1


display_notes()