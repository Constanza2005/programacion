# Ingreso de cintraseña mediante el siclo FOR

contrasena = 'eureka'
for numero in range (3):
    contrasena_usuario = input('ingrese contraseña: ')
    if contrasena_usuario == contrasena:
        print('Contraseña correcta!')
        break
    else:
        if numero < 2:
            print('Contraseña incorrecta, intente nuevamente.')
        else:
            print('Contraseña incorrecta cerrando el sistema!')
   