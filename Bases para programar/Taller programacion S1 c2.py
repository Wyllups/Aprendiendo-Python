# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:31:17 2025

@author: Wilfredo
"""

print("Bienvenid@ aqui puedes sumar una cantidad infinita de numero positivos enteros, al final puedes saber cuantos numeros pares y cuantos inpares ingresaste")
print("--------------------------------------------------------------------------------------------------------------")
suma = 0
contador_n_p = 0 
contador_n_n = 0 
numero_positivo = 1 

while numero_positivo > 0:
    numero_positivo = int(input("Ingrese numeros enteros positivos (-1 para salir):__ "))
    if(numero_positivo > 0):
        suma += numero_positivo
        print("La suma parcial es de:",(suma))
        if(numero_positivo %2==0):
            contador_n_p = contador_n_p + 1 
        if(numero_positivo %2!=0):
            contador_n_n = contador_n_n + 1 
if(numero_positivo == -1):
    print("--------------------------------------------------------------------------------------------------------------")
    print(f'La suma total de los numeros ingresados es de: {suma}')
    print("--------------------------------------------------------------------------------------------------------------")
    print(f'Los numeros pares ingresados fueron: {contador_n_p}')
    print("--------------------------------------------------------------------------------------------------------------")
    print(f'Los numeros inpares ingresados fueron: {contador_n_n}')


#%%

print("Bienvenid@ aqui puedes sumar tu compra")
print("--------------------------------------------------------------------------------------------------------------")
suma = 0
contador_productos = 0
precio = 1
producto = 0
while precio > 0:
    precio = float(input(f"Ingrese el costo del producto {producto +1} ($0 para terminar compra):$ "))
    producto = producto + 1
    if(precio > 0):
        suma += precio
        contador_productos = contador_productos + 1
if(precio == 0):
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"Total IVA : {suma*19/100:.2f}")
    print("--------------------------------------------------------------------------------------------------------------")
    print(f'Total a pagar : {suma:.2f}')
    print("--------------------------------------------------------------------------------------------------------------")
    print(f'Cantidad de productos : {contador_productos}')
    print("--------------------------------------------------------------------------------------------------------------")

#%%

print("Bienvenid@ aqui puedes calcular la tabla de multiplicar de cualquier numero")
print("--------------------------------------------------------------------------------------------------------------")

numero = int(input("Ingresa un numero para generar su tabla de multiplicar:__"))

print("\nTabla de multiplicar del numero", numero)
print("Multiplicadndo | Multiplicador | Producto")
print("--------------------------------------------------------------------------------------------------------------")

multiplicador = 1 
while multiplicador <= 12:
    producto = ( numero * multiplicador )
    print(f"{ numero:2} | {multiplicador:2} | {producto:2}")
    multiplicador += 1

#%%

numero = int(input('Ingrese un numero entero:_'))
while numero > 1:
    if (numero%2==0):
        numero = numero / 2
        print(f"{numero:.0f}")
    elif(numero%2!=0):
        numero = (numero * 3)+1
        print(f"{numero:.0f}")
if(numero == 1):
    print(f"Fin del ejercicio el numero es {numero:.0f}")

#%%

print("Bienvenid@s aqui puedes jugar con tu amig@ a piedra papel o tijera ")

print("--------------------------------------------------------------------------------------------------------------")

jugador1 = input("Jugador 1 ingrese su opcion (Piedra, Papel o Tijera):_").strip().lower()

print("--------------------------------------------------------------------------------------------------------------")

jugador2 = input("Jugador 2 ingrese su opcion (Piedra, Papel o Tijera):_").strip().lower()
opciones = ["piedra","papel","tijera"]

print("--------------------------------------------------------------------------------------------------------------")

if (jugador1 == "piedra" and jugador2 == "papel" or jugador1 == "papel" and jugador2 == "tijera" or jugador1 == "tijera" and jugador2 == "piedra"):
    
    print("--------------------------------------------------------------------------------------------------------------")
    
    print("El jugador 2 es el ganador")
elif(jugador2 == "piedra" and jugador1 == "papel" or jugador2 == "papel" and jugador1 == "tijera" or jugador2 == "tijera" and jugador1 == "piedra"):
    
    print("--------------------------------------------------------------------------------------------------------------")
    
    print("El jugador 1 es el ganador")

while (jugador1 == jugador2):
    
    print("--------------------------------------------------------------------------------------------------------------")
    
    print ("Es un empate intentenlo nuevamente")
    
    print("--------------------------------------------------------------------------------------------------------------")
    
    jugador1 = input("Jugador 1 ingrese su jugada (Piedra, Papel o Tijera)").strip().lower()
    
    print("--------------------------------------------------------------------------------------------------------------")
    
    jugador2 = input("Jugador 1 ingrese su jugada (Piedra, Papel o Tijera)").strip().lower()
    
    print("--------------------------------------------------------------------------------------------------------------")
    
    opciones = ["piedra","papel","tijera"]
    if (jugador1 == "piedra" and jugador2 == "papel" or jugador1 == "papel" and jugador2 == "tijera" or jugador1 == "tijera" and jugador2 == "piedra"):
        
        print("--------------------------------------------------------------------------------------------------------------")
        print("El jugador 2 es el ganador")
    elif(jugador2 == "piedra" and jugador1 == "papel" or jugador2 == "papel" and jugador1 == "tijera" or jugador2 == "tijera" and jugador1 == "piedra"):
        
        print("--------------------------------------------------------------------------------------------------------------")
        print("El jugador 1 es el ganador")
        
print("--------------------------------------------------------------------------------------------------------------")

print ("Hasta pronto")


























