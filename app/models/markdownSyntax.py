from abc import ABC, abstractmethod

class MarkdownSyntax(ABC):
    """
    This class represents the Markdown syntax.
    Methods are used to convert the raw text into readable markdown.
    All methods receives a raw text and returns a formatted text.
    Implementations are provided in the subclasses.

    Example:
    InheritedClass(MarkdownSyntax):
        def h1(self, raw_text: str) -> str:
            return f'# {raw_text}\n'
    
    InstanceOfInheritedClass.h1('Hello world') -> # Hello world

    References: ...
    """
    def __init__(self) -> None: ...

    def h1(self, raw_text: str) -> str: ...
    def h2(self, raw_text: str) -> str: ...
    def h3(self, raw_text: str) -> str: ...
    def h4(self, raw_text: str) -> str: ...
    def h5(self, raw_text: str) -> str: ...
    def h6(self, raw_text: str) -> str: ...
    def bold(self, raw_text: str) -> str: ...
    def italic(self, raw_text: str) -> str: ...
    def underline(self, raw_text: str) -> str: ...
    def strike(self, raw_text: str) -> str: ...
    def link(self, raw_text: str) -> str: ...
    def list(self, raw_text: str) -> str: ...
    def quote(self, raw_text: str) -> str: ...
    def code(self, raw_text: str) -> str: ...
    def table(self, raw_text: str) -> str: ...
    def h_rule(self, raw_text: str) -> str: ...
    def footnotes(self, raw_text: str) -> str: ...

    # Algunos editores y lectores de markdown pueden tener conflictos al interactuar
    # con ciertos caracteres. Esta función puede ayudar.
    def parse_markdown(self, raw_text: str) -> str: ...
        # reserved_characters = ['.', r'\'', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '!']
        # for k in reserved_characters:
        #     raw_text = raw_text.replace(k, f"\{k}")
        # return raw_text