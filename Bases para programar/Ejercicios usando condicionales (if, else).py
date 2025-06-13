# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 18:15:48 2025

@author: Wilfredo
"""
#%%
"Ejercicio #1"
#Escribir un programa que solicite al usuario un valor. Si el valor es positivo, 
#pedir un segundo valor y calcular la suma, resta y producto de ambos. 
#Mostrar los resultados por pantalla.

print("Bienvenidos a calculadora de Wil")
print("----------------------------------------------------------------")
x = int(input("ingrese un valor numerico positivo: "))

print("----------------------------------------------------------------")
if(x > 0): 
    print("El valor es correcto")
    print("----------------------------------------------------------------")
    y = int(input("Ingrese un segundo valor numerico positivo: ")) 
    print("----------------------------------------------------------------")
    if (y > 0): 
      print("El valor es correcto")
      print("----------------------------------------------------------------")
      print("Suma de los valores")
      print(x,"+",y,"=",(x+y))
      print("----------------------------------------------------------------")
      print("Resta de los valores") 
      print(x,"-",y,"=",(x-y))
      print("----------------------------------------------------------------")
      print("Multiplicacion de los valores")  
      print(x,"*",y,"=",(x*y))
      print("----------------------------------------------------------------")
      print("Division de los valores")  
      print(x,"÷",y,"=",(x/y))
      print("----------------------------------------------------------------")
    else:
      print("El valor es incorrecto, intentelo nuevamente")
else:   
    print("El valor es incorrecto, intentelo nuevamente")
print("Gracias por su visita")
print("Hasta pronto :)")

#%% 
"Ejercicio #2"
#Escribir un programa que calcule el mayor de dos números enteros introducidos 
#por teclado.

print("Bienvenidos")
print("----------------------------------------------------------------")
numero1 = int(input("ingrese un valor numerico: "))
numero2 = int(input("ingrese un segundo valor numerico: "))
print("----------------------------------------------------------------")
if(numero1 > numero2):
  print("El valor", numero1, "es mayor que", numero2)
else:
  if(numero1 == numero2):
    print("Los valores son iguales")
  else:
    if(numero1 < numero2):
       print("El valor", numero2, "es mayor que", numero1)
print("----------------------------------------------------------------")
print("Gracias por su visita")
print("Hasta pronto :)")

#%%
"EJERCICIO 3"
#Escribir un programa que calcule el mayor de tres números enteros introducidos 
#por teclado.

"Ejercicio #3"
print("Bienvenidos")
numero1 = int(input("ingrese un valor numerico: "))
numero2 = int(input("ingrese un segundo valor numerico: "))
numero3 = int(input("ingrese un tercer valor numerico: "))
print("----------------------------------------------------------------")
if(numero1 > numero2 and numero1 > numero3):
  print("El valor", numero1, "es mayor que", numero2, "y", numero3)
else:
  if(numero1 == numero2 and numero1 > numero3 ):
    print("Los valores",numero1, "y", numero2, "son iguales y mayores que", numero3)
  else:
    if(numero1 == numero2 and numero1 < numero3):
     print("Los valores",numero1, "y", numero2, "son iguales y menores que", numero3)
    else:
      if(numero2 > numero1 and numero2 > numero3):
        print("El valor", numero2, "es mayor que", numero1, "y", numero3)
      else:
        if(numero2 == numero3 and numero2 > numero1):
          print("Los valores",numero2, "y", numero3, "son iguales y mayores que", numero1)
        else:
          if(numero2 == numero3 and numero2 < numero1):
            print("Los valores",numero2, "y", numero3, "son iguales y menores que", numero1)
          else:
            if(numero3 > numero1 and numero3 > numero2):
              print("El valor", numero3, "es mayor que", numero1, "y", numero2)
            else:
              if(numero3 == numero1 and numero3 > numero2):
                print("Los valores",numero3, "y", numero1, "son iguales y mayores que", numero2)
              else:
                if(numero3 == numero1 and numero3 < numero2):
                  print("Los valores",numero3, "y", numero1, "son iguales y menores que", numero2)
                else:
                  if(numero1 == numero2 and numero1 == numero3):
                    print("Los valores son iguales")
print("----------------------------------------------------------------")
print("Gracias por su visita")
print("Hasta pronto :)")
  
#%%
"EJERCICIO #4"
#Escribir un programa que calcule el mayor de cuatro números enteros 
#introducidos por teclado.

print("Bienvenidos")
print("Los valores deben ser diferentes")
numero1 = int(input("ingrese un valor numerico: "))
numero2 = int(input("ingrese un segundo valor numerico: "))
numero3 = int(input("ingrese un tercer valor numerico: "))
numero4 = int(input("ingrese un cuarto valor numerico: "))
print("----------------------------------------------------------------")

if(numero1 > numero2 and numero1 > numero3 and numero1 > numero4):
   print("El valor", numero1, "es mayor que", numero2,",",numero3, "y", numero4)
elif(numero2 > numero1 and numero2 > numero3 and numero2 > numero4):
    print("El valor", numero2, "es mayor que", numero1, ",", numero3,"y", numero4)
else:
    if(numero3 > numero1 and numero3 > numero2 and numero3 > numero4):
        print("El valor", numero3, "es mayor que", numero1, ",", numero2, "y", numero4)
    elif(numero4 > numero1 and numero4 > numero2 and numero4 > numero3):
        print("El valor", numero4, "es mayor que", numero1, ",", numero2, "y", numero3)
        
print("----------------------------------------------------------------")
print("Gracias por su visita")
print("Hasta pronto :)")
    

#%%
"EJERCICIO #5"
#Determinar en que estado está el agua en función de su temperatura. 
#Si es negativa el estado será sólido, si es menor que 100 será líquido y si es 
#mayor que 100 será gas. Pedir al usuario el valor de la temperatura.

print("Bienvenidos")

print("--------------------------------------------")

temperatura = int(input("ingrese la temperatura del agua en °C  "))

print("--------------------------------------------")

if(temperatura > 100):
    print('El agua se encuentra en estado gaseoso')
elif(0 < temperatura < 100): 
    print("El agua se encuentra en estado liquido")
else:
    if(temperatura < 0):
        print("El agua esta en estado solido")

print("--------------------------------------------")
print("Gracias por su visita")
print("Hasta pronto :)")
    
#%%
"Ejercicio #6"
#Un año es bisiesto si es divisible por 4 y no es por 100, 
#o si es divisible por 400. Escribe un programa que lea un año y devuelva si es 
#bisiesto o no.

print("Bienvenidos")

print("--------------------------------------------")

año = int(input("ingrese un año para saber si es bisiesto o no: "))

print("--------------------------------------------")

if( año%100 != 0 and año%4 == 0 or año%400 == 0 ):
    print("El año digitado es bisiesto")
else:
    print("El año no es bisiesto")

print("--------------------------------------------")
print("Gracias por su visita")
print("Hasta pronto :)")

#%%
"EJERCICIO #7"
#Pedir un mes (número) y mostrar el nombre del mes. Solicitar al usuario la 
#inicial del día de la semana y mostrar el nombre del día completo. La letra 
#inicial puede ser mayúscula o minúscula. Usar la x para el miércoles.

#lista 
mes = ["Mes invalido","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
         "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

print("Bienvenidos")

print("--------------------------------------------") 

numero = int(input("Ingrese el mes en numero  "))

if(12>numero>1):
    print("El mes es:",(mes[(numero)]))
else:
    print("El numero de mes es invalido")
    
print("--------------------------------------------") 

#Diccionario
dias = {
    'l': 'Lunes',
    'm': 'Martes',
    'x': 'Miércoles',
    'j': 'Jueves',
    'v': 'Viernes',
    's': 'Sábado',
    'd': 'Domingo'
}


inicial = input("Introduce la inicial del día de la semana: ").lower()

print("--------------------------------------------")

if inicial in dias:
    print("El día  es:", dias[(inicial)])
else:
    print("Inicial no válida. Por favor, introduce una inicial válida.")

print("--------------------------------------------")
print("Gracias por su visita")
print("Hasta pronto :)")

#%%
"EJERCICIO#8"

#Solicitar al usuario una fecha (dd:mm:aaaa) y comprobar si es correcta.
#que una fecha sea correcta es necesario:
# El año debe ser mayor que cero.
# El mes debe estar entre 1 y 12.
# Dependiendo del mes que sea, el día debe estar dentro de los límites válidos.
# Los meses que tienen 31 días son 1, 3, 5, 7, 8, 10 y 12. 
# Los meses de 30 días son 4, 6, 9 y 11.
# El mes de 28 días es 2, excepto en un año bisiesto que es 29 días.

print("Bienvenidos")

print("--------------------------------------------") 

year = int(input("Ingrese numero de año: "))

if(year > 0) and (year%100 != 0) and (year%4 == 0) or (year%400 == 0 ):
    mes = int(input("Ingrese numero de mes: "))
    if(mes>13) and (mes<0):
        if (mes == 4)and(mes == 6)and(mes == 9)and(mes == 4):
            dia = int(input("Ingrese numero de dia: "))
            if ( 0 < dia < 31):
                print("La fecha es correcta")
                print(f"{year}:{mes}:{dia}")
        elif (mes==2):
            dia = int(input("Ingrese numero de dia"))
            if(0<dia<30):
                print("La fecha es correcta")
                print(f"{year}:{mes}:{dia}")
        else:
            dia = int(input("Ingrese el dia"))
            print("La fecha es correcta")
            print(f"{year}:{mes}:{dia}")
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    




































