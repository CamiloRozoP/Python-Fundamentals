lista = ['a','e','i','o','u']
a=0
print ('Ingrese un caracter para indicar si es una vocal')
caracter=str(input())
for x in range (0,5):
    if caracter==lista[x]:
        a=a+1
if a>0:
    print('El caracter si es una vocal')
else:
    print('El caracter no es una vocal') 
    
input()
