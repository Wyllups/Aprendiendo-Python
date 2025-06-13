# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
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


# Calcular los totales actuales de insumos en todos los cubículos
totales = {}
for fila in cubiculos:
    for cubiculo in fila:
        for insumo, datos in cubiculo.items():
            if insumo not in totales:
                totales[insumo] = {
                    'Unidades': datos['Unidades'],
                    'Cantidad': 0
                }
            totales[insumo]['Cantidad'] += datos['Cantidad']

# Determinar qué insumos requieren recarga
recarga = {}
for insumo, datos_ref in ref.items():
    cantidad_actual = totales.get(insumo, {'Cantidad': 0})['Cantidad']
    if cantidad_actual < datos_ref['Cantidad']:
        recarga[insumo] = {
            'Unidades': datos_ref['Unidades'],
            'Cantidad Necesaria': datos_ref['Cantidad'] - cantidad_actual
        }

# Salida de resultados
print("Totales Actualizados:")
for insumo, datos in totales.items():
    print(f"{insumo}: {datos['Cantidad']} {datos['Unidades']}")

print("\nInsumos por Recargar:")
for insumo, datos in recarga.items():
    print(f"{insumo}: Necesita {datos['Cantidad Necesaria']} {datos['Unidades']}")

































