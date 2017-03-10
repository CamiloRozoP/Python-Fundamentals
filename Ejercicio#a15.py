print ('Calcula la media y la suma de 1 hasta 200')
numero=0
sumapares=0
sumaimpares=0
media=0
media1=0
for x in range (0,201):
    if numero%2==0:
        sumapares=numero+sumapares
        media=sumapares/100
    else:
        sumaimpares=numero+sumaimpares
        media1=sumapares/100
    numero=numero+1

print('La suma de numeros pares es ',sumapares)
print('La suma de numeros impares es ',sumaimpares)
print('La media de numeros pares es ',media)
print('La media de numeros impares es ',media1)
input()
