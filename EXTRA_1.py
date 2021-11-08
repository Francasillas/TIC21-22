def EXTRA_1():
    num =input("Dime un numero ")
    cont=0
    continuar= "si"
    
    while(continuar=="si"):
            num2= input("Por que numero quieres multiplicarlo? ")
            print(str(num)+" x "+str(num2)+ " = "+str(num*num2))
            
            continuar= raw_input("Quieres otra cuenta? (si/no) ")
            if(continuar=="no"):
                print("MUY BIEN ")
                print("Hasta la proxima")
               
EXTRA_1()
