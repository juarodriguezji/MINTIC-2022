
alto=None
ancho=None
numeroPaquetes=None
profundo=None
descuento=None

import json
with open(r"C:\Users\juanr\Documents\MINTIC\CICLO 1\PROGRAMACION\Reto5\Paquetes.json") as file:
   # data = json.load(file)
   # listaPaquetes= data["PAQUETES"]
    empresa = json.load(file)
def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    costo=volumen*5
    if alto>30:
            costo=costo+2000
    if costo>10000:
            costo=costo*1.19
    return costo


def costoTotal(listaPaquetes,descuento):
   costoTotal=0
   for paquete in listaPaquetes:
        alto=float(paquete['ALTO'])
        ancho=float(paquete['ANCHO'])
        profundo=float(paquete['PROFUNDO'])
        costo=calcularCosto(alto,ancho,profundo)
        costoTotal=costoTotal+costo
   costoTotal=costoTotal*(1-(descuento/100))
   return costoTotal




