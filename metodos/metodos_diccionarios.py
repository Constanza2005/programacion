datos_personales = {
    'nombre':'cony',
    'edad':20,
    'titulo':'estudiante'
}

# El método LEN (length, largo = tamaño) permite conocer la cantidad de elementos en una lista
print(len(datos_personales))

print()
# El método KEYS permite obtener las CLAVES de los diccionarios
claves = datos_personales.keys()
print(claves)

print()
# El método VALUES permite obtener los VALORES de los diccionarios
claves = datos_personales.values()
print(claves)

print()
# El método GET permite obtener el VALOR de un elemento mediante su CLAVE
nombre_personal = datos_personales.get('nombre')
print(nombre_personal.title())

print()
# Para agregar un nuevo elemento a un diccionario
# debemos definir su clave y su valor
datos_personales['Es profesor?']=False
print(datos_personales)

print()
# El método POP elimina un elemento por su CLAVE
datos_personales.pop('Es profesor?')
print(datos_personales)

print()
# El método CLEAR elimina todos los elementos del diccionario
datos_personales.clear()
print(datos_personales)

