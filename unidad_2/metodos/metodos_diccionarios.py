# MÉTODOS para trabajar con DICCIONARIOS

datos_personales = {
    'nombre':'erick bailey',
    'edad':50,
    'titulo':'Analista Programador'
}

# El método LEN (length, largo = tamaño) permite conocer la cantidad de elementos de un diccionario
print(len(datos_personales))

print()
# El método ITEMS permite obtener cada uno de los pares de elementos
print(datos_personales.items())

print()
# El método KEYS permite obtener las CLAVES de un diccionario
claves = datos_personales.keys()
print(claves)

print()
# El método VALUES permite obtener las VALORES de un diccionario
valores = datos_personales.values()
print(valores)

print()
# El método GET permite obtener el VALOR de un elemento mediante su CLAVE
nombre_personal = datos_personales.get('nombre')
print(nombre_personal.title())

print()
# Para agregar un nuevo elemento a un diccionario
# debemos definir su clave y su valor
datos_personales['Es profesor?'] = True
print(datos_personales)

print()
# El método POP elimina un elemento por su CLAVE
datos_personales.pop('Es profesor?')
print(datos_personales)

print()
# El método CLEAR elimina TODOS los elementos del diccionario
datos_personales.clear()
print(datos_personales)
