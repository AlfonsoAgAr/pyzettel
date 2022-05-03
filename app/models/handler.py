from note import Note
import os

filepath = os.path.expanduser('~')

class PathHandler:
    def __init__(self) -> None:
        self.__new__

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
    def __init__(self, PathHandler):
        self.__new__
        PathHandler.__init__

    @classmethod
    def verify_filename(self, filename) -> bool:
        if os.path.exists(self.verify_path() + f'{filename}'):
            return True
        else:
            return False

    @classmethod
    def temp_file(self) -> str:
        # este metodo debe devolver un archivo temporal para visualizar
        # si el archivo es correcto, debe escribirse a un archivo real
        # con el metodo make_file
        ...

    @classmethod
    def make_file(self, **kwargs) -> str:
        # este metodo escribe el archivo markdown en la carpeta ~/.zettel/
        # despues lo indexa a .zetteldb.json
        ...

    @staticmethod
    def delete_file(filename) -> str:
        try:
            if FileHandler.verify_filename(f'{filename}'):
                os.remove(FileHandler.verify_path() + f'{filename}')
                return 'File removed suscesfully.'
            else:
                raise OSError(f'File Exception: {filename} not found.')
        except OSError as e:
            return e


# noteLocal = Note()

# test = FileHandler.verify_path()
# print(test)


# print(FileHandler.delete_file('1.txt'))
