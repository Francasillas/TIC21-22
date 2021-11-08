def cambiavocales_4():
    palabra=raw_input("dime palabra ")
    cont=0
    vocal=raw_input("Dime vocal ")
    while(cont<len(palabra)):
        if(palabra[cont]in'aeiou'):
            print(vocal)
        else:
            print(palabra[cont])
    cont=cont+1
    print("TU PALABRA TRANSFORMADA ES: "+(palabra))
           
   
                           
cambiavocales_4()
