def cambiavocales_2():
    palabra=raw_input("dime una palabra ")
    cont=0
    vocal=raw_input("dime una vocal ")
    while(cont<len(palabra)):
        if(palabra[cont]=="a"):
           print(vocal)
        else:
            if(palabra[cont]=="e"):
                print(vocal)
            else:
                if(palabra[cont]=="i"):
                     print(vocal)
                else:
                    if(palabra[cont]=="o"):
                        print(vocal)
                    else:
                        if(palabra[cont]=="u"):
                            print(vocal)
                        else:
                            print(palabra[cont])
        cont=cont+1
cambiavocales_2()
