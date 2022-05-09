import sys, unittest
sys.path.append('../')
from src import FileHandler

class FilesTest(unittest.TestCase):
        
    def test_make_file(self) -> bool:
        # Creates a markdown.
        case = FileHandler.make_file('202205080210.md', '')
        self.assertEqual(case, 'Markdown 202205080210.md created.')
    
    def test_verify_file(self) -> bool:
        # Verifies that the file created above exists.
        self.assertEqual(FileHandler.verify_filename('202205080210.md'), True)
    
    def test_content_file(self) -> bool:
        # Creates a markdown with content.
        FileHandler.make_file('file_to_read.md', 'Text to write...')
        # Open the markdown and read the content.
        with open(FileHandler.verify_path() + 'file_to_read.md', 'r') as file:
            self.assertEqual(file.read(), 'Text to write...')
           
    def test_modify_file(self) -> bool: ...
            
    def test_delete_file(self) -> bool:
        # Delete the markdown created above.
        FileHandler.delete_file('202205080210.md')
        # Verifies that the file created above was deleted. 
        self.assertEqual(FileHandler.verify_filename('202205080210.md'), False)

if __name__ == '__main__':
    unittest.main()