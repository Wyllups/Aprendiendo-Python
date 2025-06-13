# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 07:31:54 2025

@author: AULA
"""

# lista
lista = ["Wilfredo", "Felipe", "Luis", "Roger", "Nicolas"]

# Tupla
codigo = (101, 102, 103, 104, 105)

# Diccionario
estudiante = {
    "Wilfred0":101,
    "Felipe":102,
    "Luis":103,
    "Roger":104,
    "Nicolas":105,
    }


# Conjunto
notas = {
      4.5,
      4.6,
      4.0,
      4.6,
      5.0
      }

print(lista)
print(codigo)
print(estudiante)
print(notas)

print(len(lista))
len(notas)


numero1 = 5
numero2 = input("Ingrese un numero")
numero3 = int(input(" Ingrese un numero "))


#%% Ejercicio 1


numero = int(input("ingrese un numero: "))
# condicional
 
if (numero%2 == 0): 
    print("El numero es par")
    
print("Fin algoritmo...!!!!")

#%% Ejercicio 2 

numero = int(input("ingrese un numero: "))
# condicional
 
if (numero%2 != 0): 
    print("El numero es inpar")
    
print("Fin algoritmo...!!!!")


#%% Ejercicio 3 - Sentencia else - sinio

numero = int(input("ingrese un numero: "))
# condicional
 
if (numero%2 == 0): 
    print("El numero es par")
else:
    print("El numero es inpar")
    
print("Fin algoritmo...!!!!")

#%% Ejercicio 4 

numero = 1.83
# condicional
 
if (type(numero) == int) :
    print("El numero es entero")
else:
    print("El numero es decimal")
    
print("Fin algoritmo...!!!!")

#%% Ejercicio 5

nombre = input("ingrese su primer nombre: ")
# condicional

if (len(nombre) <= 5) :
    print("Salen temprano")
else:
    print("Sale a la hora normal")
    
print("Fin algoritmo...!!!!")

#%%