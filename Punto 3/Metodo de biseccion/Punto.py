import math

class Punto:
    def __init__(self, x: float, y: float, direccion_x: str, direccion_y: str, angulo: float):
        self.x = x
        self.y = y
        self.direccion_x = direccion_x.upper()  # Dirección puede ser N, S, E, W
        self.direccion_y = direccion_y.upper()  # Dirección puede ser N, S, E, W
        self.angulo = angulo

    def ajustar_signo(self, valor: float, direccion: str) -> float:
        """Ajusta el signo según la dirección."""
        if direccion == 'S' or direccion == 'W':
            return -valor
        return valor
    
    def diferencia_x(self, b: 'Punto') -> float:
        # Ajustamos las coordenadas de acuerdo con la dirección
        diferencia_x = self.x - b.x
        return self.ajustar_signo(diferencia_x, self.direccion_x)
    
    def diferencia_y(self, b: 'Punto') -> float:
        # Ajustamos las coordenadas de acuerdo con la dirección
        diferencia_y = self.y - b.y
        return self.ajustar_signo(diferencia_y, self.direccion_y)
    
    def distancia(self, b: 'Punto'):
        diferencia_x = self.diferencia_x(b)
        print("diferencia_x:", diferencia_x)
        diferencia_y = self.diferencia_y(b)
        print("diferencia y:", diferencia_y)
        distancia = pow(diferencia_x, 2) + pow(diferencia_y, 2)
        return math.sqrt(distancia)
    
    def calcular_AzAB(self, b: 'Punto') -> float:
        diferencia_x = self.diferencia_x(b)
        diferencia_y = self.diferencia_y(b)
        AzAB = math.atan2(diferencia_x, diferencia_y)
        return math.degrees(AzAB)
    
    def calcular_azimut(self, b: 'Punto'):
        AzAB = self.calcular_AzAB(b)
        azimut = 180 - (AzAB + self.angulo)
        if azimut < 0:
            azimut += 360
        return azimut
    
    def calcular_gamma(self, b: 'Punto') -> float:
        gamma = 180 - (self.angulo + b.angulo)
        return gamma
    
    def distancia_punto_P(self, b: 'Punto', gamma: float):
        ap = (math.sin(math.radians(b.angulo))/math.sin(math.radians(gamma))) * self.distancia(b)
        return ap