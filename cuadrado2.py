def cuadrado2():
    fila=" "
    num=input("Dame un numero: ")
    for fil in range(1,num+1):
        for col in range(1,num+1):
            if (fil%2==0 and col%2==1):
                fila=fila+"0"
            else:
                if(fil%2==1 and col%2==0):
                    fila=fila+"0"
                else:
                    fila=fila+"1"
        print(fila)
        fila=" "
cuadrado2()
