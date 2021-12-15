
def evau():
    suma=0
    media=0
    
    print("**********************************************************")
    print("**********************CALCULADORA EVAU********************")
    print("**********************************************************")
    print("")    
    print("Introduce las carreras que deseas cursar (3, en orden)")
    primera=raw_input("primera opcion ")
    segunda=raw_input("segunda opcion ")
    tercera=raw_input("tercera opcion ")
    print("")
    
    #FASE OBLIGATORIA
    print("             ~ NOTAS FASE OBLIGATORIA ~")
    print("")
    i=input("nota ingles/frances evau: ")
    l=input("nota lengua evau: ")
    m=input("nota mates evau: ")
    h=input("nota historia evau: ")
    suma=float(suma)
    suma=str(i+l+m+h)
    media=float(suma)/4
    if(media<4):
        print("Tu media es menor a 4 por lo que no mediara ")
        media=0
    else:
        print("Tu nota media es de: "+ str(media))
    nota_obligatoria = media*0.4
    if(media<5):
        print("Estas suspendido por lo que no puedes continuar")
        quit()
    print("")
    
    #NOTA MEDIA BACHILLERATO
        
  
    print("             ~ NOTAS BACHILLERATO ~ ")
    print("")

    print("NOTA MEDIA PRIMERO")
    nmb1=input("Dime la nota media de primero: ")
    nmb2=input("Dime la nota media de segundo: ")
    suma2=str(nmb1+nmb2)
    media2=float(suma2)/2
    nmbt=media2*0.6
    print("Tu nota media de bachillerato es: "+str(media2))
    print("")
   
    
    #NOTA ACCESO
    nota_acceso=nmbt+nota_obligatoria
    print("tu nota de acceso es: "+str(nota_acceso))
    if(nota_acceso<5):
        print("Estas suspendido por lo que no puedes continuar")
        quit()
    print("")
        

    #FASE VOLUNTARIA
    print("             ~ NOTAS FASE VOLUNTARIA ~")
    print("")
    voluntaria=input("Nota primera materia voluntaria: ")
    voluntaria2=input("Nota segunda materia voluntaria: ")
    if (voluntaria<5):
        print("Como tu primera nota es menor de 5, no ponderara")
        voluntaria=0
    if (voluntaria2<5):
        print("Como tu segunda nota es menor de 5, no ponderara")
        voluntaria2=0
    nota_voluntaria=voluntaria*0.2 + voluntaria2*0.2
    nota_admision=nota_acceso+nota_voluntaria
    print("")
    print("                 ~ LA NOTA FINAL ~")
    print("")
    print("Tu nota final de la evau es: "+ str(nota_admision))
    
        
        
    
evau()
