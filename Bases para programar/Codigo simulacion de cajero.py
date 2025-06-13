# -*- coding: utf-8 -*-
"""
Created on Thu May 22 15:24:27 2025

@author: AULA
"""

import numpy as np
import matplotib.pyplot as plt

fil, col = 6, 6
matriz = np.zeros([fil,col])
matriz

matriz1 = np.ones([4,4])
matriz1

matriz[1,1] = 4

for fila in matriz:
    for columna in fila:
        matriz[fila,columna] = 1 

for fila in range(matriz.shape[0]):
    for columna in range(matriz[fila].shape[0]):
        if (fila == columna):
            matriz[fila,columna] = 1 

fil, col = 10 , 10

matriz3 = np.zeros([fil, col])

for fila in range(matriz.shape[0]):
    for columna in range(matriz3[fila].shape[0]):
        matriz3[fila][col-1-fila] = 1
        

#%%


import numpy as np
import matplotlib.pyplot as plt

# Crear una matriz de ceros de 6x6
fil, col = 6, 6
matriz = np.zeros([fil, col])

# Crear una matriz de unos de 4x4
matriz1 = np.ones([4, 4])

# Asignar el valor 4 en una posición específica de matriz
matriz[1, 1] = 4

# Rellenar la diagonal principal de matriz con 1
for fila in range(matriz.shape[0]):
    for columna in range(matriz.shape[1]):
        if fila == columna:
            matriz[fila, columna] = 1

# Crear una matriz de ceros de 10x10
fil, col = 10, 10
matriz3 = np.zeros([fil, col])

# Rellenar la anti-diagonal de matriz3 con 1
for fila in range(matriz3.shape[0]):
    matriz3[fila, col - 1 - fila] = 1

# Mostrar las matrices
print("Matriz con la diagonal principal rellenada:")
print(matriz)

print("\nMatriz con la anti-diagonal rellenada:")
print(matriz3)

# Visualizar la matriz3
plt.imshow(matriz3, cmap='gray')
plt.title('Matriz con la Anti-Diagonal Rellenada')
plt.show()
        
#%%

saldo = 1_500_000

def msaldo():
    return saldo

def retirar(valor):
    global saldo
    if (valor >= saldo):
        return("saldo insuficiente")
    else:
        saldo -= valor
        return valor

def consignar(valor):
    global saldo
    saldo += valor
    return saldo

def inicio():
    print("""
          
          Bienvenido a su cuenta personal 
          ------------------------------------------
          ¿Que transaccio desea realizar?:}
          
          1. Saldo
          2. Retirar
          3. Consignar
          ------------------------------------------
          """)
        
#%%
    

saldo = 1_500_000

def msaldo():
    """Devuelve el saldo actual."""
    return saldo

def retirar(valor):
    """Permite retirar un valor del saldo si es suficiente."""
    global saldo
    if valor > saldo:
        return "Saldo insuficiente"
    else:
        saldo -= valor
        return f"Has retirado {valor}. Tu saldo actual es {saldo}."

def consignar(valor):
    """Permite consignar un valor al saldo."""
    global saldo
    saldo += valor
    return f"Has consignado {valor}. Tu saldo actual es {saldo}."

def inicio():
    """Muestra el menú principal y permite realizar transacciones."""
    while True:
        print("""
        Bienvenido a su cuenta personal
        ------------------------------------------
        ¿Qué transacción desea realizar?
        
        1. Consultar saldo
        2. Retirar dinero
        3. Consignar dinero
        4. Salir
        ------------------------------------------
        """)
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            print(f"Su saldo actual es: {msaldo()}.\n")
        elif opcion == "2":
            try:
                valor = int(input("Ingrese el valor a retirar: "))
                print(retirar(valor))
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.\n")
        elif opcion == "3":
            try:
                valor = int(input("Ingrese el valor a consignar: "))
                print(consignar(valor))
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.\n")
        elif opcion == "4":
            print("Gracias por usar nuestros servicios. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.\n")

inicio()

#%%


saldo = 1_500_000  # Saldo inicial de la cuenta

def msaldo():
    """Devuelve el saldo actual."""
    return saldo

def retirar(valor):
    """Permite retirar un valor del saldo si es suficiente."""
    global saldo
    if valor > saldo:
        return "Saldo insuficiente"
    else:
        saldo -= valor
        return f"Has retirado {valor}. Tu saldo actual es {saldo}."

def consignar(valor):
    """Permite consignar un valor al saldo."""
    global saldo
    saldo += valor
    return f"Has consignado {valor}. Tu saldo actual es {saldo}."

def inicio():
    """Muestra el menú principal y permite realizar transacciones."""
    while True:
        print("""
        Bienvenido a su cuenta personal
        ------------------------------------------
        ¿Qué transacción desea realizar?
        
        1. Consultar saldo
        2. Retirar dinero
        3. Consignar dinero
        4. Salir
        ------------------------------------------
        """)
        opcion = input("Seleccione una opción (1-4): ")
        
        match opcion:
            case "1":
                print(f"Su saldo actual es: {msaldo()}.\n")
            case "2":
                try:
                    valor = int(input("Ingrese el valor a retirar: "))
                    print(retirar(valor))
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.\n")
            case "3":
                try:
                    valor = int(input("Ingrese el valor a consignar: "))
                    print(consignar(valor))
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.\n")
            case "4":
                print("Gracias por usar nuestros servicios. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.\n")

# Ejecutar el programa
inicio()

#%%

saldo = 1_500_000

def msaldo():
    print(f" Su saldo es {saldo}")

def retirar(valor):
    global saldo
    if (valor >= saldo):
        return("saldo insuficiente")
    else:
        saldo -= valor
        return valor

def consignar(valor):
    global saldo
    saldo += valor
    return saldo

def inicio():
    print("""
          
          Bienvenido a su cuenta personal 
          ------------------------------------------
          ¿Que transaccio desea realizar?:}
          
          1. Saldo
          2. Retirar
          3. Consignar
          ------------------------------------------
          """)
          
print(inicio())

opcion = int(input("seleccione una opcion"))

match opcion:
    case 1:
        msaldo()
    case 2:
        v = int(input("Ingrese su saldo a retirar:"))
        print(retirar(v))
    case 3:
        v = int(input("Ingrese su saldo a consignar:"))
        print(consignar())
    case _:
        print("No es una opcion valida")      
