print ('Suma de los numeros pares')
lista = [20]
numlista=0
sumador=0
for x in range (1,41):
    if x%2==0:
        lista.insert(numlista,x)
        numlista+=1
for y in range (0,20):
    print (lista[y])
    sumador=lista[y]+sumador

print('La suma del arreglo es ',sumador)
input()
