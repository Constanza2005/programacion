from datetime import date,datetime
from negocio import crear_nueva_rifa

def solicitar_datos_rifa():
    # fecha_hoy = date.today()
    nombre = input('Ingrese Nombre Rifa: ')
    precio = convertir_texto_numero('Valor Número Rifa: ')
    cantidad_rifas = convertir_texto_numero('Cantidad Rifas: ')
    numeros_rifa = convertir_texto_numero('Cantidad de Número por Rifa: ')
    fecha_lanzamiento = convertir_texto_fecha('Fecha de Lanzamiento en formato dd/mm/aaaa: ')
    # cantidad_premios = convertir_texto_numero('Cantidad de Premios: ')
    # premios = {}
    # for numero in range(1,cantidad_premios + 1):
    #     contenido_premio = input(f'Premio {numero}: ')
    #     nuevo_premio = {f'Premio {numero}':f'{contenido_premio.title()}'}
    #     premios.update(nuevo_premio)
    crear_nueva_rifa(nombre,precio,cantidad_rifas,numeros_rifa,fecha_lanzamiento)

def convertir_texto_numero(mensaje_input):
    numero_entero = 0
    while numero_entero <= 0:
        try:
            numero_entero = int(input(mensaje_input))
            return numero_entero
        except Exception:
            print('Ingrese un número entero')

def convertir_texto_fecha(mensaje_input):
    fecha_lanzamiento = ''
    while not isinstance(fecha_lanzamiento, (date, datetime)):
        try:
            fecha_lanzamiento = input(f'{mensaje_input}')
            # Convertimos el texto ingresado a un objeto fecha
            fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%d/%m/%Y")
            return fecha_lanzamiento
        except ValueError:
            print("Formato de fecha incorrecto. Asegúrate de usar dd/mm/aaaa.")