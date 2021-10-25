def cuenta_letras_2():
    palabra=raw_input("Escribe una palabra: ")
    cont=0
    vocal=0
    cons=0
    while(cont<len(palabra)):
        if(palabra[cont]in "aeiou"):
            vocal=vocal+1
        else:
            cons=cons+1

        cont=cont+1
    print("Vocales " + str(vocal))
    print("Consonantes " + str(cons))
    print("Total de letras "+ str(vocal + cons))
cuenta_letras_2()
