with open('ejemplo.txt', 'r+') as fichero:
    print(fichero.read())
    fichero.write('escrito desde un programa en .py\n')

import os

f = "ejem.txt"

if os.path.exists(f):
    with open(f, 'r') as archivo:
        content = archivo.read()
        if content == "":
            print("no hay nada")
            with open(f, 'w') as archivo:
                archivo.write("nuevo")
        else:
            print(content)
else:
    open(f, 'x')
