import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from services.autenticacion import AutenticacionService

# SOLUCIÓN: Le indicamos que los menús están dentro de la carpeta "services"
from services import solicitante
from services import encargado

def menu_principal():
    print("\n" + "="*35)
    print("  SISTEMA DE PRÉSTAMOS DE EQUIPOS")
    print("="*35)
    print("1. Iniciar sesión")
    print("2. Salir")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    correo = input("Ingrese su correo: ")
    password = input("Ingrese su contraseña: ")
    
    usuario, mensaje = AutenticacionService().iniciar_sesion(correo, password)
    
    if usuario:
        print(f"\n¡Bienvenido(a), {usuario.nombre}! Rol: {usuario.rol}")
        return usuario
    else:
        print(f"\n{mensaje}")
        return None

def main():
    usuario_actual = None

    while True:
        if usuario_actual is None:
            menu_principal()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                usuario_actual = iniciar_sesion()
            elif opcion == "2":
                print("Saliendo del sistema. ¡Hasta pronto!")
                sys.exit()
            else:
                print("Opción inválida. Intente nuevamente.")

        else:
            # Derivamos el control al archivo correspondiente según el rol
            if usuario_actual.rol == "SOLICITANTE":
                solicitante.iniciar_menu(usuario_actual)
            elif usuario_actual.rol == "ENCARGADO":
                encargado.iniciar_menu(usuario_actual)
            
            # Si las funciones anteriores terminan (break), el usuario cerró sesión
            usuario_actual = None

if __name__ == "__main__":
    main()