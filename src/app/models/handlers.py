import os, re, itertools

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
    def verify_filename(filename: str) -> bool:
        if os.path.exists(FileHandler.verify_path() + f'{filename}'):
            return True
        else:
            return False

    @staticmethod
    def make_file(filename: str, texto_markdown: str) -> str:
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
    def add_parent(filename: str) -> str:
        parents = []
        try:
            # Reading the tags inside the file.
            with open(FileHandler.verify_path() + f'{filename}', 'r+') as file:
                for i in file.read().splitlines():
                    if 'Tags:' in i:
                        raw = re.split('\[(.*?)\]', i)
                        parents = [i.replace('#', '') for i in raw if i.startswith('#')]
            # Adding the parent to the file
            for parent in parents:
                title_parent = parent.capitalize()+'.md'
                FileHandler.make_file(title_parent, '')
                with open(FileHandler.verify_path() + f'{title_parent}', 'r+') as file:
                    content = file.read()
                    if content.find(filename) != -1:
                        print(f'{title_parent} already has {filename}')
                    else:
                        file.write(f'{filename} ()\n')
                        print(f'{filename} was added successfully to {title_parent}')
        except OSError as e:
            return e

    @staticmethod
    def delete_parent() -> None:
        files = os.listdir(FileHandler.verify_path())
        parents_files = itertools.filterfalse(lambda x: x[:1].islower(), files)
        parents_files = [i for i in parents_files]
        k = 0

        for parent in parents_files:
            files_asociated = []
            with open(FileHandler.verify_path() + f'{parent}', 'r') as file:
                for i in file.read().splitlines():
                    if i.find('.md') != -1:
                        files_asociated.append(i[:i.find('.md')+3])

            for file in files_asociated:
                parents_in_file = []
                try:
                    with open(FileHandler.verify_path() + f'{file}', 'r+') as f:
                        for i in f.read().splitlines():
                            if 'Tags:' in i:
                                raw = re.split('\[(.*?)\]', i)
                                parents_in_file=[i.replace('#', '') for i in raw if i.startswith('#')]
                    # print(f'     Parents on file: [{file}] has the follow tags ----> {parents_in_file}') # DEBUG
                    if parent.replace('.md', '').lower() not in parents_in_file:
                        with open(FileHandler.verify_path() + f'{parent}', 'r+') as fr:
                            lines_to_write = fr.readlines()
                            line_to_delete = [i for i in lines_to_write if i.startswith(file)]
                            fr.seek(0)
                            fr.truncate()
                            for current_line in lines_to_write:
                                if current_line != line_to_delete[0]:
                                    fr.write(current_line)
                                else:
                                    k += 1
                                    print(f'          [{file}] was deleted from {parent}')
                except:
                    with open(FileHandler.verify_path() + f'{parent}', 'r+') as fr:
                            lines_to_write = fr.readlines()
                            line_to_delete = [i for i in lines_to_write if i.startswith(file)]
                            fr.seek(0)
                            fr.truncate()
                            for current_line in lines_to_write:
                                if current_line != line_to_delete[0]:
                                    fr.write(current_line)
                                else:
                                    k += 1
                                    print(f'          [{file}] was deleted from {parent}')

        print(f'\n\nPushed elements, {k} tags were removed in the process.')


    @staticmethod
    def push_changes() -> str:
        """
        This method should push the changes from the files to the parents files.
        """
        files = os.listdir(FileHandler.verify_path())
        notes_file = itertools.filterfalse(lambda x: x[:1].isupper(), files) # Check if a file is a parent or is a note. Parents are capilalized strings.
        [FileHandler.add_parent(filename) for filename in notes_file] # Convert the itertools.filterfalse object to a redable list.
        FileHandler.delete_parent() # Delete the parents that are not used anymore.
        return 'Push message:\n' + '\n'.join(notes_file)

    @staticmethod
    def delete_file(filename: str) -> str:
        try:
            if FileHandler.verify_filename(f'{filename}'):
                os.remove(FileHandler.verify_path() + f'{filename}')
                return 'File removed suscesfully.'
            else:
                raise FileNotFoundError(f'File Exception: {filename} not found.')
        except OSError as e:
            return e

# FileHandler.add_parent('moving_files_with_mv_command_202205081411.md')
# print(FileHandler.push_changes())
# FileHandler.push_changes()
