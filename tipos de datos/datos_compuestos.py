# Colecciones de DATOS



# LISTAS => list
# Es una colección ORDENADA y MUTABLE de datos de cualquier tipo

print('\nLISTAS')
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

print('\nDICCIONARIO')

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


# CONJUNTOS set
# Es una coleccion DESORDENADA e INMUTABLE de datos de cualquier tipo

print('\nCONJUNTOS')

mi_primer_conjunto = {'dato 1' , 45 , False}
print(type(mi_primer_conjunto))
print(mi_primer_conjunto)
mi_primer_conjunto.add(25)
print(mi_primer_conjunto)

# TUPLAS tuple
# Es una coleccion de datos ORDENADA e INMUTABLE de datos de cualquier tipo

print('\nTUPLAS')

mi_primera_tupla = ('Constanza Alarcon', 20, True)
print(type(mi_primera_tupla))
print(mi_primera_tupla)
print(mi_primera_tupla[0])

# La tupla NO permite asignar un nuevo valor para los elementos, la siguiente asignacion es invalida
# mi_primera_tupla[0] = nombre_personal

