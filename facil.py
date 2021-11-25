#errores corregidos 
def facil():
    nombre=raw_input("Dime nombre: ")
    if (nombre[0]=="A" or nombre[0]=="z"):
        print("tu nombre va primero o ultimo ")
    else:
        print("Tu nombre no va el primero ")
        for cont in range (1,4):
            print("adios")
facil()
