def tabla():
    num=input("Dame un numero: ")
    suma=1
    cont=0
    for cont in range(num,-1,-1):
        print(cont,suma)
        suma=cont*suma
        print("final")
tabla()
