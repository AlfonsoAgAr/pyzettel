import os, json, pickle, re
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
    ...
    """

    def __init__(self) -> None: ...

    def upload(self): ...

    def remove(self): ...

    def update(self): ...

    def get(self): ...

    def search(self): ...

# a.x = 'hola'
# a.y = 'mundo'

a = Constructor('moving_files_with_mv_command_202205081411.md')
print(a.raw_note)
