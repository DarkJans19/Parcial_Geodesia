import math

class CoordenadaGMS():
    def __init__(self, grados, minutos, segundos, direccion):
        self.grados = grados
        self.minutos = minutos
        self.segundos = segundos
        self.direccion = direccion.upper()
    
    def convertir_a_radianes(self):
        # Convertir a grados decimales y luego a radianes
        grados = self.grados + (self.minutos / 60) + (self.segundos / 3600)
        radianes = math.radians(grados)
        # Ajustar para direcciones sur (S) y oeste (W)
        if self.direccion in ['S', 'W']:
            radianes = -radianes
        return radianes    
    
    def __str__(self):
        return f"{self.grados}°{self.minutos}'{self.segundos}\" {self.direccion}"