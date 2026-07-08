# Ciclo WHILE es usado para ejecutar un set de tareas una cantidad determinada de veces

contador = 0
while contador < 10:
    print(contador)
    contador = contador + 1

print('Ciclo While mientras contador < 10')

contrasena = 'eureka'
intento = 3
while intento < 3:
    contrasena_usuario = input('Ingrese contraseña: ')
    if contrasena_usuario == contrasena:
        print('Contraseña Correcta!')
    else:
        intento += 1
        if intento < 3:
            print('Contraseña Incorrecta, intente nuevamente.')
        else:
            print('Contraseña Incorrecta, Cerrando Sistema!')

    