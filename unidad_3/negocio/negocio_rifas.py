from datos import listado_rifas,guardar_datos
from prettytable import PrettyTable
from datetime import date

def obtener_listado_rifas():
    tabla_rifas = PrettyTable()
    tabla_rifas.field_names = ['Nombre','Fecha Creación','Precio Número','Cantidad Rifas','Fecha Lanzamiento']

    for rifa in listado_rifas:
        tabla_rifas.add_row([rifa['nombre'], rifa['fecha_creacion'], f'${rifa['precio']}', rifa['cantidad_rifas'], rifa['fecha_lanzamiento']])
    
    return tabla_rifas

def crear_nueva_rifa(nombre,precio,cantidad_rifas,numeros_rifa,fecha_lanzamiento):
    valores = (nombre,cantidad_rifas,numeros_rifa,precio,fecha_lanzamiento)
    consulta = f'''
insert into rifa_t.rifas (nombre_rifa ,cantidad_rifas ,numeros_rifa ,precio ,fecha_creacion,fecha_lanzamiento)
values
(%s,%s,%s,%s,CURDATE(),%s)
'''
    guardar_datos(consulta,valores)