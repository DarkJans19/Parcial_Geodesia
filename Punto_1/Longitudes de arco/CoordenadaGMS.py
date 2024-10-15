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
    
    def diferencia_coordenada(self, b):
        diferencia_radianes = self.convertir_a_radianes() - b.convertir_a_radianes()
        return diferencia_radianes
    
    def suma_coordenada(self, b):
        diferencia_radianes = self.convertir_a_radianes() + b.convertir_a_radianes()
        return diferencia_radianes
    
    def __str__(self):
    # Representación de la coordenada
        return f"{self.grados}°{self.minutos}'{self.segundos}\" {self.direccion}"