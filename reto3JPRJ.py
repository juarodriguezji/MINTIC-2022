# Tu tarea esta semana es hacer que el software de la semana pasada lea una nueva variable que sea el número de paquetes a calcular. Luego, que aplique el mismo algoritmo de cálculo de costo el número de veces que se haya indicado en la nueva variable, imprimiendo los valores de volumen y costo. Al finalizar, el programa también deberá imprimir el valor de costo total.

# Lee detenidamente el planteamiento del reto, cuando se te indique que hay que seguir un orden, es necesario que así sea. Sigue atentamente los pasos de la solución del reto si tienes dificultades al resolverlo.
numeroPaquetes=int(input())
costoTotal=0
for i in range(0,numeroPaquetes):
    alto=float(input())
    ancho=float(input())
    profundo=float(input())
    volumen=alto*ancho*profundo
    costo=volumen*5
    if alto>30:
        costo=costo+2000
    if costo>10000:
        costo=costo*1.19
    print(volumen)
    print(costo)
    costoTotal=costoTotal+costo
print(costoTotal)