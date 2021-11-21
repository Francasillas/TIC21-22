##def mayor(num1,num2,num3):
##    mayor=0
##    if(num1>num2 and num2>num3):
##    mayor=num1
##    else:
##        (num2>num1 and num1>num3)
##        mayor=num2
##        else:
##            (num3>num1 and num1>num2)
##            mayor=num3
            



import random
def dados():
    print("PRIMERA TIRADA")

        for cont in range(1,2):
            num1=random.randint(1,6)
            print(num1)
        for cont in range(1,2):
            num2=random.randint(1,6)
            print(num2)
        for cont in range(1,2):
            num3=random.randint(1,6)
            print(num3)  
        
        suma1=num1+num2+num3
        print("EN TOTAL HA SACADO: "+(suma1))

    #print("SEGUNDA TIRADA")
    #for cont in range(1,4):
      # num2=random.randit(1,6)
      #  print(num4)


    
    #print("TERCERA TIRADA")




dados()
