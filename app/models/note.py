from markdownSyntax import MarkdownSyntax as MD
import datetime

class Note:
    def __init__(self) -> None:
        self.file_name: str
        self.uid: str
        self.title: str
        self.tags: list[str]
        self.origin: str
        self.origin_title: str
        self.child: str
        self.createdAt: str
        self.content: str
        self.references: str

        if self.__new__:
            self.uid = self.setUid()
            self.createdAt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self) -> str:
        return f'<{self.title} [[{self.uid}]]>'

    def setUid(self) -> str:
        uid =  datetime.datetime.now()
        uid =  str(uid).replace('-', '').replace(':', '').replace(' ', '')

        return uid[:12]

    def setFilename(self) -> str:
        title = self.title.replace(' ', '_').lower()
        title += f'_[{self.uid}].md'

        return title

    @staticmethod
    def getUid(self) -> str:
        """
        Simple method to get the uid of a created class.

        Note().getUid({note_created})
        """
        return self.uid

    @classmethod
    def setAttributes(self, **kwargs) -> None:
        """
        This method provides access to the elements of Note class.

        :: Note.file_name -> srt ::
        :: Note.title -> str ::
        :: Note.tags -> List[str] ::
        :: Note.origin -> int ::
        :: Note.origin_title -> str ::
        """
        _ATTRIBUTES = ['file_name', 'title', 'tags', 'origin', 'origin_title']

        for i in kwargs.keys():
            if i in _ATTRIBUTES:
                setattr(self, i, kwargs[i])

class MarkdwonNote(Note, MD):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'Markdown Note'

    def h1(self, text_to: str) -> str: return f'# {text_to}\n'.format(text_to)
    def h2(self, text_to: str) -> str: return f'## {text_to}\n'.format(text_to)
    def h3(self, text_to: str) -> str: return f'### {text_to}\n'.format(text_to)
    def bold(self, text_to: str) -> str: return f'**{text_to}**' + ' '
    def italic(self, text_to: str) -> str: return f'*{text_to}*' + ' '
    def quote(self, text_to: str) -> str: return f'>{text_to}\n'
    def code(self, text_to: str) -> str: return f'```\n{text_to}\n```'
    def h_rule(self, text_to: str) -> str: return f'---\n{text_to}\n---'
    def link(self, text_to: str, link_to: str) -> str: return f'[{text_to}]({link_to})'

    def __repr__(self) -> str:
        return self.bold(f'<{self.title} [[{self.uid}]]>') + 'and more'

test = MarkdwonNote()

print(test.uid)
print(test)

