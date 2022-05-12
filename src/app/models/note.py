from src.app.models.markdownSyntax import MarkdownSyntax as MD
import datetime

class Note:
    def __init__(self) -> None:
        self.file_name: str
        self.uid: str
        self.title: str
        self.tags: list[str]
        self.origin: str
        self.origin_title: str
        self.createdAt: str
        self.content: str
        self.references: str

        if self.__new__:
            self.uid = self.setUid()
            self.createdAt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self) -> str:
        return f'<{self.title} [[{self.uid}]]>'
    
    @property
    def filename(self) -> str:
        title = self.title.replace(' ', '_').replace('.','').lower()
        title += f'_{self.uid}.md'
        self.file_name = title
        return self.file_name

    def setUid(self) -> str:
        uid =  datetime.datetime.now()
        uid =  str(uid).replace('-', '').replace(':', '').replace(' ', '')

        return uid[:12]

    @staticmethod
    def getUid(self) -> str:
        """
        Simple method to get the uid of a created class.

        Note().getUid({note_created})
        """
        return self.uid

    @classmethod
    def set_attributes(self, **kwargs) -> None:
        """
        This method provides access to the elements of Note class.

        :: Note.file_name -> srt ::
        :: Note.title -> str ::
        :: Note.tags -> List[str] ::
        :: Note.origin -> int ::
        :: Note.origin_title -> str ::
        """
        _ATTRIBUTES = ['title', 'tags', 'origin', 'origin_title']

        for i in kwargs.keys():
            if i in _ATTRIBUTES:
                setattr(self, i, kwargs[i])

class MarkdownNote(Note, MD):
    """
    Class that represents a Note as Markdown File.
    Use this class to create a new Structured Note.
    
    Methods:\n
        :: h1('Title') -> '# Title' ::\n
        :: h2('Title') -> '## Title' ::
        :: h3('Title') -> '### Title' ::
        :: bold('Title') -> '**Title**' ::
        :: italic('Title') -> '*Title*' ::
        :: quote('Title') -> '>Title' ::
        :: code('Title') -> '```Some Code```' ::
        :: h_rule('Title') -> '---Some Content---' ::
        :: link('Title', 'google.com') -> '[Title](google.com)' ::
        :: footnotes('Title') -> '[^1]: [Title](google.com)' ::
        
        :: create_markdown -> return the note structured as str::
    """
    def __init__(self) -> None: super().__init__()
    def __repr__(self) -> str: return f'<{self.title} [[{self.uid}]]>'
    def h1(self, text_to: str) -> str: return f'# {text_to}\n\n'.format(text_to)
    def h2(self, text_to: str) -> str: return f'## {text_to}\n\n'.format(text_to)
    def h3(self, text_to: str) -> str: return f'### {text_to}\n\n'.format(text_to)
    def bold(self, text_to: str) -> str: return f'**{text_to}**' + ' '
    def italic(self, text_to: str) -> str: return f'*{text_to}*' + ' '
    def quote(self, text_to: str) -> str: return f'>{text_to}\n\n'
    def code(self, text_to: str) -> str: return f'```\n{text_to}\n\n```'
    def h_rule(self, text_to: str) -> str: return f'---\n{text_to}\n\n---\n'
    def link(self, text_to: str, link_to: str) -> str: return f'[{text_to}]({link_to})'
    def footnotes(self, text_to: str) -> str: return f'[^1]: [{text_to}](google.com)'

    def create_markdown(self) -> str:
        markdown_note = self.h1(self.title)\
        + self.h_rule(
        'Title: ' + self.title + '\n' +
        'UID: ' + self.link(self.uid, '') + '\n' +
        'Tags: ' + str([self.link('#'+ self.tags[i], self.tags[i].capitalize() + '.md') for i in range(len(self.tags))]).replace("'",'').replace(',','')[1:-1] + '\n' +
        'Origin UID:  ' + self.link('', '') + '\n' +
        'Origin Title: ' + self.link('', '') + '\n' +
        'Date: ' + self.italic(self.createdAt)
        )\
        + self.h3('Main Content') + self.bold('Description of the problem')\
        + '\n\n' + 'Some problem' + '\n\n' + self.bold('Solution') + '[^1]'\
        + '\n\n' + self.code('Some code') + '\n\n' + self.footnotes('Some refer')

        return markdown_note