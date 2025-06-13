# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:36:24 2025

@author: AULA
"""


Via = int(input("ingrese el numero de la via (1 o 2): "))

if(Via == 1):
  print("estas en la via #1")
  print("-------------------------")
  Color = input("ingrese el color de la via 1 (R - Rojo, A - Amarillo, V - Verde): ")
  if ('Color' == "R"):
      print("Detengase, porque el semaforo de la via # 2 esta en verde)")
  else:
      if (Color == "A"):
          print("Detengase, porque no hay cambio de color")
      else:
          print("Avance, la via # 2 esta en rojo")
if(Via == 2):
  print("estas en la via #2")
  print("-------------------------")
  Color = input("ingrese el color de la via 2 (R - Rojo, A - Amarillo, V - Verde): ")
  if ('Color' == "R"):
      print("Detengase, porque el semaforo de la via # 1 esta en verde)")
  else:
      if (Color == "A"):
          print("Detengase, porque no hay cambio de color")
      else:
          print("Avance, la via # 1 esta en rojo")

#%%+
Numero = int(input("ingrese un numero: "))

if (Numero  == 0):
    print("imprimiste el numero 0")
else:
    if(Numero%2==0):
        if(Numero > 0):
            print("El numero es positivo par")
        else:
            print("El numero es negativo par")
    else:
        if(Numero < 0):
            print("El numero es negativo impar")
        else:
            print("El numero es negativo impar")

#%%

numero = int(input("ingrese un numero: "))

if(numero==0):
    print("ingresaste el numero 0")
elif(numero > 0) and (numero%2 == 0):
    print("El numero es par positivo")
elif(numero > 0) and (numero%2 != 0):
    print("El numero es impar positivo")
elif(numero < 0) and (numero%2 == 0):
    print("El numero es negativo par")
elif(numero < 0) and (numero%2 != 0):
    print("El numero es impar negativo")
    
    
#%%
anio = int(input("Ingrese el año: "))

if (anio > 0) and (anio % 100 != 0) and (anio%4 == 0) or (anio % 400 == 0):
    mes = int(input("Ingrese el mes en numero: "))
    if (0 < mes < 13 ):
        if (mes == 4) and (mes == 6) and (mes == 9) and (mes == 11):
            dia = int(input("Ingrese el día: "))
            if (0 < dia < 31):
                print(" La fecha es correcta")
                print(f"{anio}:{mes}:{dia}")
            else:
                print("No es un día dentro del mes")
        elif (mes == 2):
            dia = int(input("Ingrese el día: "))
            if (0 < dia < 30):
                print(" La fecha es correcta")
                print(f"{anio}:{mes}:{dia}")
            else:
                print("No es un día dentro del mes")  
        else:
            dia = int(input("Ingrese el día: "))
            print(" La fecha es correcta")
            print(f"{anio}:{mes}:{dia}")
    else:
        print("El mes debe estar entre 1 y 12")
else:
    mes = int(input("Ingrese el mes en numero: "))
    if (0 < mes < 13 ):
        if (mes == 4) and (mes == 6) and (mes == 9) and (mes == 11):
            dia = int(input("Ingrese el día: "))
            if (0 < dia < 31):
                print(" La fecha es correcta")
                print(f"{anio}:{mes}:{dia}")
            else:
                print("No es un día dentro del mes")
        elif (mes == 2):
            dia = int(input("Ingrese el día: "))
            if (0 < dia < 29):
                print(" La fecha es correcta")
                print(f"{anio}:{mes}:{dia}")
            else:
                print(" La fecha no es correcta")
                print("No es un día dentro del mes")  
        else:
            dia = int(input("Ingrese el día: "))
            print(" La fecha es correcta")
            print(f"{anio}:{mes}:{dia}")
    else:
        print("El mes debe estar entre 1 y 12")
    
    
#%%
    
    
    
    
    
    
    
    
    
    