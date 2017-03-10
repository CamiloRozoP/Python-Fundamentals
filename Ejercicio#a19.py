print ('Media aritmetica de 5 numeros en 1 arreglo')
lista = [5]
sumador=0
for x in range (0,5):
    numero = int(input())
    lista.insert(x,numero)
    sumador=lista[x]+sumador
print('La suma del arreglo es ',sumador/5)
input()
