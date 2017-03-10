print ('Intercambio de numero 1 si es mayor ')
num1=int(input('ingrese el numero 1 \n'))
num2=int(input('ingrese el numero 2 \n'))
aux=0
if num1>num2:
    aux=num2
    num2=num1
    num1=aux
print ('El numero 1 ahora es ',num1)
print ('El numero 2 ahora es ',num2)
input()
