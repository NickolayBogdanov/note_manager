from note_manager.add_input import username, content, status, title
from note_manager.add_list import titles
from note_manager.data_changer import created_date, issue_date

note = {
    username: titles,
    title: (content, status, created_date, issue_date)
     } # словарь по имени предоставляющий список заголовков а по заголовку предоставляющий саму заметку и данные о заметке
print(note)
