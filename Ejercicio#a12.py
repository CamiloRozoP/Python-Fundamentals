print ('Ingrese el capital')
capital=int(input())
capital1=capital
for x in range (1,20):
    capital=capital+capital*0.05
    print ('el capital es',capital,'en el año',x) 
    if capital1*2<capital:
        print ('el capital se duplica en',x,'años')
        break
    
input()
