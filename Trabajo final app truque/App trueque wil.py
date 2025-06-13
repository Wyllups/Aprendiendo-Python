# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 23:17:50 2025

@author: Wilfredo
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 23:08:56 2025
@author: Wilfredo
"""

articulos = []
truecoins = 0
usuario_activo = ""
carrito = []
articulos_en_venta = []

def validar_correo(correo):
    return "@" in correo and "." in correo.split("@")[-1]

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Subir artículo")
    print("2. Proponer trueque")
    print("3. Ver carrito")
    print("4. Comprar artículos a la app por 7 Truecoins")
    print("5. Vender artículo a la app (ganas 5 Truecoins)")
    print("6. Ver cuántos Truecoins tienes")
    print("7. Cerrar sesión")

def subir_articulo():
    articulo = input("Escribe el nombre del artículo que deseas subir: ")
    articulos.append(articulo)
    print(f"Artículo '{articulo}' subido correctamente.")
    
def proponer_trueque():
    print("\n--- ARTÍCULOS DISPONIBLES PARA TRUEQUE ---")
    if not articulos:
        print("No hay artículos disponibles todavía. Sube uno primero.")
        return
    
    for i, item in enumerate(articulos, 1):
        print(f"{i}. {item}")
    
    articulo = input("¿Qué artículo deseas ofrecer para el trueque?: ")
    recibir = input("¿Qué artículo deseas recibir a cambio?: ")

    if recibir in articulos:
        articulos.remove(recibir)
        print(f"Trueque propuesto: cambiar '{articulo}' por '{recibir}'.")
        print(f"El artículo '{recibir}' ya no está disponible porque ha sido reservado para el trueque.")
    else:
        print("El artículo que deseas recibir no está disponible.")

def ver_carrito():
    print("\n--- TU CARRITO ---")
    if not carrito:
        print("Tu carrito está vacío.")
    else:
        for i, item in enumerate(carrito, 1):
            print(f"{i}. {item}")

def comprar_articulo_app():
    global truecoins
    print("\n--- ARTÍCULOS EN VENTA POR LA APP (7 Truecoins c/u) ---")
    if not articulos_en_venta:
        print("No hay artículos disponibles en la tienda aún.")
        return

    if truecoins < 7:
        print(f"No tienes suficientes Truecoins para comprar. Tienes {truecoins}, necesitas al menos 7.")
        return

    for i, item in enumerate(articulos_en_venta, 1):
        print(f"{i}. {item}")
    
    eleccion = input("Escribe el nombre del artículo que deseas comprar: ")
    if eleccion in articulos_en_venta:
        truecoins -= 7
        articulos_en_venta.remove(eleccion)
        print(f"Has comprado '{eleccion}' por 7 Truecoins.")
    else:
        print("El artículo no está disponible o escribiste mal el nombre.")

def vender_a_la_app():
    global truecoins
    articulo = input("Escribe el artículo que deseas vender a la app: ")
    truecoins += 5
    articulos_en_venta.append(articulo)
    if articulo in articulos:
        articulos.remove(articulo)
    print(f"Has vendido '{articulo}' a la app y ganado 5 Truecoins.")

def ver_truecoins():
    print(f"Tienes {truecoins} Truecoins.")

def iniciar_sesion():
    global usuario_activo
    while True:
        correo = input("Ingresa tu correo electrónico para iniciar sesión: ")
        if validar_correo(correo):
            usuario_activo = correo
            print(f"Bienvenido, {correo}")
            break
        else:
            print("Correo no válido. Intenta de nuevo.")

iniciar_sesion()

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-7): ")

    match opcion:
        case "1":
            subir_articulo()
        case "2":
            proponer_trueque()
        case "3":
            ver_carrito()
        case "4":
            comprar_articulo_app()
        case "5":
            vender_a_la_app()
        case "6":
            ver_truecoins()
        case "7":
            print("Cerrando sesión. Hasta pronto.")
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
