# #Tuplas:Inmutables
# tupla1=(1,2.4,"o",True,(1,4))
# #Lista : Mutable
# listas1=[1,2.4,"o",True,(1,4)]

# #Por indexacion podemos obtener un valor[]
# ext1=tupla1[2]
# print(ext1)

# #Los cubos representan metodos: Porque es aplicado a un objeto
# listas1.append("Caracacorum")#Añadir elemento
# print(listas1)
# listas1.pop()#Eliminar ultimo elemento
# print(listas1)
# listas1.insert(2,"Juan")#Insertar elemento en un indice establecido,los demas se corren.
# print(listas1)
# listas1.insert(listas1.index(["Juan"]),"Pablo")#El metodo index localiza donde esta el objeto y devuelve su indice
# # print(listas1)
# listas1.extend(range(5))#Extend añade listas enteras u objetos iterables a una cadena
# print(listas1)
# listas1.remove(4)
# print(listas1)

#Metodo para agregar elementos con un ciclo for
# lista=[]
# for i in range (10):
#     lista.append(i)
# print(lista)

#Diccionarios
# Amigo="Daniel"
# dicc={"nombre":"Juan Pablo","Amigo":Amigo,"edad":28,"Sexo":"Masculino"}
# print(dicc["Amigo"])#Indexacion con clave
# #Get obtiene el valor de una clave pero si no existe,envia un texto
# print(dicc.get("direccion","No tiene direccion"))
# #Añadir nuevo elemento al diccionario
# dicc["Pelicula"]="Star Wars"
# print(dicc)
# #Modificar elemento en el diccionario
# dicc["Pelicula"]="Jumanji"
# print(dicc)
# #Eliminar elemento
# dicc.pop("Pelicula")
# print(dicc)


#Fromkeys (De la libreria dict): Generar diccionario a partir de las claves dadas
#seq : secuencia que será el diccionario
#val:valores iniciales
# seq={"maca","ruiz","montero","bicho"}
# val={"GOATZ"}
# res_dict=dict.fromkeys(seq,val)
# print(res_dict)
# #Listar todas las claves de un diccionario
# print(res_dict.keys())
# #Listar todos los valores de un diccionario
# print(res_dict.values())
#Metodo items trae tanto clave como valor
# for clave,valor in res_dict.items():
#     print(clave,valor)
# #Iterar a traves de la lista de diccionarios
# lenguajes=[{"Python:":"ML","R":"ML"},{"C++":"GD","Python":"GD"},{"Java":"AD","Kotlin":"AD"}]
# print(lenguajes[2])

#Conjuntos
#Los conjuntos no dejan tener elementos mutables dentro, como listas.
#Los conjuntos si son mutables
# miconjunto={1,2,3}
# print(miconjunto)
# #añadir con el metodo add : Solo deja añadir enteros
# miconjunto.add(4)
# print(miconjunto)
# #eliminar: metodo remove
# miconjunto.remove(4)
# print(miconjunto)
# #pop elimina un elemento cualquiera de manera aleatoria
# miconjunto.pop()
# print(miconjunto)

# miconjunto.add(1)

# miconjunto2={4,5,6}
# miconjunto3={5,6,7}
# #Union de conjuntos
# conjmax=miconjunto.union(miconjunto2)
# print(conjmax)
# #Interseccion de conjuntos
# conjint=miconjunto2.intersection(miconjunto3)
# print(conjint)

#Frozen set :Vuelve inmutable un conjunto o lista
# cfrozen=frozenset([1,2,3])
# print(cfrozen)

# #Frozen conjunto
# c1={1,2}
# c2={3,4}
# c3=frozenset(c1.union(c2))
# print(c3)

#Ejercicios materias:Escriba una función llamada materias que, a partir de una cadena de texto con el siguiente formato: “materia1,materia2,materia3” (Ej: “Inglés,Física,Sociales,Historia,Programación”), separe las materias y las guarde en una lista. La función debe retornar la lista de materias en el orden en el que iban en la cadena de texto. 
def materias(cadena):
    lnueva=list()
    lnueva=cadena.split(",")
        
    return lnueva
print (materias("Inglés,Física,Sociales,Historia,Programación"))

# #Haga una función llamada listaFrutas que tome como parámetro una lista que contendrá cadenas de texto con nombres de frutas (Ej: [“Manzana”, “Pera”, “Uva”]). La función deberá imprimir en pantalla el nombre de cada fruta dentro de la lista, en el orden en que ahí van.
# def listaFrutas(cadena):
#     lfrutas=list()
#     for i in cadena:
#         print (i)

# print(listaFrutas(("Banano","Guayaba","Fresa")))

# #Haga una función llamada multiplicarNumeros que tome como parámetro una lista que contendrá números enteros. La función deberá retornar el resultado de la multiplicación de los números en la lista. Ejemplo:
# def multiplicarNumeros(lisa):
#     multitot=1
#     for i in lisa:
#         multitot=multitot*i
#         print (i)
#     return multitot
# print(multiplicarNumeros([2,3,5]))
