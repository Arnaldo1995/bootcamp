class persona:
    edad = 0
    def __init__(self,un_nombre):
        self.mi_nombre =un_nombre
        print("hola naci, me llamo", self.mi_nombre)
    def cumple(self):
        self.edad = self. edad + 1

pepe = persona("pepito")
pepa = persona("pepita")
print(pepe.edad)
print(pepe.mi_nombre)

pepe. cumple()
pepe. cumple()
pepe. cumple()
print(pepe.edad)
 
