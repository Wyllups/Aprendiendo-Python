# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:39:17 2025

@author: Wilfredo
"""
print("Listas ejemplo")

lista1 = [31.1, 31.9,31.7,31.4,31.2]

print("--------------------------------------------") 

#sort(): Ordena la lista en orden ascendente.

lista1.sort()
print(lista1)

print("--------------------------------------------") 

#tipo(lista): Devuelve el tipo de clase de un objeto.

print(type(lista1))

print("--------------------------------------------") 

#append(): Añade un único elemento a una lista.

lista1.append(31.3)
print(lista1)

print("--------------------------------------------") 

#extend(): Añade varios elementos a una lista.

lista1.extend([31.5,31.8,31.6])
print(lista1)

print("--------------------------------------------") 

#index(): Devuelve la primera aparición del valor especificado.

Lista = ["Perro", "Gato", "Pollo", "Leon", "tigre"]

precios = [31.1, 31.9,31.7,31.4,31.2]

Lista.index("Gato")

print(precios[1])

print("--------------------------------------------") 

#max(lista): Devuelve un elemento de la lista con valor máximo.

print(max(precios))

print("--------------------------------------------") 

#min(list): Devuelve un elemento de la lista con valor min.

print(min(precios))

print("--------------------------------------------") 

#len(lista): Da la longitud total de la lista.

print(len(Lista))

print("--------------------------------------------") 


#list(seq): Convierte una tupla en una lista.

numeros = (1,2,3,4,5,6,7,8,9)

list(numeros) 
print(list(numeros))

print("--------------------------------------------") 

#filter(fun,list): filtra la lista utilizando la función de Python. 

def filter_price(price):
    if (price > 350):
        return True
    else:
        return False
 
item_price = [230, 400, 450, 350, 370]

filtered_price = filter(filter_price, item_price)


print(list(filtered_price))


print("--------------------------------------------") 


#%%

"Tuple ejemplos"



tupla = (1, 2, 3)

print("--------------------------------------------") 

#Al igual que las listas, las tuplas también pueden ser anidadas.

tupla = 1, 2, ('a', 'b'), 3
print(tupla)
print(tupla[2][0])

print("--------------------------------------------") 

#{}es posible convertir una lista en tupla haciendo uso de al función tuple().

lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla))
print(tupla)
print("--------------------------------------------") 

#Se puede iterar una tupla de la misma forma que se hacía con las listas.

tupla = [1, 2, 3]
for t in tupla:
    print(t)
    
print("--------------------------------------------") 

#asignar el valor de una tupla con n elementos a n variables.

l = (1, 2, 3)
x, y, z = l
print(x, y, z) #1 2 3

print("--------------------------------------------") 

#es posible crear una tupla de un solo elemento. Para ello debes usar 
#, antes del paréntesis, porque de lo contrario (2) sería interpretado como int.

tupla = (2,)
print(type(tupla)) #<class 'tuple'>

print("--------------------------------------------") 

#El método count() cuenta el número de veces que el objeto pasado como 
#parámetro se ha encontrado en la lista.

l = [1, 1, 1, 3, 5]
print(l.count(1)) #3
#index(<obj>[,index])

print("--------------------------------------------") 

#El método index() busca el objeto que se le pasa como parámetro y devuelve el
# índice en el que se ha encontrado.

l = [7, 7, 7, 3, 5]
print(l.index(5)) #4

print("--------------------------------------------") 

#En el caso de no encontrarse, se devuelve un ValueError.

l = [7, 7, 7, 3, 5]

print("--------------------------------------------") 

#El método index() también acepta un segundo parámetro opcional, que indica a 
#partir de que índice empezar a buscar el objeto.

l = [7, 7, 7, 3, 5]
print(l.index(7, 2))

#%%
"Diccionario ejemplos"

datos = { "cedula":1077841388,
         "nombre":"Wilfredo",
         "edad":20,
         "altura":1.72}

print("--------------------------------------------") 

datos1 = dict([
    ("cedula",1985435),
    ("nombre","Juan"),
    ("edad",30),
    ("Altura",1.70)
    ])

print("--------------------------------------------") 

datos2 = dict(
    cedula=10657843,
    nombre="Sofia",
    edad = 39,
    altura = 1.60
    )

print("--------------------------------------------") 

#Acceder y modificar elementos
#Se puede acceder a sus elementos con [] o también con la función get()

print(datos["nombre"])

print(datos.get("nombre"))

print("--------------------------------------------") 

#Para modificar un elemento basta con usar [] con el nombre del key y asignar el valor que queremos.

datos["nombre"] = "Laura"
print(datos)

print("--------------------------------------------") 

#Si el key al que accedemos no existe, se añade automáticamente.

datos['Direccion'] = "Calle 1"
print(datos)

print("--------------------------------------------")

#Iterar diccionario
# Imprime los key del diccionario
for x in datos:
    print(x)

print("--------------------------------------------")

# Impre los value del diccionario
for x in datos:
    print(datos[x])

print("--------------------------------------------")

# Imprime los key y value del diccionario
for x, y in datos.items():
    print(x, y)

print("--------------------------------------------")

#Diccionarios anidados

datos1y2 = {
  "datos1" : datos2,
  "datos2" : datos1
}
print(datos1y2)

print("--------------------------------------------")

#Métodos diccionarios Python
#clear()
#El método clear() elimina todo el contenido del diccionario.

d = {'a': 1, 'b': 2}
d.clear()
print(d)

print("--------------------------------------------")

#get(<key>[,<default>])
#El método get() nos permite consultar el value para un key determinado. 
#El segundo parámetro es opcional, y en el caso de proporcionarlo es el valor a 
#devolver si no se encuentra la key.

d = {'a': 1, 'b': 2}
print(d.get('a'))
print(d.get('z', 'No encontrado'))

print("--------------------------------------------")

#items()
#El método items() devuelve una lista con los keys y values del diccionario. 
#Si se convierte en list se puede indexar como si de una lista normal se tratase, 
#siendo los primeros elementos las key y los segundos los value.

d = {'a': 1, 'b': 2}
it = d.items()
print(it)
print(list(it))
print(list(it)[0][0])

print("--------------------------------------------")

#keys()
#El método keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)
print(list(k))

print("--------------------------------------------")

#values()
#El método values() devuelve una lista con todos los values o valores del diccionario.

d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

print("--------------------------------------------")

#pop(<key>[,<default>])
#El método pop() busca y elimina la key que se pasa como parámetro y devuelve 
#su valor asociado. Daría un error si se intenta eliminar una key que no existe.

d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}

print("--------------------------------------------")

#También se puede pasar un segundo parámetro que es el valor a devolver si la 
#key no se ha encontrado. En este caso si no se encuentra no habría error.

d = {'a': 1, 'b': 2}
d.pop('c', -1)
print(d) #{'a': 1, 'b': 2}

print("--------------------------------------------")

#popitem()
#El método popitem() elimina de manera aleatoria un elemento del diccionario.

d = {'a': 1, 'b': 2}
d.popitem()
print(d)

print("--------------------------------------------")

#{'a': 1}
#update(<obj>)
#El método update() se llama sobre un diccionario y tiene como entrada otro 
#diccionario. Los value son actualizados y si alguna key del nuevo diccionario
# no esta, es añadida.

d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)

print("--------------------------------------------")

#%% 

"Conjuntos ejemplos"

#Métodos básicos
#add()
#Añade un ítem a un conjunto, si ya existe no lo añade:


c = set()
c.add(1)
c.add(2)
c.add(3)
c

{1, 2, 3}

print("--------------------------------------------")

#discard()
#Borra un ítem de un conjunto:

c.discard(1)
c

{2, 3}

print("--------------------------------------------")

#copy()
#Devuelva una copia de un conjunto, ya que éstos como la mayoría de colecciones 
#se almacenan por referencia:


c1 = {1,2,3,4}
c2 = c.copy()
print(c1, c2)
c2.discard(4)
print(c1, c2)

print("--------------------------------------------")

#clear()
#Borra todos los ítems de un conjunto:

c2.clear()


print("--------------------------------------------")

#set()
#Comparación de conjuntos

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

print("--------------------------------------------")

#isdisjoint()
#Comprueba si el conjunto es disjunto de otro conjunto, es decir, si no hay ningún elemento en común entre ellos:


c1.isdisjoint(c2)

print("--------------------------------------------")

#issubset()
#Comprueba si el conjunto es subconjunto de otro conjunto, es decir, si sus ítems se encuentran todos dentro de otro:

print("--------------------------------------------")

c3.issubset(c4)

print("--------------------------------------------")

#issuperset()
#Comprueba si el conjunto es contenedor de otro subconjunto, es decir, si 
#contiene todos los ítems de otro:


c3.issuperset(c1)

False
#Métodos avanzados
#Se utilizan para realizar uniones, diferencias y otras operaciones avanzadas entre conjuntos.

#Suelen tener dos formas, la normal que devuelve el resultado, y otra que hace lo mismo pero actualiza el propio resultado.

#union()
#Une un conjunto a otro y devuelve el resultado en un nuevo conjunto:

print("--------------------------------------------")

c1 = {1,2,3}
c2 = {3,4,5}
c3 = c1.union(c2)
print(c1, "+", c2, "=", c3)

print("--------------------------------------------")

#update()
#Une un conjunto a otro en el propio conjunto:


c1.update(c2)
c1

print("--------------------------------------------")

#difference()
#Encuentra los elementos no comunes entre dos conjuntos:


c1 = {1,2,3}
c2 = {3,4,5}

c1.difference(c2)

print("--------------------------------------------")

#difference_update()
#Guarda en el conjunto los elementos no comunes entre dos conjuntos:


c1.difference_update(c2)
c1

print("--------------------------------------------")

#intersection()
#Devuelve un conjunto con los elementos comunes en dos conjuntos:


c1 = {1,2,3}
c2 = {3,4,5}

c1.intersection(c2)

print("--------------------------------------------")

#intersection_update()
#Guarda en el conjunto los elementos comunes entre dos conjuntos:


c1.intersection_update(c2)
c1

print("--------------------------------------------")

#symmetric_difference()
#Devuelve los elementos simétricamente diferentes entre dos conjuntos, es decir, 
#todos los elementos que no concuerdan entre los dos conjuntos:


c1 = {1,2,3}
c2 = {3,4,5}

c1.symmetric_difference(c2)

print("--------------------------------------------")
















































