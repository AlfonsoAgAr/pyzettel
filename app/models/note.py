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

    def set_filename(self) -> str:
        title = self.title.replace(' ', '_').replace('.','').lower()
        title += f'_{self.uid}.md'

        return title

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

class MarkdwonNote(Note, MD):
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
        'Tags: ' + str([self.link('#'+ self.tags[i], '') for i in range(len(self.tags))]).replace("'",'').replace(',','')[1:-1] + '\n' +
        'Origin UID:  ' + self.link('', '') + '\n' +
        'Origin Title: ' + self.link('', '') + '\n' +
        'Date: ' + self.italic(self.createdAt)
        )\
        + self.h3('Main Content') + self.bold('Description of the problem')\
        + '\n\n' + 'Some problem' + '\n\n' + self.bold('Solution') + '[^1]'\
        + '\n\n' + self.code('Some code') + '\n\n' + self.footnotes('Some refer')
        
        return markdown_note

# Example of usage
data = {
    'title': 'Recursive python script over html files for get data with bash.', 
    'tags': ['bash', 'python', 'html']
    }

test = MarkdwonNote() 
test.set_attributes(**data)
print(test.create_markdown())

#   TODO:

# Escribir el test.create_markdown() en un archivo markdown. Los tags deberian verificar si existe un markdown padre.
# Para este ejemplo, deberían existir los archivos Python.md, Bash.md y Html.md.

# En cada archivo de ellos debería escribir lo siguiente:
    
#     Recursive python script over html files for get data with bash. [202205060425](routa_para_recursive_..._202205060425)
    
# De esta manera, automaticamente deberían irse llenando los archivos principales.
# Si existe el archivo padre (Python.md), escibre sobre él. Si no existe, lo crea y escribe.
# Escribir una función para actualizar los archivos padres, es decir, si agrego más tags, debería llamar una función push que actualice los archivos padres.
# También se debe actualizar la base de datos.
# También se deben enviar a un repositorio git.
