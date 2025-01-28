import yaml
from colorama import Fore, init

def load_notes_from_file():
    init(autoreset=True)
    with open('notes.txt') as file:
        try:
            while True:
                notes = yaml.load(file, Loader=yaml.FullLoader)
                if notes == None:
                    print("Фаил пуст.")
                    break
                else:
                    note_number = 1
                    for i in range(len(notes)):
                        print(
                            Fore.RED + "----------------------------------------------------")
                        # разделительная линния (красная)
                        print(Fore.YELLOW + f"Note №{note_number}")  # нумерация заметок (желтая)
                        note_number = note_number + 1
                        string_namber = 1
                        for k in notes[i].items():
                            name, val = k
                            print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
                            # нумерация строк (зеленая) и габариты таблицы
                            string_namber = string_namber + 1
                    break
        except FileNotFoundError:
            print(Fore.RED +"Фаил не найден.")
        except UnicodeDecodeError:
            print(Fore.RED +"Не удалось декодировать фаил.")
        except PermissionError:
            print(Fore.RED +"Ошибка доступа, системный фаил.")
    file.close()
load_notes_from_file()