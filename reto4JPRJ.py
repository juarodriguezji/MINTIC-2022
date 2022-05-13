
# numeroPaquetes=int(input())
# costoTotal=0
# for i in range(0,numeroPaquetes):
#     alto=float(input())
#     ancho=float(input())
#     profundo=float(input())
#     volumen=alto*ancho*profundo
#     costo=volumen*5
#     if alto>30:
#         costo=costo+2000
#     if costo>10000:
#         costo=costo*1.19
#     print(volumen)
#     print(costo)
#     costoTotal=costoTotal+costo
# print(costoTotal)
alto=None
ancho=None
numeroPaquetes=None
profundo=None
descuento=None

def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    costo=volumen*5
    if alto>30:
            costo=costo+2000
    if costo>10000:
            costo=costo*1.19
    return costo


def costoTotal(numeroPaquetes,descuento):
    costoTotal=0
    for i in range(0,numeroPaquetes):
        alto=float(input("ingrese alto"))
        ancho=float(input("ingrese ancho"))
        profundo=float(input("ingrese profu"))
        costo=calcularCosto(alto,ancho,profundo)
        costoTotal=costoTotal+costo
    costoTotal=costoTotal*(1-(descuento/100))
    return costoTotal
print(calcularCosto(35,10,5))
print(costoTotal(2,50 ))
    