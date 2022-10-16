from pickle import TRUE
import math

class punto:

    def __init__(self, coordenadas_x=0, coordenadas_y=0):
        self.coordenadas_x = coordenadas_x
        self.coordenadas_y = coordenadas_y

    def __str__(self):
        return "(X={},Y={})".format(self.coordenadas_x, self.coordenadas_y)

    def cuadrante(self):
        if self.coordenadas_x > 0 and self.coordenadas_y > 0:
            print("Los puntos->",self, "pertenecen al Primer cuadrante.")
        elif self.coordenadas_x < 0 and self.coordenadas_y > 0:
            print("Los puntos->",self, "pertenecen al Segundo cuadrante.")
        elif self.coordenadas_x < 0 and self.coordenadas_y < 0:
            print("Los puntos->",self, "pertenecen al Tercer cuadrante.")
        elif self.coordenadas_x > 0 and self.coordenadas_y < 0:
            print("Los puntos->",self, "pertenecen al Cuarto cuadrante.")
        elif self.coordenadas_x == 0 and self.coordenadas_y == 0:
            print("Los puntos->",self, "estan sobre el Origen")
        elif self.coordenadas_x == 0 and self.coordenadas_y != 0:
            print("Los puntos->",self, "se situan en el Eje Y")
        elif self.coordenadas_x != 0 and self.coordenadas_y == 0:
            print("Los puntos->",self, "se situan en el Eje X")

    def vector(self, v):
        print("El vector entre {} y {} es ({}, {})".format(self, v, v.coordenadas_x - self.coordenadas_x, v.coordenadas_y - self.coordenadas_y))
    
    def distancia(self, d):
        dist = math.sqrt((d.coordenadas_x - self.coordenadas_x)**2 + (d.coordenadas_y - self.coordenadas_y)**2)
        print("La distancia esntre los puntos", self, "y", d, "es", dist)

class rectangulo:

    def __init__(self, p_inicial = punto(), p_final = punto()):
        self.p_inicial = p_inicial
        self.p_final = p_final

        self.n_base = abs(self.p_inicial.coordenadas_x - self.p_final.coordenadas_x)
        self.n_altura = abs(self.p_final.coordenadas_y - self.p_inicial.coordenadas_y)
        self.n_area = self.n_base * self.n_altura

    def base(self):
        print("La base del del rectangulo es:",self.n_base)

    def altura(self):
        print("La altura del rectangulo es:",self.n_altura)

    def area(self):
        print("El area del rectangulo es:",self.n_area)

A = punto(2,3)
B = punto(5,5)
C = punto(-3,-1)
D = punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

rectang = rectangulo(A, B)
rectang.base()
rectang.altura()
rectang.area()