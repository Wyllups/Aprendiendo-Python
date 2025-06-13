# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:07:16 2025

@author: AULA
"""

ovejas = 0

dormido = input("me dormi: s/n --").lower()

while (dormido == "n"):
    ovejas = ovejas + 1 
    print(f"ovejita:..... {ovejas}")
    respuesta = input("me dormi: s/n --").lower()
    
ovejas = 0 
print(f"ovejas = {ovejas} \nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

#%%


suma = 0


while True:
    suma += 1
    print("ciclo del numero")
    
#%%

g = 0

a = input("Ingrese una letra: --").lower()

while (a != "h"):
    g = g + 1
    print(f"intentos:......{g}")
    a = input("Ingrese una letra: --").lower()
g = 0

print(f"adivino la letra")
    
#%%

g = 0

a = input("Ingrese una letra: --").lower()

while (a != "h"):
    g = g + 1
    print(f"Estas en el intento {g}")
    a = input("Ingrese una letra: --").lower()


print(f"adivino la letra al intento {g}")

g = 0

#%%
h = 0
g = 4

a = input("Ingrese una letra: --").lower().strip()

while (a != "h" and 1 < g <= 4 ):
    g = g - 1
    h = h + 1
    print(f"Tienes {g} Intentos")
    a = input("Ingrese otra letra: --").lower().strip()

if(a == "h" and 1 < g <= 4 ):
    h = h + 1
    print(f"adivinaste al intento {h} ")
else:
    print("no adivinaste la letra ")
    
g = 4

#%%



    
a = int(input("Ingrese numero de notas: --"))
b = 0
c = 0
while (a > 0):
    a = a - 1
    b = b + 1
    b = float(input(f'ingrese su nota {a} :__'))
    c = c + b
    
    






















































