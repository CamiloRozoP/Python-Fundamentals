print ('Calcula la media y la suma de 1 hasta 200')
lista= [23, 45, 68, 99, 10, 15, 4]
pos=0
mayor=lista[0]
for x in range (1,6):
    if mayor<lista[x]:
        pos=x

print('El numero mayor se encuentra en la posicion  ',pos+1)
input()
