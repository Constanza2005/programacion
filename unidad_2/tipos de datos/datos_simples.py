# Tipos de datos en Python

# Con el símbolo # escribo comentarios que no se ejecutan con el código

variable_texto = 'Buen día queridos estudiantes'
variable_texto_multiple_lineas = '''
esto es un texto
en múltiples líneas
'''
variable_texto_multiple_lineas = """
esto es un texto
en múltiples líneas
"""

variable_entero = 25
variable_decimal = 2.5
variable_booleana = True

# Tipo de dato STRING str
print(variable_texto)

# Tipo de dato INTEGER int
print(variable_entero)

# Tipo de dato FLOATING float
print(variable_decimal)

# Tipo de dato BOOLEAN bool
print(variable_booleana)

print(type(variable_texto))
print(type(variable_entero))
print(type(variable_decimal))
print(type(variable_booleana))

print(dir(variable_texto))
print(variable_texto.title())
print(variable_texto.upper())
print(variable_texto.lower())

print(dir(variable_entero))
print(variable_entero.is_integer())
print(variable_decimal.is_integer())

print(dir(variable_booleana))
print(dir(variable_decimal))