def cambiavocales_3():
    palabra=raw_input("dime una palabra ")
    cont=0
    nueva_palabra=" "
    vocal=raw_input("dime una vocal ")
    while(cont<len(palabra)):
        if(palabra[cont]=="a"):
            nueva_palabra=nueva_palabra+vocal
        else:
            if(palabra[cont]=="e"):
                    nueva_palabra=nueva_palabra+vocal
            else:
                if(palabra[cont]=="i"):
                        nueva_palabra=nueva_palabra+vocal
                else:
                    if(palabra[cont]=="o"):
                        nueva_palabra=nueva_palabra+vocal
                    else:
                        if(palabra[cont]=="u"):
                            nueva_palabra=nueva_palabra+vocal
                        else:
                            nueva_palabra=nueva_palabra+(palabra[cont])
        cont=cont+1
        print("La palabra transformada es: "+nueva_palabra)
cambiavocales_3()
