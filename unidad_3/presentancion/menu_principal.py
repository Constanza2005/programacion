from datos import numero_version,titulo_app,menu_aplicacion,sub_menu,opcion_invalida
from negocio import obtener_listado_usuarios,obtener_listado_rifas,buscar_usuario_correo,validar_contrasena_login,bloquear_usaurio
from presentacion import solicitar_datos_rifa,solicitar_datos_usuario,ingresar_correo_login,ingresar_contrasena_login
import sys

def login():
    print(f'\n{titulo_app} v{numero_version}')
    print(f'{'=' * len(titulo_app)}=={'=' * len(numero_version)}')
    while True:
        titulo_menu('Login')
        correo = ingresar_correo_login()
        usuario = buscar_usuario_correo(correo)
        if usuario:
            if usuario['habilitado'] == True:
                contador = 0
                while contador < 3:
                    contrasena = ingresar_contrasena_login()
                    usuario_valido = validar_contrasena_login(contrasena,usuario['contrasena'])
                    if usuario_valido:
                        print('Usuario Válido! Puede ingresar a la app!')
                        menu_principal()
                    else:
                        contador+=1
                        print('Contraseña NO corresponde!')
                else:
                    bloquear_usaurio(usuario['email'])
                    print('Superó la cantidad de intentos.')
            else:
               print('Usuario Bloqueado... Comuníquese con el administrador de sistema.') 
        else:
            print('Usuario NO encontrado... Intente nuevamente.')

def menu_principal():
    print(f'\n{titulo_app} v{numero_version}')
    print(f'{'=' * len(titulo_app)}=={'=' * len(numero_version)}')
    
    while True:
        titulo_menu('Menú Principal')
        for clave,valor in menu_aplicacion.items():
            print(f'[{clave}] - {valor}')
        opcion = seleccionar_opcion(menu_aplicacion)

        if opcion == '1':
            while True:
                titulo_menu('SubMenú Rifas')
                for clave,valor in sub_menu.items():
                    if clave != '0':
                        print(f'[{clave}] - {valor + ' Rifas'}')
                    else:
                        print(f'[{clave}] - {valor}')
                opcion_sub_menu = seleccionar_opcion(sub_menu)

                if opcion_sub_menu == '0':
                    print('Volviendo al menú anterior...')
                    break
                elif opcion_sub_menu == '1':
                    solicitar_datos_rifa()
                elif opcion_sub_menu == '2':
                    tabla_rifas = obtener_listado_rifas()
                    print(tabla_rifas)
                else:
                    print(opcion_invalida)
        elif opcion == '2':
            while True:
                titulo_menu('SubMenú Usuarios')
                for clave,valor in sub_menu.items():
                    if clave != '0':
                        print(f'[{clave}] - {valor + ' Usuarios'}')
                    else:
                        print(f'[{clave}] - {valor}')
                
                opcion_sub_menu = seleccionar_opcion(sub_menu)

                if opcion_sub_menu == '0':
                    print('Volviendo al menú anterior...')
                    break
                elif opcion_sub_menu == '1':
                    solicitar_datos_usuario()
                elif opcion_sub_menu == '2':
                    tabla_usuarios = obtener_listado_usuarios()
                    print(tabla_usuarios)
                else:
                    print(opcion_invalida)
        elif opcion == '3':
            print('Cerrando Sesión.')
            break
        elif opcion == '0':
            print(f'Gracias por usar {titulo_app}.\n¡Hasta Luego!')
            sys.exit()
        else:
            print(opcion_invalida)

def titulo_menu(menu):
    print()
    print(menu)
    print(f'{'=' * len(menu)}')

def seleccionar_opcion(menu):
    opcion = input(f'\nSeleccione su Opción [0-{len(menu) - 1}]: ')
    return opcion