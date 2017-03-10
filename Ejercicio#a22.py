print ('Determina la posicion del maximo y minimo')
lista = [10]


for x in range (0,10):
    numero=int(input())
    lista.insert(x,numero)
mayor=lista[0]
menos=lista[0]
posicion=lista[0]
posicion1=lista[0]
for y in range (0,10):
    if mayor<lista[y]:
        mayor=lista[y]
        posicion=y
    if menos>lista[y]:
        menos=lista[y]
        posicion1=y
print('La posicion del mayor numero es  ',posicion,'Del numero', mayor)
print('La posicion del menor numero es  ',posicion1,'Del numero ',menos)

input()
