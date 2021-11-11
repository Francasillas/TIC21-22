def pinta_menu():
    print("**************************************")
    print("***               MENU             ***")
    print("**************************************")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")

def manda_error():
    print("ELECCION ERRONEA, NO SE PUEDE DIVIDIR POR 0")
   
def suma(num1,num2):
    respuesta=num1+num2
    return(respuesta)

def resta(num1,num2):
    respuesta=num1-num2
    return(respuesta)

def multiplicacion(num1,num2):
    respuesta=num1*num2
    return(respuesta)

def division(num1,num2):
    respuesta=float(num1)/float(num2)
    return(respuesta)

def menu_2():
    #Pedimos dos numeros
    error=1
    while(error==1):
        num1=input("Introduce un numero: ")
        num2=input("Introduce otro numero: ")
        opcion=0
       
        pinta_menu()
       
        while(opcion<=0 or opcion>4):
            opcion=input(" ELIGE: ")
            if(num2==0 and opcion==4):
                error=1
                manda_error()
            else:
                error=0
                print("Has elegido la opcion "+str(opcion))
               
    #OPCION SUMA
    if(opcion==1):
        print(suma(num1,num2))
    #OPCION RESTA
    if(opcion==2):
        print(resta(num1,num2))
    #OPCION PRODUCTO
    if(opcion==3):
        print(multiplicacion(num1,num2))
    #OPCION COCIENTE
    if(opcion==4):
        print(division(num1,num2))
   
menu_2()
