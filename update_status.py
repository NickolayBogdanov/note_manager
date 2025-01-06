status_base = {1: "Выполнено", 2: "В процессе", 3: "Отложено"}
status = status_base.get(2)

print("текущий статус заметки: ", status)
print("выберите статус заметки: 1 - выполнено, 2 - в процессе, 3 - отложено")

while True:
    status = status_base.get(int(input("Выберите статус заметки \"1\", \"2\" или \"3\": ")))
    if  status != status_base.get(1) and status != status_base.get(2) and status != status_base.get(3):
        status_base = {1: "Выполнено", 2: "В процессе", 3: "Отложено"}
        print("неверно введено значение")
    else:
        print("Стаус успешно изменен, текущий статус: ", (status))
        break


