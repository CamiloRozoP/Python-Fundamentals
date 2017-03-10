print ('Suma un segundo a la hora')

hora=int(input('ingrese la hora maximo 24 \n'))
while not hora<25:
    hora=int(input('ingrese la hora maximo 24 \n'))

minutos=int(input('ingrese los minutos maximo 60 \n'))
while not minutos<61:    
    minutos=int(input('ingrese los minutos maximo 60 \n'))
    
segundos=int(input('ingrese los segundos maximo 60 \n'))
while not segundos<61:
    segundos=int(input('ingrese los segundos maximo 60 \n'))
print ('La hora ingresada es [',hora,':',minutos,':',segundos,']')
segundos=segundos+1

if segundos>60:
    segundos=0
    minutos=minutos+1
    if minutos > 60:
        minutos=0
        hora=hora+1
        if hora>24:
            hora=0
print ('La hora sumandole un segundo es [',hora,':',minutos,':',segundos,']')

print('Segunda parte programa ciclo while 1 a 10')
numero=0
while numero<10:
    print(numero+1)
    numero=numero+1
input()
