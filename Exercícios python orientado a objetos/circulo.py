class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area_do_circulo(self):
        pi = 3.14159265358979323846
        area = pi * (self.raio ** 2)
        area = round(area, 2)
        print(f'A área do circulo é {area}')

    def calcular_perimetro(self):
        pi = 3.14159265358979323846
        perimetro = (2 * pi * self.raio)
        perimetro = round(perimetro, 2)
        print(f'perimetro: {perimetro}')

circulo1 = Circulo(3)
circulo1.area_do_circulo()
circulo1.calcular_perimetro()