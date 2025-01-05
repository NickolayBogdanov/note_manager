from note_manager.add_input import username, title, content, status
from note_manager.add_list import titles
from note_manager.data_changer import temp_created_date, temp_issue_date

note = [
    username,
    {title: (
        content,
        status,
        temp_created_date,
        temp_issue_date
        )
    },
    titles
]

print(note)
