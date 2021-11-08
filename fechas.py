def fechas ():
    x=raw_input("dime una fecha (dd/mm/aa) ")
    mes="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    num=x[3]+x[4]
    s=int(num)*3
    palabra= (mes[s-3]+mes[s-2]+mes[s-1])
    print("Estas en el mes de "+ palabra)
fechas ()
