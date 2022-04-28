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

# #Ejercicio numero 4 Digitos

# #Ejercicio Dos numeros enteros
# Num1=int(input("Ingrese el primer numero"))
# Num2=int(input("Ingrese el segundo numero"))
# Dif=Num2-Num1

#Ejercicio horas extra
Horas_T=int(input("Por favor ingrese el numero de horas:"))
Horas_Normal=8
Horas_Extra=Horas_T-Horas_Normal
Horas_Extra_Doble=0
Horas_Extra_Triple=0
if Horas_Extra >0 and Horas_Extra>8:
    Horas_Extra_Doble=8
    Horas_Extra_Triple=Horas_T-8-8
else:
    Horas_Extra_Doble=Horas_T-8
    Horas_Extra_Triple=0
print("Su pago del dia será: Horas Normales %d , Horas Extras(Pago Doble) %d y Horas Extra(Pago Triple) %d"%(Horas_Normal,Horas_Extra_Doble,Horas_Extra_Triple))  
    