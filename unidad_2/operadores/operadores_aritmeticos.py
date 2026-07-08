# Operadores ARITMÉTICOS

numero_1 = 45
numero_2 = 12
numero_3 = 0
cadena_1 = 'GG'
cadena_2 = 'GGWP'

# Operador SUMA +
suma = numero_1 + numero_2
print(suma)
print(type(suma))

# Operador RESTA -
print()
resta = numero_1 - numero_2
print(resta)
print(type(resta))

# Operador MULTIPLICACIÓN *
print()
multiplicacion = numero_1 * numero_2
print(multiplicacion)
print(type(multiplicacion))

# Operador DIVISIÓN /
print()
division = numero_1 / numero_2
print(division)
print(type(division))
# Una división con DENOMINADOR 0 NO está definida, no se puede hacer
# siempre hay que revisar que el denominador sea distinto de 0
# print(numero_1 / numero_3)

# Operador SUMA y MULTIPLICACIÓN también se aplican sobre cadenas de texto
print(cadena_1 + cadena_2)
print(cadena_1 + str(numero_1))
print(cadena_1 * numero_2)