# Métodos para modificación de cadenas de texto

nombre_completo_minusculas = 'erick bailey'
nombre_completo_mayusculas = 'ERICK BAILEY'
rut_str = '12.824.290-2'
camion_codigo = 'cami&oacute;n'
cadena_espacios = '     esta es mi cadena de texto      '

loren_ipsum = '''Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Donec quis ipsum porttitor, 
rutrum tortor quis, 
rhoncus dui. 
Mauris sit amet lectus at nibh fermentum mollis. 
Proin malesuada justo vel sagittis lacinia. 
In auctor vel tortor nec egestas. 
In ac pretium leo. 
Aenean feugiat vulputate augue ac pellentesque. 
Fusce viverra et nulla quis eleifend. 
Suspendisse aliquam venenatis nisl quis efficitur. 
Quisque luctus, 
dolor a aliquet varius, 
ex risus cursus orci, 
in convallis purus nisi vel ante.
'''

# print(dir(nombre_completo))
print(nombre_completo_minusculas)
# El método CAPITALIZE deja en mayúscula la primera letra del texto
print(nombre_completo_minusculas.capitalize())
# print(loren_ipsum.capitalize())

# El método LOWER deja todos los caracteres en minúsculas
print(nombre_completo_mayusculas.lower())

# El método UPPER deja todos los caracteres en mayúsculas
print(nombre_completo_minusculas.upper())

# El método TITLE transforma la cadena en título, la primera letra de cada palabra en mayúsculas
print(nombre_completo_minusculas.title())
# print(loren_ipsum.title())

# El método LEN (length, largo = tamaño) permite conocer la cantidad de caracteres de un string
print(len(nombre_completo_minusculas))
print(len(loren_ipsum))

# El método SPLIT permite cortar una cadena de caracteres en el caracter indicado
# Si no se entrega ningún argumento al método split, se dividirá la cadena en los espacios
nombre_split = nombre_completo_minusculas.split()
print(nombre_split)

# Si se entrega un argumento al método split, se dividirá la cadena en el caracter indicado
nombre_split = nombre_completo_minusculas.split('i')
print(nombre_split)

rut_split = rut_str.split('-')
print(rut_split)

# El método REPLACE modifica una parte de la cadena de texto especificada por otra definida
# REPLACE recibe 2 argumentos, el primero es el texto a buscar y el segundo el texto que lo reemplazará
nombre_modificado = nombre_completo_mayusculas.replace('RICK','gg')
print(nombre_modificado)

nombre_modificado_minusculas = nombre_completo_minusculas.replace('erick','Torch')
print(nombre_modificado_minusculas)

modificar_texto_tilde = camion_codigo.replace('&oacute;','ó')
print(modificar_texto_tilde)

# El método STRIP (TRIMM en la mayoría de los lenguajes) 
# elimina espacios en blanco al principio y al final de una cadena de texto
print(cadena_espacios)
print(len(cadena_espacios))
cadena_modificada = cadena_espacios.strip()
print(cadena_modificada)
print(len(cadena_modificada))