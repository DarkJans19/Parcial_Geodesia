import math

class CoordenadaGMS():
    def __init__(self, grados, minutos, segundos, direccion):
        self.grados = grados
        self.minutos = minutos
        self.segundos = segundos
        self.direccion = direccion.upper()
    
    def convertir_a_radianes(self):
        # Para convertir de grados minutos y segundos a radianes podemos pasar el angulo a grados y luego a radianes
        grados = self.grados + (self.minutos / 60) + (self.segundos / 3600)
        radianes = math.radians(grados)
        if self.direccion in ['S', 'W']:
            radianes = -radianes
        return radianes    
    
    def to_decimal(self):
        # Convertir grados, minutos y segundos a decimal
        decimal = self.grados + self.minutos / 60 + self.segundos / 3600

        # Si la dirección es 'S' o 'W', el valor debe ser negativo
        if self.direccion in ['S', 'W']:
            decimal = -decimal
        
        return decimal
    
    def __str__(self):
    # Representación de la coordenada
        return f"{self.grados}°{self.minutos}'{self.segundos}\" {self.direccion}"