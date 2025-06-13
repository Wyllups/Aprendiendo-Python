# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 07:51:30 2025

@author: AULA
"""


"""Cada camilla de hospital en donde se atienden a pacientes de diferentes dolencias 
cuentan con unos insumos mínimos mandatorios, entre ellos: camilla, algodón, jeringuillas y 
acetaminofén, por nombrar algunos. Cuando algún insumo se encuentre por debajo del  del 
inventario de referencia se debe hacer la recarga de todos los insumos. Desarolla un algoritmo 
que automatice el proceso de conteo para determinar los insumos restantes para cada paciente."""

ref = {
    'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
    'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
    'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
    'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 20}
}



cubiculos = [
  [
    {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 3},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 3}
    },
    {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 5},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 2},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 1}
    },
   {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 16}
    },
  ],
  [
   {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 8},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 7},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 7}
    },
    {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 5},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 6},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 10}
    },
   {
      'Camilla': {'Unidades': 'Un', 'Cantidad': 1},
      'Acetaminofén': {'Unidades': 'cajas', 'Cantidad': 10},
      'Jeringuillas': {'Unidades': 'Un', 'Cantidad': 10},
      'Algodón': {'Unidades': 'paquetes 200 g', 'Cantidad': 6}
    },
  ]
]

cubiculos[0]
cubiculos[1]

cubiculos[1][0]
cubiculos[1][0]["Camilla"]["Cantidad"]


cont_cub = 0
for cubiculo in cubiculos :
    cont_cub += 1
    cont_pac = 0
    print('------------------------------------------------')
    print('CUBICULO', cont_cub)
    print('  ')
    for paciente in cubiculo:
        cont_pac += 1
        print('------------------------------------------------')
        print('Paciente',cont_pac,)
        print(' ')
        print('\nInsumos:')
        print('  ')
        for insumos in paciente:
            print(insumos)
            
        
    
    



































































































