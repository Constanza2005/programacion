from datos import listado_usuarios,guardar_datos
from prettytable import PrettyTable
import bcrypt

def obtener_listado_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['N°','Nombre','Rut','Nacionalidad','Teléfono','Email','Tipo Usuario']

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario['id'],usuario['nombre'], usuario['rut'], usuario['nacionalidad'], usuario['telefono'], usuario['email'],usuario['tipo_usuario']])
    
    return tabla_usuarios

def crear_nuevo_usuario(nombre,rut,nacionalidad,telefono,email,tipo_usuario,contrasena):    
    contrasena = contrasena.encode('utf-8')
    contrasena_encriptada = bcrypt.hashpw(contrasena, bcrypt.gensalt())
    nacionalidad_int = 38
    valores=(nombre,rut,nacionalidad_int,telefono,email,tipo_usuario,contrasena_encriptada)
    consulta = '''
insert into rifa_t.usuarios  (nombre_usuario,rut_usuario,nacionalidad_usuario,telefono_usuario,email_usuario,tipo_usuario,contrasena)
values 
(%s,%s,%s,%s,%s,%s,%s)
'''

    guardar_datos(consulta,valores)

def buscar_usuario_correo(correo):
    for usuario in listado_usuarios:
        if correo == usuario['email']:
            return usuario

def validar_contrasena_login(contrasena,contrasena_encriptada):
    contrasena = contrasena.encode('utf-8')
    if bcrypt.checkpw(contrasena,contrasena_encriptada):
        return True
    else:
        return False
    
def bloquear_usaurio(correo):
    for usuario in listado_usuarios:
        if correo == usuario['email']:
            usuario.update({'habilitado' : False})
            # guardar_usuario(listado_usuarios)