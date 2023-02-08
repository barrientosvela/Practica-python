edad = 5
if edad!=5:
    print('has cambiado el programa')

while edad<10:
    print(edad)
    edad+=1

for i in range(5):
    print('rango ',i)
    if i==2:
        print('stop')
        break # sale del bucle
    print('fin')

for i in range(5):
    print('rango ',i)
    if i==2:
        print('stop')
        continue # sale de esta iteración y vuelve al bucle
    print('fin')
else:
    print('cuando termina el for')

n = int(input('divide 5 entre: '))
try:
    result = 5/n # / división normal // división entera
except:
    print('error','no se puede dividir entre',n)
else:
    print('resultado=',result)
finally:
    print('error o no se acabó')

i=5
match i>0:
    case 2:
        print("es 2")
    case 5:
        print("es 5")
    case True:
        print("verdad")
    case _:
        print("ni uno ni otro")

