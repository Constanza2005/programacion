# Ingreso de contraseña mediante ciclo FOR

contrasena = 'eureka'
for numero in range(3):
    contrasena_usuario = input('Ingrese contraseña: ')
    if contrasena_usuario == contrasena:
        print('Contraseña Correcta!')
        break
    else:
        if numero < 2:
            print('Contraseña Incorrecta, intente nuevamente.')
        else:
            print('Contraseña Incorrecta, Cerrando Sistema!')