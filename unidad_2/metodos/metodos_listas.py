lista_animales = ['perro','gato','delfín','pantera']
lista_compras = ['cepillo','pasta de dientes','jabón']
lista_numeros = [5,45,1,98,2563,-25]

print(type(lista_animales))

# El método LEN (length, largo = tamaño) permite conocer la cantidad de elementos de una lista
print(len(lista_animales))

print()
# El método APPEND agrega un nuevo elemento al final de la lista
nuevo_animal = input('Agregue un nuevo animal a la lista: ')
lista_animales.append(nuevo_animal)
print(len(lista_animales))
print(lista_animales)

print()
# El método INSERT permite agregar un elemento en un lugar (índice) especifico
otro_animal = input('Agregue un nuevo animal a la lista: ')
lista_animales.insert(2,otro_animal)
print(len(lista_animales))
print(lista_animales)

print()
# El método EXTEND permite agregar varios elementos a una lista
# Agregamos una lista ya creada, uniendo ambas listas
lista_animales.extend(lista_compras)
print(len(lista_animales))
print(lista_animales)

# Agregamos una lista creada manualmente
lista_animales.extend(['oso pardo','panda','oso polar'])
print(len(lista_animales))
print(lista_animales)

print()
# El método POP permite elimnar elementos de una lista
# Si al método POP no se le entregan elementos, elimina el último elemento de la lista
lista_animales.pop()
print(len(lista_animales))
print(lista_animales)

# Si al método POP le indico el argumento ÍNDICE, elimina el elemento especificado
lista_animales.pop(0)
print(len(lista_animales))
print(lista_animales)

# Si al método POP le indico el argumento ÍNDICE -1, elimina el último elemento de la lista
lista_animales.pop(-1)
print(len(lista_animales))
print(lista_animales)

print()
# El método REMOVE elimina un elemento por su VALOR
lista_animales.remove('oso pardo')
print(len(lista_animales))
print(lista_animales)

print()
# El método CLEAR elimina TODOS los elementos de la lista
lista_animales.clear()
print(len(lista_animales))
print(lista_animales)

print()
# El método SORT ordena una lista de cadenas de texto alfabéticamente
lista_compras.sort()
print(len(lista_compras))
print(lista_compras)

# El método REVERSE ordena la lista al revés
lista_compras.reverse()
print(lista_compras)

print()
# El método SORT ordena una lista de números de manera ascendente
lista_numeros.sort()
print(len(lista_numeros))
print(lista_numeros)

# El método REVERSE ordena la lista de números de manera descendente
lista_numeros.reverse()
print(lista_numeros)

# El método SUM permite sumar los elementos de una lista de números
print(f'suma de {lista_numeros} = {sum(lista_numeros)}')