# esto es una informacion para que me ayude a identificar donde utilisar el for
# donde poder utilisar la lista y los ingredientes
ingre_pan =["harina","sal","agua","levadora","azucar"]
def imprimir_lista(ingredientes):
    for productos in ingredientes :
        print(productos)
imprimir_lista(ingre_pan)
###################
a = 3
if a > 3:
    print("si,a es mayor a 3")
    print("chau")
else:
    print("NO, no es mayor 3")

if a==3:
    print("a es iguala 3")
##########################comentarios#################
# nota 1
# == igual
# > mayor que
# < menor que
# >= ,mayor o igual que
# <= menor o igual que
# != distinto o no igual que
# =3
#pregunta 2
if a == 3:
    print("a es igual a 3")
nota = 60
# pregunta 3
if nota >=60:
    print("pasastee")
else:
    print("ule ya")
# ej crear una funcion lista nota como parametro
# nota del 1 al 100 e imprima si pasaste o te aplazaste ( se aprueba con 61)
def resultados(nota):
    if nota >=60:
        print("pasate de grado")
    else:
        print("hule")
resultados(60)
#############3
#puntaje(60,"pepito")
a = 7
if a > 5 and a < 10:
    print("a es mayor a 5y menorque 10")
else:
    print("a no esta en el rango, algunas de ls 2 condiciones no se cumplieron")
if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")

edad = 7
if edad > 18:
        print("deberia estar en la universidad")
elif edad > 13:("deberia estar em secundaria")
elif edad > 6:
    print("deberia estar en primaria")
else:
    print("deberia estar en su casa bbdlc")
#an1dado
if edad > 18:
    print("universidad")
else:
    if edad>13:
        print("secundaria")
    else:
        if edad > 6:
            print("primaria")
        else:
            print("bbdlc")
####################ejercici#######
#crear una funcion con puntaje que reciba como parametro un puntaje
# de uno al 100 e imprima que nota sacaste
# nota < 60----------->1
# nota entre 60 y 70---->2
# nota entre 71 y 75------->3
# nota entre 76 y 85-------->4
# nota mayor que 85----------->5
def calificacion(nota):
    if nota<60:
        print("sacaste1")
    elif nota >60 and nota<70:
        print("sacaste2")
    elif nota <71 and nota>75:
        print("sacaste3")
    elif nota>76 and nota<85:
        print("sacaste4")
    elif nota >=85 and nota <=100:
        print("sacaste 5")

# Ej1 pedir al usuario que ingrese tresn numeros y multiplicarlos
# entre si, imprimir el reultado
#int("22")
nro1= int( input("dame un numero "))
nmr2= int( input("dame un numero mas "))
numr3= int (input("dame mas numero "))
print(nro1*nmr2*numr3)

# ej2 pedir al usuario el numero del 1 al 100 y llamar ala 
# funcion que retornaba la nota que creamos hace un rato
# utilizando el valor ingresado por el usuario

#####################ej##############3*=0
while x1= 5:
    print("hola esto es un bucle wh1lle, se va a ejecutar mientras")
    x = int(inpu("ingresa un numero:"))
    print("el valor de x ahora es",x)
print("termino,]]")
contador = 10
while contador > 0:
    print("sigo en el bucle wh1le")
    contador = contador - 1
    print("te quedan".contador,"oportunidades")
# ej crear un juego de adivinar el numero como el de arriba y
# darle pistas al usuario si el numero que inngreso es mayor o menor
# al numero a divinar
# pista usar elif
estado = False
numa = 5

while estado == False:
    ingreso = int(input("ingresa un numero"))

    if ingreso == numa:
        print("ganaste")
        estado = True
    else:
        print("intenta otro")