import os, json, re
from itertools import chain
from typing import Optional

filepath = os.path.expanduser('~/.zettel/')

class NoteStore:
    __slots__ = 'file_name', 'uid', 'title', 'tags', 'origin', 'origin_title', 'createdAt', 'content', 'references', 'filepath'

    def __init__(
        self,
        file_name: str,
        uid: int,
        title: str,
        tags: list,
        origin: Optional[int],
        origin_title: Optional[str],
        createdAt: str,
        content: str,
        references: Optional[str],
        filepath: str) -> None:
        self.file_name: str = file_name
        self.uid: int = uid
        self.title: str = title
        self.tags: list = tags
        self.origin: int = origin
        self.origin_title: str = origin_title
        self.createdAt: str = createdAt
        self.content: str = content
        self.references: str = references
        self.filepath: str = filepath

class Constructor(NoteStore):

    def __init__(self, filename: str) -> None:
        self.raw_note: dict = self.parse_note(filename)
        super().__init__(self.raw_note['file_name'],
                         self.raw_note['uid'],
                         self.raw_note['title'],
                         self.raw_note['tags'],
                         self.raw_note['origin'],
                         self.raw_note['origin_title'],
                         self.raw_note['createdAt'],
                         self.raw_note['content'],
                         self.raw_note['references'],
                         self.raw_note['filepath'])

    def __repr__(self) -> str:
        return f'Constructor from <{self.file_name}>'

    @classmethod
    def parse_note(self, filename: str) -> object:
        note = {
            'file_name': str,
            'uid': int,
            'title': str,
            'tags': list,
            'origin': int,
            'origin_title': str,
            'createdAt': str,
            'content': list,
            'references': str,
            'filepath': str
            }

        with open(filepath+filename, 'r') as f:
            document = f.readlines()
            note['content'] = document
            for line in document:
                if line[:6] == 'Title:': note['title'] = line[7:-1];
                if line[:3] == 'UID': _uid = re.split('\[(.*?)\]', line); note['uid'] = [int(element) for element in _uid if element.isdigit()][0];
                if 'Tags' in line: raw = re.split('\[(.*?)\]', line); note['tags'] = [line.replace('#', '') for line in raw if line.startswith('#')];
                if 'Origin UID' in line: _uid = re.split('\[(.*?)\]', line); note['origin'] = [int(element) for element in _uid if element.isdigit()][0];
                if 'Origin Title' in line: raw = re.split('\[(.*?)\]', line); note['origin_title'] = raw[1];
                if 'Date' in line: note['createdAt'] = line[6:-1].replace('*', '')
        note['file_name'] = filename
        note['filepath'] = filepath + filename

        return note

class DataBase:
    # Essentially a dictionary built from a json file.
    """
    JSON file for record all notes.
    """

    def __init__(self) -> None:

        self.db: dict = {}

        if '.zetteldb.json' in os.listdir(filepath):
            with open(filepath + '.zetteldb.json', 'r') as f:
                self.db = json.load(f)
        else:
            self.create()
            with open(filepath + '.zetteldb.json', 'r') as f:
                self.db = json.load(f)

    def create(self) -> None:
        notes = [Constructor(file) for file in os.listdir(filepath) if file[0].islower()]
        acumulative_tags = [note.tags for note in notes]
        list_tags = list(set(chain(*acumulative_tags)))
        list_tags = [tag.capitalize() for tag in list_tags]
        tag_dict = dict.fromkeys(list_tags, {})

        with open(filepath + '.zetteldb.json', 'w+') as f:
            json.dump(tag_dict, f, indent=4, separators=(',', ' : '))

    def update(self) -> None:
        """
        Add all elements to a Json file in the .zettel directory.
        If an element was removed, this function doesn't delet the key from the json.
        Saves everything.
        """
        notes = [Constructor(file) for file in os.listdir(filepath) if file[0].islower()]
        for parent in self.db:
            for note in notes:
                if parent.lower() in note.tags:
                    uid = {note.uid:
                            {
                                'file_name':note.file_name,
                                'uid': note.uid,
                                'title': note.title,
                                'tags': note.tags,
                                'origin': parent,
                                'origin_title': parent,
                                'createdAt': note.createdAt,
                                'content': note.content,
                                'references': None,
                                'filepath': filepath + note.file_name
                            }}
                    self.db[parent].update(uid)
        with open(filepath + '.zetteldb.json', 'r+') as f:
            json.dump(self.db, f, indent=4, separators=(',', ' : '))

    def search(self) -> dict: ...

#a = Constructor('moving_files_with_mv_command_202205081411.md')
#print(a.raw_note)
#print(os.listdir(filepath))
#test = DataBase()
#print(test)
#print(test.update())
# DataBase().update() ----> Converts all data from .zettel to jsonn format
