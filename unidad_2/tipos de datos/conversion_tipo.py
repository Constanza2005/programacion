nombre_personal = input('Ingrese su nombre: ')
saludo = 'Buen día '
print(type(nombre_personal))
print(nombre_personal)

# CONCATENACIÓN de cadenas de texto
print(saludo + nombre_personal)

str_numero_entero = input('Ingrese un número entero: ')
numero_entero = int(str_numero_entero)
numero_decimal = float(str_numero_entero)
print(type(numero_entero))
print(type(numero_decimal))
print(numero_entero)
print(numero_decimal)

numero_uno = 25
numero_dos = 50

# La operacion + con 2 números, opera aritméticamente sumándolos y entregando el resultado
print(numero_uno + numero_dos)
# La operacion + con 2 cadenas de texto, opera semánticamente concatenándolos y entregando el string resultante
print(saludo + str_numero_entero)
# La operación + con 2 tipos de datos distintos arroja ERROR
# print(str_numero_entero + numero_dos)

# Solicite al usuario que ingrese su nombre y edad y muéstrelos por pantalla con un saludo.

# Un string NO vacío siempre retorna True al convertirlo a booleano, porque TIENE contenido.
# Si el string estuviera vacío, en ese caso sería False.
# str_booleano = 'false'
int_booleano = 1

# print(type(str_booleano))
print(type(int_booleano))

# booleano = bool(str_booleano)
otro_booleano = bool(int_booleano)

# print(booleano)
# print(type(booleano))
print(type(otro_booleano))

# Validando el tipo de datos
numero = 1
if isinstance(numero,str):
    print('ES UN TEXTO!!')
elif isinstance(numero,bool):
    print('ES UN BOOLEANO!!')
elif isinstance(numero,int):
    print('ES UN ENTERO!!')
elif isinstance(numero,float):
    print('ES UN DECIMAL!!')
else:
    print('NO TENGO IDEA DE LO QUE ES!!')