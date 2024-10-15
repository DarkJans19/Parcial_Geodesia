from CoordenadaGMS import CoordenadaGMS

class Punto:
    def __init__(self, x: CoordenadaGMS, y: CoordenadaGMS):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Punto(X: {self.x}, Y: {self.y})"