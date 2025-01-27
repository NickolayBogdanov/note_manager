import yaml

def load_notes_from_file():
    with open('notes.txt') as fh:
        notes = yaml.load(fh, Loader=yaml.FullLoader)
        print(notes)
load_notes_from_file()