# Metodo para modificacion de cadenas de texto

nombre_completo_minusculas = 'constanza alarcon'
nombre_completo_mayusculas = 'CONSTANZA ALARCON'
rut_vale = 21

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

rut_split = 