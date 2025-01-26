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
print("To skip one of the search criteria, leave the field blank and press Enter.")
print("Чтобы пропустить один из критериев поиска, оставьте поле пустым и нажмите Enter")
def search_notes(keyword=None, status=None):
    init(autoreset=True)
    note_number = 1
    notes_search = []
    while True:
        if keyword != "" and status != "":
            for i in range(len(notes)):
                if (keyword.upper() in notes[i]["title"].upper() and status.upper() == notes[i]["status"].upper()
                        or keyword.upper() in notes[i]["username"].upper() and status.upper() == notes[i]["status"].upper()
                        or keyword.upper() in notes[i]["content"].upper() and status.upper() == notes[i]["status"].upper()):
                    notes_search.append(notes[i])  # поиск по ключевому слову и статусу
            else:
                print("No notes were found for this query.")
            for k in range(len(notes_search)): # вывод данных в цветную таблицу с нумерацией заметок и строк
                print(Fore.RED + "----------------------------------------------------")
                print(Fore.YELLOW + f"Note №{note_number}")
                note_number = note_number + 1
                string_namber = 1
                for j in notes_search[k].items():
                    name, val = j
                    print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
                    string_namber = string_namber + 1
            break
        elif keyword != None and status == "":
            for i in range(len(notes)):
                if (keyword.upper() in notes[i]["title"].upper() or keyword.upper() in notes[i]["username"].upper()
                        or keyword.upper() in notes[i]["content"].upper()):
                    notes_search.append(notes[i]) # поиск по ключевому слову
            else:
                print("No notes were found for this query.")
            for k in range(len(notes_search)): # вывод данных в цветную таблицу с нумерацией заметок и строк
                print(Fore.RED + "----------------------------------------------------")
                print(Fore.YELLOW + f"Note №{note_number}")
                note_number = note_number + 1
                string_namber = 1
                for j in notes_search[k].items():
                    name, val = j
                    print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
                    string_namber = string_namber + 1
            break
        elif keyword == "" and status != None: # поиск по статусу
            for i in range(len(notes)):
                if status.upper() == notes[i]["status"].upper():
                    notes_search.append(notes[i])
            else:
                print("No notes were found for this query.")
            for k in range(len(notes_search)):
                print(Fore.RED + "----------------------------------------------------")
                print(Fore.YELLOW + f"Note №{note_number}")
                note_number = note_number + 1
                string_namber = 1
                for j in notes_search[k].items():
                    name, val = j
                    print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
                    string_namber = string_namber + 1
            break

search_notes(input("Please, entered keyword (username, title or content): "), input("Please, entered status: "))