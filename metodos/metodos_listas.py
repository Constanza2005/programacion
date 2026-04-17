lista_animales = ['perro','gato','delfin','pantera']
lista_compras = ['cepillo','pasta de dientes','jabon']
lista_numeros = ['5','25','64','-3']

print(type(lista_animales))

# El método LEN (length, largo = tamaño) permite conocer la cantidad de elementos en una lista
print(len(lista_animales))

print()
# El método APPPEND agrega un nuevo elemento al final de la lista
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
lista_animales.extend(['oso pardo','oso polar','panda'])
print(len(lista_animales))
print(lista_animales)

print()
# El método POP permite eliminar elementos de una lista 
# Si al metodo POP no se le entregan elementos, elimina el ultimo elemento de la lista
lista_animales.pop()
print(len(lista_animales))
print(lista_animales)

# Si al método POP le indico el argumento ÍNDICE, elimina el elemento especificado
lista_animales.pop(0)
print(len(lista_animales))
print(lista_animales)

# Si al método POP le indico el argumento ÍNDICE -1, elimina el elemento especificado
lista_animales.pop(-1)
print(len(lista_animales))
print(lista_animales)

print()
# El método REMOVE elimina un elemento por su VALOR
lista_animales.remove('oso pardo')
print(len(lista_animales))
print(lista_animales)

print()
# El método CLEAR elimina todos los elementos de la lista
lista_animales.clear()
print(len(lista_animales))
print(lista_animales)

print()
# El método SORT ordena una lista
lista_compras.sort()
print(len(lista_compras))
print(lista_compras)

# El metodo REVERSE ordena la lista al revés
lista_compras.reverse()
print(lista_compras)

print()
# El método SORT ordena una lista de numeros de manera ascendente
lista_numeros.sort()
print(len(lista_numeros))
print(lista_numeros)

# El metodo REVERSE ordena la lista de numeros de mandera descendente
lista_numeros.reverse()
print(lista_numeros)
