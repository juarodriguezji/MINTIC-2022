# def dibujar_tabla_n(a):
#     for i in range (10):
#         print("{} * {} = {}".format(a,i,a*i) )
#        
# numero=int(input("\n Por favor ingrese un numero entero positivo: "))
# while numero<=0:
#     numero=int(input("\n El numero ingresado no es un numero entero positivo,por favor ingrese un numero entero positivo: "))
# dibujar_tabla_n(numero)

#Ejercicio Tabla multiplicar
# def dibujar_tabla_n(a):
#     # for i in range (10):
#         multi=a*i
#         return multi
# numero=int(input("\n Por favor ingrese un numero entero positivo de 2 digitos: "))
# while numero<=9 or numero>99 :
#     numero=int(input("\n El numero ingresado no es un numero entero positivo de 2 digitos,por favor ingrese un numero entero positivo: "))

# for i in range (1,11):
#     multiplicacion=dibujar_tabla_n(numero)
#     print("{} * {} = {}".format(numero,i,multiplicacion) )

# #Extraccion de una parte de la tupla de salida de la definicion
# def lista():
#     return "hola",20

# tupla=lista()
# print(tupla[2])

# #Funcion Random
# import random
# resultado=random.randint(1,10)#Numero aleatorio entero
# resuni=random.uniform(1,10)#Numero aleatorio float
# lista1=[1,4,5,4.16]#Numero aleatorio de lista
# numi=random.choice(lista1)
# print(resultado)
# print(resuni)
# print(numi)

#Funcion datetime
# import datetime
# fecha=datetime.date.today()#Fecha hoy
# fechahora=  datetime.datetime.now()#Fecha y hora hoy
# print(fecha)
# print(fechahora)


#EJERCICIO
#Buscar de una cadena texto introducida una letra pero solo indicar la posicion de la que necesite el usuario

#Capitalize: Capitalizar primera letra
# ppap="i have a pen i have an apple"
# ppapC=ppap.capitalize()
# print(ppapC)

#Split
# correo="oscargonzalez@gmail.com"
# variableSplit=correo.split("@")
# print(variableSplit)

# #Definicion de parametros dentro de la llamada
# def resta(a,b):
#     return a-b
# coclea=resta(a=30,b=20)
# print(coclea)

# #For mejorado en python
# def doblar_valores(numeros):
#     for i,n in enumerate(numeros):
#         numeros[i]*=2#El "=" SIGNIFICA UNA ASIGNACION
# ns=[10,50,100]
# doblar_valores(ns)
# print(ns)

#Funcion que devuelve el cubo  de un numero el cual se pasa bajo un parametro
#Paso por valor
# def cubo_val(num):
#     resultado=num**3
#     return resultado
# num=3
# num=cubo_val(num)#Actualizo bajo lo que me retorno la funcion el numero
# print(num)

# def cubico_valores(numeros):#La variable numeros recibe la lista
#     for i,n in enumerate(numeros):
#         numeros[i]=numeros[i]**3#Forma basica para realizar la asignacion lo mismo que la linea de abajo
#         # numeros[i]**=3#El "=" SIGNIFICA UNA ASIGNACION
# ns=[2,3,4]#Paso por referencia , dato compuesto es una lista
# cubico_valores(ns)#En este paso envio los datos
# print(ns)

#Slice
lista=[4,20,30,"Oscar",(1,2,3),[4,20,30]]
print(lista[:5])#No se cuenta el ultimo elemento,asi como el range
print(lista[:])#Impresion total
print(lista[:3])#Slice 1
print(lista[3:5])#Slice 2


