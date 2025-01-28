import yaml
from colorama import Fore, init




def append_notes_to_file(file = open(input("Введите название файла: "), mode='a', encoding='utf-8')):
    notes = []
    init(autoreset=True)
    while True:
        print('Добро пожаловать в "Менеджер заметок"')
        yes_no = input('Желаете добавить заметку? \"да\" \"нет\" : ')
        try:
            if yes_no == "нет":
                print("До новых встреч.")
                break
            elif yes_no == "да":
                notes.append(dict())  # создание нового словаря
                notes[-1].get("username")  # добавление ключа
                while True:
                    notes[-1]["username"] = input("Введите ваше имя: ")  # присвоение значения
                    if notes[-1]["username"] == "" or notes[-1]["username"] == " ":
                        print("Нельзя оставить пустое поле. Попрпобуйте снова.")
                    else:
                        break
                notes[-1].get("title")  # добавление ключа
                while True:
                    notes[-1]["title"] = input("Введите заголовок: ")  # присвоение значения
                    if notes[-1]["title"] == "" or notes[-1]["title"] == " ":
                        print("Нельзя оставить пустое поле. Попрпобуйте снова.")
                    else:
                        break
                notes[-1].get("content")  # добавление ключа
                while True:
                    notes[-1]["content"] = input('Введите заметку: ')  # присвоение значения
                    if notes[-1]["content"] == "" or notes[-1]["content"] == " ":
                        print("Нельзя оставить пустое поле. Попрпобуйте снова.")
                    else:
                        break
                notes[-1].get("status")
                while True:
                    status_base = {1: "Выполнено", 2: "В процессе", 3: "Отложено"}  # предусмотренные статусы
                    try:
                        status = status_base.get(int(input(
                            "Выберите статус заметки \"1\" - Выполнено, \"2\" - В процессе или \"3\" - Отложено: ")))
                        # запрос данных от пользователя
                        if status != status_base.get(1) and status != status_base.get(2) and status != status_base.get(
                                3):
                            print("неверно введено значение")  # проверка правельности ввода значений
                        else:
                            notes[-1]["status"] = status
                            print("Стаус успешно изменен, текущий статус: ", (status))
                            break  # завершение цикла при правельном вводе
                    except ValueError:  # страховка от ошибки, при введении некорректных данных
                        print("Неверный формат, попробуйте снова")
                import datetime
                created_date = datetime.datetime.today()  # текущая дата
                while True:
                    try:
                        issue_date = input("Введите дату истечения заметки в формате \'дд-мм-гггг\': ")
                        # получаем от пользователя дату
                        issue_date = (datetime.datetime.strptime(issue_date, '%d-%m-%Y'))
                        # конвертируем дату в объект
                        break  # завершение цикла при правельном вводе
                    except (ValueError):  # страховка от ошибки, при введении некорректных данных
                        print("Неверный формат, попробуйте снова.")
                notes[-1]["created_date"] = str(created_date.strftime("%d-%m-%Y"))
                notes[-1]["issue_date"] = str(issue_date.strftime("%d-%m-%Y"))
                print("Заметка создана успешно!")
                print("Текущие заметки:")
                note_number = 1
                for i in range(len(notes)):

                    print(Fore.RED + "----------------------------------------------------")
                    # разделительная линния (красная)
                    print(Fore.YELLOW + f"Note №{note_number}")  # нумерация заметок (желтая)
                    note_number += 1
                    string_namber = 1
                    for k in notes[i].items():
                        name, val = k
                        print(Fore.GREEN + f"{string_namber})", "{:<15} {:<30}".format(name, val))
                        # нумерация строк (зеленая) и габариты таблицы
                        string_namber = string_namber + 1
                break
            else:
                print("Неверно введено значение, попробуйте снова.")
        except ValueError:
            print("Неверный формат, попробуйте снова.")
    notes_yaml = yaml.dump(notes, allow_unicode=True, sort_keys=False)
    file.write(notes_yaml)
    file.close()
    print("Фаил успешно записан.")


append_notes_to_file()