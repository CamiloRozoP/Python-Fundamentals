print ('Determina la posicion del maximo y minimo')
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sumador=0
sumador1=0
for x in range (0,20):
    if x%2==0:
        sumador=lista[x]+sumador
    else:
        sumador1+=lista[x]

print('La media de los numeros en posiciones pares es',sumador)
print('La media de los numeros en posiciones impares es',sumador1)
input()
