def palabra2 ():
    nombre = raw_input ("NOMBRE: ")
    apellido = raw_input ("APELLIDO: ")
    print ("BUENOS DIAS, " + nombre + " " + apellido)
    print ("tu lindo nombre empieza por la letra " + nombre[0])
    print ("Voy a deletrear tu nombre")
    for cont in range (0, 20):
        print (nombre[cont])
palabra2 ()
