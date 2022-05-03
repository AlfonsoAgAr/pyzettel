from note import Note

class Handler:
    def __init__(self, Note: Note()) -> None:
        self.note = Note
    
    def testFunction(self) -> None:
        return self.note

testNote = Note()
testNote.setAttributes(title='Bash find regex', tags=['#hola', '#mundo'], origin=737219132)


test = Handler(testNote)
print(test.testFunction())