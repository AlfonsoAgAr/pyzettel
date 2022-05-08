import sys, unittest
sys.path.append('../')
from src import FileHandler, MarkdownNote



test = FileHandler.verify_path()
print('*'*80, '\n\n', test,'\n')

# Example of usage
data = {
    'title': 'Recursive python script over html files for get data with bash.',
    'tags': ['bash', 'python', 'html']
    }

test = MarkdownNote()
test.set_attributes(**data)
print(test.create_markdown())

