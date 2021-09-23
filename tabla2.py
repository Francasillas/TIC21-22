def tabla2():
    numero=input("Que tabla quieres ")
    print("============================")
    print("          TABLA " + str(numero))
    print("===========================")
    print("AHI VA")
    for cont in range (0,11):
        print(str(numero)+ " x " + str(cont)+ " = " + str(cont*numero))
    print("EUREKA")
tabla2()
