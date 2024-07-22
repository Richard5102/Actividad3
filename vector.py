import math

class Vector: 
   
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.magnitud = math.sqrt(math.pow(x,2)+math.pow(y,2))
        self.angulo = math.atan(y/x)
        self.anguloGrados = math.degrees(self.angulo)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other): 
        return Vector(self.x - other.x, self.y - other.x)


v1 = Vector(5,5)
v2 = Vector(10,10)
v3 = v1 + v2
print(f"Las coordenadas son: {v1}")
print(f"La magnitud es {v1.magnitud}")
print(f"El angulo es {v1.angulo} en radianes y {v1.anguloGrados} en grados" )
      
print(f"Sumando el vector v1: {v1} y v2: {v2} da: {v3} con magnitud: {v3.magnitud}")

#Ejemplo 
print("\n****************** Ejemplo ***************** \n")
p = Vector(5, -1)
q = Vector(2, -4)
print(f"Magnitud de p (5, -1): {p.magnitud}")
print(f"Angulo en rad {p.angulo}")
print(f"Angulo en grados {p.anguloGrados}")

print(f"Magnitud de q (5, -1): {q.magnitud}")
print(f"Angulo en rad {q.angulo}")
print(f"Angulo en grados {q.anguloGrados}")

print(f"Suma de los valores p y q: {p + q}")

