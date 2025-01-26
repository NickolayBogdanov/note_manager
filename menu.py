from colorama import Fore, init






init(autoreset=True)
menu = {1: "Создать новую заметку", 2: "Показать все заметки", 3: "Обновить заметку",
        4: "Удалить заметку", 5: "Найти заметки", 6: "Выйти из программы"}

print("Добро пожаловать в 'Менеджер заметок'")
while True:
    try:
        print(Fore.YELLOW + "         Меню")
        for i in menu.items():
            name, val = i
            print(Fore.CYAN + "{:<1} {:<30}".format(name, val))
        action = int(input("Выберите действие из списка 1-6: "))
        if action == 1:
            from note_manager.create_note_function import create_note
            create_note()
            continue
        elif action == 2:
            from note_manager.display_notes_function import display_notes
            display_notes()
            continue
        elif action == 3:
            from note_manager.update_note_function import update_status, date, yes_no, update_note
            update_note()
            continue
        elif action == 4:
            from note_manager.delete_note import delete_one, delete_all, delete_note
            delete_note()
            continue
        elif action == 5:
            from note_manager.search_notes_function import search_notes
            print("To skip one of the search criteria, leave the field blank and press Enter.")
            print("Чтобы пропустить один из критериев поиска, оставьте поле пустым и нажмите Enter")
            search_notes(input("Please, entered keyword (username, title or content): "), input("Please, entered status: "))
            continue
        elif action == 6:
            break
        else:
            print("Неверный выбор, пожалуйста выберете действие из списка")
    except ValueError:
        print("Неверно введено значение, попробуйте снова.")
