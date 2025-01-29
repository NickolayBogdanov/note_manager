import yaml
from colorama import Fore, init

def load_notes_from_file(file_name = input("Введите название файла: ")):
    init(autoreset=True)
    try:
        with open(file_name, encoding='utf-8') as file:
        # открытие файла в режиме чтения с кодировкой поддерживающей кириллицу
            while True:
                notes = yaml.load(file, Loader=yaml.FullLoader) # загрузка данных из файла
                if notes == None:
                    print("Фаил пуст.")
                    break
                else:
                    note_number = 1
                    for i in range(len(notes)):
                        print(Fore.RED + "----------------------------------------------------")
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
            file.close()
    except AttributeError:
        print("Ошибка при чтении файла. Проверьте его содержимое.")
    except FileNotFoundError:
        print(Fore.RED +"Фаил не найден.")
        file = open(file_name, "w", encoding='utf-8') # создание файла в случае его отсутствия
        file.close()
        print(f"Новый файл {file}, успешно создан.")
    except UnicodeDecodeError:
        print(Fore.RED +"Не удалось декодировать фаил.")
    except PermissionError:
        print(Fore.RED +"Ошибка доступа, системный фаил.")


load_notes_from_file()