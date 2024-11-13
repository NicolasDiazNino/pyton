# ¿que es una lista?
# Una lista es una estructura de datos que te permite almacenar varios elementos en una sola variable. 
# Los elementos de una lista están ordenados y son modificables, es decir, puedes cambiar, 
# añadir o eliminar elementos en cualquier momento. En Python, las listas se crean con corchetes [] 
# y los elementos se separan por comas.

# Ejemplo basico

mi_lista = [10, 20,"Hola", 3.14, True]

# En este ejemplo, mi_lista es una lista que contiene varios tipos de datos: un entero (10), 
# otro entero (20), una cadena de texto ("hola"), un número decimal (3.14), y un booleano (True).

# 1.Practica

frutas = ["Manzana", "banana", "naranja","pera"]
#print(frutas[0])
#print(frutas[-1])

# 2.Modificacion de elementos

frutas[1]= "kiwi"
#print(frutas)

# 3.Añadir elementos a una lista

# Puedes usar append() para agregar un elemento al final de la lista o insert() para agregarlo 
# en una posición específica.

frutas.append("mango")
#print(frutas)

# al solo poner el objeto que se va a insertar en la lista se va a añadir a cola de la fila

frutas.insert(1,"fresa")
#print(frutas)

# al poner un numero antes del objeto se pondra en esa posicion
# NOTA: los objetos se cuentan desde el 0

# 4.Eliminar elementos de la lista

# Usa remove() para eliminar un elemento específico, pop() para eliminar el elemento en un índice, 
# o clear() para vaciar la lista completamente.

frutas.remove("kiwi")
#print(frutas)   

frutas.pop()
#print(frutas)

frutas.clear()
#print(frutas)

# 5. Recorrer una lista

# Puedes usar un bucle for para recorrer cada elemento de la lista.

frutas = ["Manzana", "banana", "naranja"]
for fruta in frutas:
    print("Me gusta la", fruta)

# 6. Longitud de la lista

# La función len() te da la cantidad de elementos en la lista.

print(len(frutas))