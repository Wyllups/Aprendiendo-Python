# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

variable1 = 0
variable2 = 1
variable3 = 2
contador1 = 0

while( contador1 > 0):
    cantidad = int(input("Escribne una cantidad para los numeros:__"))
    contador =+ 1 
    numero = contador + numero
    print (numero)
    
    if(contador == cantidad):
        break
    
#%%

cont = 2 
a = 0
b = 1 

usuario = int(input("Escribe la cantidad de digitos que desees: "))

print (a,b, end = " ",)

while(cont < usuario):
    c = a + b
    a = b 
    b = c
    cont = cont + 1
    print (c,end = " ")
    
    if(usuario == -1):
        break
    
print(" Hasta pronto ")
    

#%%

cond = 0

while (cond !=  -1):
    cont = 2
    if (contador==2):
        usuario = int(input("Escribe la cantidad de digitos que desees:__ "))
    else:
    
    a = 0
    b = 1 
    print (a,b, end = " ",)
    while(cont < usuario):
        c = a + b
        a = b 
        b = c
        cont = cont + 1
        print (c,end = " ")
        print ("-------------------------------------------------------------")
        cond = int(input("Desea otra cantidad? sino orprime -1 :__ "))
        
print(" Hasta pronto ")





























