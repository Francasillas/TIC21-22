def gauss_total():
  n=input("Hasta que numero quieres que cuente: ")
  suma_par=0
  suma_impar=0
  suma=0
  resto= 0
  for cont in range( 1,n+1):
    resto=cont%2
    suma=suma+cont
    if(resto==0):
        suma_par=suma_par+cont
    else:
           suma_impar=suma_impar+cont
           
    print(str(cont)+" pares = "+ str(suma_par)+" impares = "+str(suma_impar))
    print("la suma de los pares=" + str(suma_par))
    print("la suma de los impares=" + str (suma_impar))
    print("la suma TOTAL="+str(suma))
gauss_total()
