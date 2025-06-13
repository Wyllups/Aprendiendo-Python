# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:25:02 2025

@author: AULA
"""
#%%
for i in (1,2,3,4,5):
    print (i)
    
#%%    
    
for a in range (6):
    print (a)   
    
#%%

for b in range (5,20):
    print (b)
    
#%%

for c in range (5,19,2):
    print (c) 
    
 #%% 

for d in range (5,0,-1):
    print (d)  
    
#%%

frutas = ['Manzana','Pera','Mango','Fresa','Coco']
for fruta in frutas:
    print (fruta,end=' ')
    
#%%

estudiantes = {
    'Mexico': 10,
    'Colombia': 15,
    'Puesto rico': 4
}   
    
print (estudiantes) 

for pais in estudiantes:
    print(pais)

for pais in estudiantes:
    print(estudiantes[pais])
    
for pais in estudiantes.keys():
    print(pais)

for pais in estudiantes.values():
    print (pais)

for j, k in estudiantes.items():
    print('En el pais',j,'hay',k,'estudiantes')
    
#%%

num = (1,2,3,4)
sumatoria = 0

for j in num:
    print(j, sumatoria)
    sumatoria + j
print('------------------------------------------')
print(f'El total de la sumatoria es: {sumatoria}')

#%%

sumatoria = 0

for k in range(1,11):
    print (k, sumatoria)
    sumatoria += k
print('-----------------------------------------------------')
print(f'El total de la sumatoria es: {sumatoria}')

#%%
    
num2 = [8,7,3,4,0,9,1,2]  

for n in range(len(num2)):
    print('Posicion:',n)
    
for n in range(len(num2)):
    print (f"Posicion:{n}-elemento: {num2[n]}")
        
#%%

estudiante = 'Wilfredo Calderon Perez'

for letra in estudiante:
    if (letra=='o' or letra=='o' or letra=='o'):
        s+=1
        
print('En su nombre hay',s,"letras o")

#%%

num = int(input('Ingrese el numero al que desea sacar su factorial:_'))

if num < 0:
    print('El factorial no esta definido para numeros negativos')
else:
    factorial = 1
    for i in range (1, num + 1 ):
        factorial *= i
print(f'El factorial de {num} es {factorial}')

#%%
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    