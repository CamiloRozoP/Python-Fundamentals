print ('Este agrupa de 20 en 20 hasta 1000')
numero=0
while True:
    for x in range (0,20):
        numero=numero+1
        print (numero)
    n = input( '¿Desea continuar S/N?')
    if n.strip() == 'N':
            break

input()
