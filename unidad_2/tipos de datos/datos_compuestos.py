# Colecciones de DATOS

# LISTAS => list
# Es una colección ORDENADA y MUTABLE de datos de cualquier tipo

print('\nLISTAS')
mi_primera_lista = ['Erick Bailey ',50,True]

print(type(mi_primera_lista))
print(mi_primera_lista)
print(f'El primer elemento de la lista es: {mi_primera_lista[0]}')

nombre_personal = input('Ingrese su nombre: ')
mi_primera_lista[0] = nombre_personal
print(mi_primera_lista)

# print(dir(mi_primera_lista))
mi_primera_lista.append(25)
print(mi_primera_lista)
mi_primera_lista.remove(25)
print(mi_primera_lista)

# DICCIONARIOS dictionary => dict (dictionary)
# Es una colección ORDENADA y MUTABLE de pares de datos de cualquier tipo
# los datos de un diccionario ocupan el doble de espacio en memoria
# deben almacenar la CLAVE y el VALOR de cada dato

print('\nDICCIONARIOS')
mi_primer_diccionario = {'nombre':'Erick Bailey','edad':50,'asistio a clase hoy?':True}
print(type(mi_primer_diccionario))
print(mi_primer_diccionario)

print(mi_primer_diccionario["nombre"])
mi_primer_diccionario['nombre'] = nombre_personal
print( mi_primer_diccionario)
mi_primer_diccionario['Esta feliz?']=True
print(mi_primer_diccionario)
# print(dir(mi_primer_diccionario))
# mi_primer_diccionario_modificado = mi_primer_diccionario.clear()
# print(mi_primer_diccionario_modificado)

# CONJUNTOS set
# Es una colección DESORDENADA e INMUTABLE de datos de cualquier tipo

print('\nCONJUNTOS')
mi_primer_conjunto = {'dato 1',45,False}
print(type(mi_primer_conjunto))
print(mi_primer_conjunto)
mi_primer_conjunto.add(25)
print(mi_primer_conjunto)

# TUPLAS tuple
# Es una colección ORDENADA e INMUTABLE de datos de cualquier tipo

print('\nTUPLAS')
mi_primera_tupla = ('Erick Bailey ',50,True)
print(type(mi_primera_tupla))
print(mi_primera_tupla[0])

# La tupla NO permite asignar un nuevo valor para los elementos, la siguiente asignación es inválida
# mi_primera_tupla[0] = nombre_personal

# Podemos incluir colecciones de elementos dentro de colecciones de elementos
nueva_lista = [mi_primer_diccionario,mi_primer_conjunto,mi_primera_tupla,mi_primera_lista]
print(nueva_lista)