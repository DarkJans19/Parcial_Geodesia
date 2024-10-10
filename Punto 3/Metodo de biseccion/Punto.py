import math

class Punto:
    def __init__(self, x: float, y: float, direccion: str, angulo: float):
        self.x = x
        self.y = y
        self.direccion = direccion.upper()  # Dirección puede ser N, S, E, W
        self.angulo = angulo

    def ajustar_signo(self, valor: float) -> float:
        """Ajusta el signo según la dirección."""
        if self.direccion == 'S' or self.direccion == 'W':
            return -valor
        return valor
    
    # Self.x es el valor de x del primer punto y b.x es el valor de X en el segundo punto
    def diferencia_x(self, b: 'Punto') -> float:
        return self.x - b.x
    
    # Self.y es el valor de y del primer punto y b.y es el valor de y en el segundo punto
    def diferencia_y(self, b: 'Punto') -> float:
        return self.y - b.y
    
    # En este caso b son los valores del otro punto
    def distancia(self, b: 'Punto'):
        diferencia_x = self.diferencia_x(b)
        print("diferencia_x:", diferencia_x)
        diferencia_y = self.diferencia_y(b)
        print("diferencia y:",diferencia_y)
        distancia = pow(diferencia_x, 2) + pow(diferencia_y, 2)
        return math.sqrt(distancia)
    
    # Esta funcion calcula el azmiut de los angulos
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
    
    # Esta funcion calcula el gamma
    def calcular_gamma(self, b: 'Punto') -> float:
        gamma = 180 - (self.angulo + b.angulo)
        return gamma
    
    # Como es la distancia al punto que estamos buscando no utilizamos la funcion distancia normal sino utilizamos una formula diferente
    def distancia_punto_P(self, b: 'Punto', gamma: float):
        ap = (math.sin(math.radians(b.angulo))/math.sin(math.radians(gamma))) * self.distancia(b)
        return ap
    