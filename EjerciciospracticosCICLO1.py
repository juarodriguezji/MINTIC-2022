#1.Area de la figura seria: (pi*Rcuad)/2 + (R*H)
from cmath import pi

R=input("Por favor inserte el valor de R")
H=input("Por favor inserte el valor de H")
R=float(R)
H=float(H)
area= ((pi*(R**2))/2)+(R*H)
print("El area de la figura es"+" ",area)

#2. Ejercicio parentesis sabrosos
X=input("Ingrese el valor que desee y presencie la magia")
X=float(X)
oper=1/(X+(1/(X+(1/(X+(1/X))))))
print("El resultado es"+" ",oper )

#3. Ejercicio Tiempo Final
HoraInicial=input("Ingrese la hora inicial")
MinutoInicial=input("Ingrese los minutos iniciales")
Duracion=input("Ingrese la duración del evento")
HoraInicial=int(HoraInicial)
MinutoInicial=int(MinutoInicial)
Duracion=int(Duracion)
MinutoFinal=MinutoInicial+(Duracion%60)
MinutoFinalB=((MinutoInicial+(Duracion%60))%60)
HoraFinal=((HoraInicial+(Duracion//60)+(MinutoFinal//60))%24)


print("Su hora inicial es"," ",HoraInicial,":",MinutoInicial)
print("Y según la duración del evento,este terminará a las"," ",HoraFinal,":",MinutoFinalB)

#4.Puntaje Fichas
Gan=input("Ingrese las veces que usted quedó ganador")
Seg=input("Ingrese las veces que usted quedó en segundo lugar")
Ter=input("Ingrese las veces que usted quedó en tercer lugar")
Gan=int(Gan)
Seg=int(Seg)
Ter=int(Ter)
PunFin=Gan+(Seg*2)-(Ter**2)
print("Su puntaje final del juego es",":",PunFin)