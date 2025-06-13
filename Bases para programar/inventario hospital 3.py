# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:27:53 2025

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

for cubiculo in range(len(cubiculos)):
    print('cubiculo',cubiculo+1)
    print("------------------")
    for paciente in range (len(cubiculos[cubiculo])):
        print('Paciente: ', paciente+1 )
        for insumos in cubiculos [cubiculo][paciente]:
            print('Insumo -', cubiculos[cubiculo][paciente][insumo]['Cantidad'])
            
            
            
            
            