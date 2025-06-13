# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 23:39:01 2025

@author: Wilfredo
"""

""" 3 1. Ejercicio:
Elabora una condicional que calcule el valor de x!.
El programa debe pedir al usuario el número al que se le quiere calcular el factorial
Recuerda que:

x! = x(x − 1)(x − 2)...[x − (x − 1)]"""


x = int(input("Introduce un número entero para calcular su factorial: "))

# Verificar si el número es no negativo
if x < 0:
    print("El factorial no está definido para números negativos.")
elif x == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    print(f"El factorial de {x} es {factorial}.")
    

#%%

"""4 2 . Ejercicio
Elabora un algoritmo que identifique los números mayores a 1.
lista = [5,4,2,-4,0,20,50] """

lista = [5, 4, 2, -4, 0, 20, 50]

numeros_mayores_a_1 = [numero for numero in lista if numero > 1]

print(f"Los números mayores a 1 en la lista son: {numeros_mayores_a_1}")

#%%

"""(1.6 puntos) Desarrolle un programa que pida al usuario un correo electrónico y éste valide: * si
es un correo electrónico o no * cuántos puntos tiene * cuántos numeros tiene """

correo = input("Introduce un correo electrónico: ")

# Validar si contiene un '@' y un '.'
if '@' in correo and '.' in correo:
    print("El correo ingresado es válido.")
else:
    print("El correo ingresado no es válido.")


cantidad_puntos = 0
cantidad_numeros = 0


for caracter in correo:
    if caracter == '.':
        cantidad_puntos += 1
    elif caracter.isdigit():
        cantidad_numeros += 1

print(f"Cantidad de puntos en el correo: {cantidad_puntos}")
print(f"Cantidad de números en el correo: {cantidad_numeros}")

#%%

"""(1.6 puntos) Desarrolle un programa que pida al usuario un número y me valide: * Si es un
número primo * si es un número par o impar * si es un número cuadrado. """



n = int(input("Introduce un número entero: "))


es_primo = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
paridad = "par" if n % 2 == 0 else "impar"
es_cuadrado = int(n**0.5)**2 == n


print(f"{n} {'es primo' if es_primo else 'no es primo'}, es {paridad}, y {'es' if es_cuadrado else 'no es'} un cuadrado perfecto.")

#%%

"""(1.8 puntos)Desarrolle un programa que pida al usuario una palabra y me valide si esta es un
palindromo o no """


palabra = input("Introduce una palabra: ").lower()


es_palindromo = True
for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-(i + 1)]:
        es_palindromo = False
        break


print(f"La palabra '{palabra}' {'es' if es_palindromo else 'no es'} un palíndromo.")