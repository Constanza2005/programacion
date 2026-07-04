# Metodo para modificacion de cadenas de texto
# Programa que ya existe para cambiar...

nombre_completo_minusculas = 'constanza alarcon'
nombre_completo_mayusculas = 'CONSTANZA ALARCON'
rut_str = '21.975.012-9'
camion_codigo = 'cami&oacute;n'
cadena_espacios = '           vale       '

loren_ipsum = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum.
'''

# Print(dir(nombre_completo))
print(nombre_completo_minusculas)

# El metodo CAPITALIZE deja en mayusculas la primera linea del texto
print(nombre_completo_minusculas.capitalize())
# print(loren_ipsum.capitalize())

# El metodo LOWER deja todos los caracteres en minusculas
print(nombre_completo_mayusculas.lower())

# El metodo UPPER deja todos caracteres en mayusculas
print(nombre_completo_minusculas.upper())

# El metodo TITLE transforms la cadena en titulo, la primera letra de cada palabra en mayusculas
print(nombre_completo_minusculas.title())
# print(loren_ipsum.title())

# El metodo LEN (length, largo = tamaño) permite conocer la cantidad de caracteres em un string
print(len(nombre_completo_minusculas))
print(len(loren_ipsum))

# El metodo SPLIT permite cortar una cadena de caracteres en el caracter indicado
# Si no se entrega ningun argumento al metodo split, se dividira la caddena en los espacios
nombre_split = nombre_completo_minusculas.split()
print(nombre_split)

# Si se entrega un argumento al metodo split, se dividira la cadena en el caracter indicado
nombre_split = nombre_completo_minusculas.split('o')
print(nombre_split)

rut_split = rut_str.split('-')
print(rut_split)

# EL metodo REPLACE modifica una parte de la cadena de texto especificada por otra definida
# REPLACE recibe 2 argumentos, el primero es el texto a buscar y el segundo el texto que lo reemplazará
nombre_modificado = nombre_completo_mayusculas.replace('LARCON','ka')
print(nombre_modificado)

nombre_modificado_minusculas = nombre_completo_minusculas.replace('constanza','nonii')
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

