print('Hola')
nom = "jose"
ape = "Barrientos"
num = 3
print(type(nom))
print(isinstance(num, int))  # Devuelve true o false

print(nom, ape, sep=', ')
# nom = input('nombre:')  # cambia el valor de la variable
print(nom, ape, sep=', ')
"""
Esto es un comentario
de varias lineas
"""
# Un input siempre se guarda como un string
# edad = input()
edad = 12.7
print(type(edad))
edad = int(edad)  # cambia el tipo de dato
print(type(edad))
edad = float(edad)
print(edad)
if isinstance(edad, int):
    print ('es int')
else:
    print ('no es int')

