# imprimir el ultimo elemenmto de una lista sin saber cuantos
# elementos tiene,solucion general
otra_lista=[5,"hola que tal","",4]
print(otra_lista,3)
print("-------------")
# solusion paso por paso
dim_lista=len(otra_lista)
print("la dimde otra_lista es",dim_lista)
indice_del_ultimo=dim_lista-1
print("el indece del ultimo elementos ",indice_del_ultimo)
otra_lista[indice_del_ultimo]
#esto es equivalente
for numeros in range(1,11):
    print(numero)
# a esto
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)
# imprimir hola 10 veces

#acumuladores
challenge=(1,2,3,4,5,6,7,8,9,10) #se crea una lista
a=0                               #se crea una variable de base
for x in challenge:                #se crea un ciclo que va a correr
    a=a+x                          # se va acumulando la suma parciable

print(a)
sumatoria=0
for valor in range(1,11):
    sumatoria= sumatoria + valor
    print(sumatoria)



######################Funcion
def suma(num1,num2):
    resultado= num1+num2
    return resultado

def suma2(num1,num2):
    return num1 +num2
suma(1,5)
suma(2,6)
#print(len(listax))
prin(suma(5,10))
resul=suma(5,6)
print(resul)
#crear una funcion saludo2que reciba como parametro dos numeros
#y retorne la resta de esos numeros 

