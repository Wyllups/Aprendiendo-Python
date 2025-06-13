# -*- coding: utf-8 -*-
"""
Created on Tue May  6 07:56:22 2025

@author: AULA
"""


def sumar (a,b):
    c = (a + b)
    return c 

def restar (a,b):
    c = (a - b)
    return c

def multiplicar (a,b):
    c = (a * b)
    return c

def dividir (a,b):
    c = (a / b)
    return c 

def potencia (a,b):
    c = (a**b)
    return c 

def modulo (a,b):
    c = (a % b == 0)
    return c

def raiz (a,b):
    c = (a**1/b)
    return c 

#%%

def sumar_numeros():
    try:
        cantidad = int(input("Cuántos números deseas sumar? "))
        suma = 0
        for i in range(1, cantidad + 1):
            numero = int(input(f"Ingrese el número {i}: "))
            suma += numero
        print(f"La suma total es: {suma}")
    except ValueError:
        print("Por favor, ingresa solo números enteros válidos.")

sumar_numeros()

#%%

numeros = ( 4,6,7,8,9,10 )

def sumar_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

resultado = sumar_numeros(numeros)
print(f"La suma de los elementos : {resultado} " )

#%%



















































