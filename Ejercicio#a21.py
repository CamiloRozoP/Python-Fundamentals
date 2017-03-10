print ('Suma de los pares e impares de un arreglo')
lista= [-2, 5, 8, -9, 10, 15,-4]
sumapares=0
sumaimpares=0
for x in range (0,7):
    if lista[x]%2==0:
        sumapares+=lista[x]
    else:
        sumaimpares+=lista[x]

print('La suma de los pares es ',sumapares)
print('La suma de los impares es ',sumaimpares)
input()
