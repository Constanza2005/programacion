from negocio import crear_nuevo_usuario,buscar_usuario_correo
from datos import opcion_invalida,correo_invalido,telefono_invalido,contrasena_invalida,correo_usado
import re
import pwinput

def solicitar_datos_usuario():
    nombre = ingresar_datos('Nombre Usuario: ')
    rut = ingresar_datos('Rut Usuario (12.345.678-5): ')
    nacionalidad = ingresar_datos('Nacionalidad Usuario: ')
    telefono = validar_telefono()
    email = ''
    while email == '':
        email = validar_email()
        correo_encontrado = buscar_correo_usado(email)
        if correo_encontrado:
            email = ''

    print('Seleccione el tipo de usuario: ')
    print('[1] Administrador')
    print('[2] Observador')
    tipo_usuario = ''
    while tipo_usuario == '':
        opcion_tipo_usuario = input('Seleccione el tipo de usuario [1-2]: ')
        if opcion_tipo_usuario in ['1','2']:
            if opcion_tipo_usuario == '1':
                tipo_usuario = 1
            else:
                tipo_usuario = 2
        else:
            print(opcion_invalida)
    contrasena = ''
    while contrasena == '':
        contrasena = pwinput.pwinput(prompt='Contraseña: ',mask='*')
        if contrasena_segura(contrasena)==False:
            contrasena = ''

    crear_nuevo_usuario(nombre,rut,nacionalidad,telefono,email,tipo_usuario,contrasena)

def ingresar_correo_login():
    email = validar_email()
    return email

def ingresar_contrasena_login():
    contrasena=''
    while contrasena == '':
        contrasena = pwinput.pwinput(prompt='Contraseña: ',mask='*')
        return contrasena

def contrasena_segura(contrasena):
    patron_contrasena = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(patron_contrasena, contrasena):
        return True
    else:
        print(contrasena_invalida)
        return False

def validar_email():
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$'
    email = ''
        
    while email == '':
        email = input('Email Usuario (nombreusuario@servidor.dom): ')
        if re.fullmatch(patron_email, email):
            return email
        else:
            print(correo_invalido)
            email = ''

def buscar_correo_usado(correo):
    usuario = buscar_usuario_correo(correo)
    if usuario:
        print(correo_usado)
        return True
    else:
        return False

def validar_telefono():
    patron_telefono = r'^[0-9]{9,9}$'
    telefono = ''
        
    while telefono == '':
        telefono = input('Teléfono Usuario (999999999):  ')
        if re.fullmatch(patron_telefono, telefono):
            return telefono
        else:
            print(telefono_invalido)
            telefono = ''

def ingresar_datos(mensaje):
    dato=''
    while dato == '':
        dato = input(mensaje)
        return dato