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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    