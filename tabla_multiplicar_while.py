def multiplicar_while ():
    num=input("Dime un numero: ")
    print("***************************************")
    print("*************"+" TABLA DEL "+ str(num)+" *************")
    print("***************************************")
    cont=0
    while (cont<21):
        print(str(num)+" x "+str(cont)+ " = "+str(num*cont))
        cont=cont+1


    
multiplicar_while()
