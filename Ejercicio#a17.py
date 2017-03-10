print ('Este programa solo lee los negativos de 10 entradas')
sumador=0
for x in range (0,10):
    numero=(float(input()))
    if numero<0:
        sumador+=numero
        print ('la suma es ' , sumador)
input()
