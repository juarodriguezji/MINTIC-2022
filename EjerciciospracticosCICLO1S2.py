#Ejercicio clasificacion sexo e ingresos
# Nombre=input("Ingrese su nombre:")
# Sueldo=int(input("Ingrese su sueldo:"))
# Edad=int(input("Ingrese su edad:"))
# Sexo=input("Ingrese su sexo (hombre o mujer):")
# if Sexo=="hombre" and Sueldo<1200000:
#     print("Usted es un Hombre con bajos ingresos")
# if Sexo=="mujer" and Sueldo>4000000:
#     print("Usted es una Mujer con Altos ingresos")
# if Sexo=="mujer" and 1200000<Sueldo<4000000 and 20<Edad<30:
#     print("Mujer joven de clase media")

#Ejercicio prestamo a 20 años
# Salario=int(input("Ingrese su salario:"))
# Estado_Civil=input("Ingrese su estado civil (soltero o casado) :")
# Hijos=input("¿Tiene hijos? (SI O NO) :")
# if Salario>20000000:
#     print("Prestamo aceptado")
# elif 12000000<Salario<20000000 and Estado_Civil=="soltero":
#     print("Prestamo aceptado")
# elif 15000000<Salario<20000000 and Estado_Civil=="casado" and Hijos=="NO":
#     print("Prestamo concedido")
# else:
#     print("Prestamo no concedido o programa no concluyente")

#Ejercicio numero 4 Digitos
# Num1=int(input("Por favor ingrese el primer numero :"))
# Pares=0
# Impares=0
# Ceros=0
# if Num1==0:
#     Ceros=Ceros+1
# if (Num1%2)==0 and Num1>0:
#     Pares=Pares+1
# elif (Num1%2!=0):
#     Impares=Impares+1
# Num2=int(input("Por favor ingrese el segundo numero :"))
# if Num2==0:
#     Ceros=Ceros+1
# if (Num2%2)==0 and Num2>0:
#     Pares=Pares+1
# elif (Num2%2!=0):
#     Impares=Impares+1
# Num3=int(input("Por favor ingrese el tercer numero :"))
# if Num3==0:
#     Ceros=Ceros+1
# if (Num3%2)==0 and Num3>0:
#     Pares=Pares+1
# elif (Num3%2!=0):
#     Impares=Impares+1
# Num4=int(input("Por favor ingrese el cuarto numero :"))
# if Num4==0:
#     Ceros=Ceros+1
# if (Num4%2)==0 and Num4>0:
#     Pares=Pares+1
# elif (Num4%2!=0):
#     Impares=Impares+1
# print("El numero ingresado es %d%d%d%d, asi mismo, el total de numeros pares es %d y el total de impares es %d.Complementario tiene %d ceros."%(Num1,Num2,Num3,Num4,Pares,Impares,Ceros))

# #Ejercicio Dos numeros enteros
# Numa=int(input("Ingrese el primer digito del primer numero:"))
# Numb=int(input("Ingrese el segundo digito del primer numero:"))
# Numc=int(input("Ingrese el primer digito del segundo numero:"))
# Numd=int(input("Ingrese el segundo digito del segundo numero:"))


#Ejercicio horas extra
# Horas_T=int(input("Por favor ingrese el numero de horas:"))
# Horas_Normal=8
# Horas_Extra=Horas_T-Horas_Normal
# Horas_Extra_Doble=0
# Horas_Extra_Triple=0
# if Horas_Extra >0 and Horas_Extra>8:
#     Horas_Extra_Doble=8
#     Horas_Extra_Triple=Horas_T-8-8
# else:
#     Horas_Extra_Doble=Horas_T-8
#     Horas_Extra_Triple=0
# print("Su pago del dia será: Horas Normales %d , Horas Extras(Pago Doble) %d y Horas Extra(Pago Triple) %d"%(Horas_Normal,Horas_Extra_Doble,Horas_Extra_Triple))  

#Ejercicio museo Python
print("Hola:  Bienvenido al museo de Python --_-_-_-o~")
Edad=int(input("Si deseas saber el precio de tu entrada, por favor indica tu edad: "))
if Edad<=6:
    print("Genial! Entras gratis al museo")
else:
    Cupon=input("OK,¿Tiene bono de descuento para este mes? responde (s/n):")
    if 6<Edad<22:
        if Cupon=="s":
            Precio_O=9
            Precio_D=9*0.9
            print("El precio de la entrada sin descuento es de %d euros. Con el descuento sería: %d"%(Precio_O,Precio_D))
        else:
            Precio_O=9
            print("El precio de la entrada sin descuento es: %d"%(Precio_O))
    elif 21<Edad<67:
        if Cupon=="s":
            Precio_O=14
            Precio_D=14*0.9
            print("El precio de la entrada sin descuento es de %d euros. Con el descuento sería: %d"%(Precio_O,Precio_D))
        else:
            Precio_O=14
            print("El precio de la entrada sin descuento es: %d"%(Precio_O))
    elif Edad>=67:
        if Cupon=="s":
            Precio_O=6
            Precio_D=6*0.9
            print("El precio de la entrada sin descuento es de %d euros. Con el descuento sería: %d"%(Precio_O,Precio_D))
        else:
            Precio_O=6
            print("El precio de la entrada sin descuento es: %d"%(Precio_O))
print("Disfrute parce!")
            