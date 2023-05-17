#Declararando lista de 5 elementos
numbers = [10, 5, 7, 2, 1]

#imprimir lista creada
print("Contenido de la lista:", numbers)

#asignando un valor al primer elemento de la lista
numbers[0] = 111

# Imprimir el primer elemento de la lista.
print(numbers[0]) 

#asignando al segundo elemento de la lista el valor del quinto elemento de la lista
numbers[1] = numbers[4]

#Mostrando la longitud de la lista creada
print("Longitud de la lista:", len(numbers))

#Eliminando el segundo elemento de la lista
del numbers[1]

#los negativos van mostrando los valores desde el último elemento de la lista hasta el primero
#Imprimir el último elemento de la lista
print(numbers[-1])

#Imprimir el penúltimo elemento de la lista
print(numbers[-2])

#Cambiar un elemento de una lista, asignandole un valor ingresado por el usuario
print("Ingrese un número para cambiar el tercer valor de la lista")
numero = input()
hat_list [2] = int(numero)

#Agregando un elemento a la lista mediante append que tenga como valor: 4. Esta función agrega el elemento al final de la lista
numbers.append(4)

#Agregando un elemento a la lista mediante insert. Con esta función es necesario asignar la posición y el valor. Para este caso ubicamos en la posición 0 de la lista y le asignamos el valor de: 222.
numbers.insert(0, 222)

#Crear una lista vacía y llenarla usando un ciclo for, con 5 elementos que inicien en forma ascendente
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#Crear una lista vacía y llenarla usando un ciclo for, con 5 elementos que inicien en forma descendente
my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

#Sumar los valores que se encuentran en una lista de 5 elementos
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

#intercambiar los elementos de la lista para revertir su orden (Podrías usarlo para listas pequeñas)
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)






