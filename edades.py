def edades():
   
    suma=0
    num=input("Dime una edad ")
    mayor=num
    menor=num
    suma=suma+num
    for cont in range(1,4):
        num=input("Dime una edad ")
        if(num>mayor):
            mayor=num
        if(num<menor):
            menor=num
        suma=suma+num
    media=suma/4.0
    print("Mayor= "+str(mayor))
    print("Menor= "+str(menor))
    print("Media= "+str(media))
edades()
