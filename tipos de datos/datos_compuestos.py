# Colecciones de DATOS

# LISTAS => list
# Es una colección ORDENADA y MUTABLE de datos de cualquier tipo

print('Listas en Python')
mi_primera_lista = ['Constanza Alarcon ',20,True]

nombre_personal = input('Ingrese su nombre: ')

print(type(mi_primera_lista))
print(mi_primera_lista)
print(f'El primer elemento de la lista es: {mi_primera_lista[0]}')
print(f'El segundo elemento de la lista es: {mi_primera_lista[1]}')
print(f'El tercer elemento de la lista es: {mi_primera_lista[2]}')

mi_primera_lista[0] = nombre_personal
print(mi_primera_lista)

print(dir(mi_primera_lista))

# DICCIONARIOS dictionary => dict
# Es una colección ORDENADA y MUTABLE de pares de datos de cualquier tipo
# los datos de un diccionario ocupan el doble de espacio en memoria
# deben almacenar la CLAVE y el VALOR de cada dato

mi_primer_diccionario = {'nombre':'Constanza Alarcon','edad':20,'asistio a clase hoy?':True}
print(type(mi_primer_diccionario))
print(mi_primer_diccionario)

print(mi_primer_diccionario["nombre"])
mi_primer_diccionario['nombre'] = nombre_personal
print( mi_primer_diccionario)

print(dir(mi_primer_diccionario))




