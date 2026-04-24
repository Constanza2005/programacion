# Ciclo FOR para recorrer colecciones de elementos 

lista_juegos = ['dota 2', 'CS2', 'Plantas VS Zombies', 'Expedition 33']
lista_numeros = [1, 5, 25, 30, 35]

for elemento in lista_juegos:
    elemento = elemento.upper()
    print(elemento)

print(f'\nRecorriendo la lista de números = {lista_numeros}')
for numero in lista_numeros:
    resultado = numero * numero
    print(f'{numero} X {numero} = {resultado}')


conjunto_animales = {'perro','gato','ornitorrinco','murciegalo'}
print()
for animal in conjunto_animales:
    print(animal)


tupla_datos_personales = ('Wendy Sulca', 25, 'peruana', 'cantante')
print()
for dato in tupla_datos_personales:
    print(dato)

diccionario_asignatura = {
    'codigo':'TI3011',
    'nombre':'Introduccion a la programacion segura',
    'seccion':'IEI-N1-C2',
    'alumnos': 20
}
print()
for elemento in diccionario_asignatura:
    print(elemento)
print()
for elemento in diccionario_asignatura.items():
    clave = elemento [0]
    valor = elemento [1]
    print(f'Clave: {clave} - Valor: {valor}')
print()
for elemento in diccionario_asignatura.items():
    print(elemento[1])