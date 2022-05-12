from src import MarkdownNote

data = {
    'title': 'Counting numbers on files directory',
    'tags': ['bash', 'python', 'html']
    }

test = MarkdownNote()
test.set_attributes(**data)


print(test)
print(test.create_markdown())
print('\n\n'+test.createdAt)
print(test.filename)
# print(test.tags)
print(test.__dict__)
# DONE
# Escribir el test.create_markdown() en un archivo markdown. Los tags deberian verificar si existe un markdown padre.
# Para este ejemplo, deberían existir los archivos Python.md, Bash.md y Html.md.
# En cada archivo de ellos debería escribir lo siguiente:
#     Recursive python script over html files for get data with bash. [202205060425](routa_para_recursive_..._202205060425)
# De esta manera, automaticamente deberían irse llenando los archivos principales.
# Si existe el archivo padre (Python.md), escibre sobre él. Si no existe, lo crea y escribe.
# Escribir una función para actualizar los archivos padres, es decir, si agrego más tags, debería llamar una función push que actualice los archivos padres.

# TODO
# También se debe actualizar la base de datos.
# También se deben enviar a un repositorio git.
