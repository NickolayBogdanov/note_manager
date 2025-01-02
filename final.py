from note_manager.add_input import username, title, status, subtitle1, subtitle2, subtitle3, subcontent1, subcontent2, subcontent3
from note_manager.add_list import titles
from note_manager.data_changer import temp_created_date, temp_issue_date
# импорт данных из других фаилов программы

content = {subtitle1: subcontent1, subtitle2: subcontent2, subtitle3: subcontent3}
note = {
    username: titles,
    title: (content, status, temp_created_date, temp_issue_date)
} # сбор всех данных в библиотеку
print(note)
