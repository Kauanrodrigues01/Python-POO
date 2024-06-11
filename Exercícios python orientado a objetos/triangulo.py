import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def eh_valido(self):
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if not self.eh_valido():
            return "Não é um triângulo válido."
        
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return round(area, 2)

triangulo1 = Triangulo(3, 4, 5)
if triangulo1.eh_valido():
    area = triangulo1.calcular_area()
    print(f'A área do triângulo é {area}')
else:
    print("Os lados fornecidos não formam um triângulo válido.")
