import os

filepath = os.path.expanduser('~')

class PathHandler:
    def __init__(self) -> None: ...

    @classmethod
    def create_path(self) -> str:
       os.mkdir(f'{filepath}/.zettel')
       return f'{filepath}/.zettel/'

    @classmethod
    def verify_path(self) -> str:
        dir_files = os.listdir(filepath)

        if '.zettel' in dir_files:
            return f'{filepath}/.zettel/'
        else:
            return self.create_path()

class FileHandler(PathHandler):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def verify_filename(filename) -> bool:
        if os.path.exists(FileHandler.verify_path() + f'{filename}'):
            return True
        else:
            return False

    @staticmethod
    def make_file(filename, texto_markdown) -> str:
        try:
            if FileHandler.verify_filename(f'{filename}'):
                return 'This file already exists.'
            else:
                with open(FileHandler.verify_path() + f'{filename}', 'w') as file:
                    file.write(texto_markdown)
                return f'Markdown {filename} created.'
        except OSError as e:
            return e

    @staticmethod
    def edit_file(filename, texto_markdown) -> str: ...

    @staticmethod
    def delete_file(filename) -> str:
        try:
            if FileHandler.verify_filename(f'{filename}'):
                os.remove(FileHandler.verify_path() + f'{filename}')
                return 'File removed suscesfully.'
            else:
                raise FileNotFoundError(f'File Exception: {filename} not found.')
        except OSError as e:
            return e