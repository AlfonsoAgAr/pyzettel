from app import *

test = Note()
setattr(test, 'title', 'Bash find regex')
print('Función getUid:\n',Note().getUid(test))
test.setAttributes(tags=['#hola', '#mundo'], origin=737219132)
print('Representación de la clase:\n',test)
print('Created at:\n',test.createdAt)
print('Origin:\n',test.tags)
print('Origin:\n',test.origin)
print('Filename:\n',test.setFilename())