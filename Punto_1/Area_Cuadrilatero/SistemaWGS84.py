import math
import punto
import CoordenadaGMS

class SistemaWGS84:   
    # Constantes, al estar utilizando el sistema WSG84 utilizamos el semieje mayor y menor y calculamos la excentricidad
    a = 6378137
    b = 6356752.314245
    
    @staticmethod
    def calcular_excentricidad():
        return math.sqrt(1 - (SistemaWGS84.b**2 / SistemaWGS84.a**2))
    
    @staticmethod
    def calcular_longitud_arco_paralelo(delta_x: float, y: float, e: float) -> float:
        cos = math.cos(y)
        print(cos)
        sen = math.sin(y)**2
        print(sen)
        factor_ajuste = (e**2) * sen
        numerador = SistemaWGS84.a * math.cos(y) * 2 * math.pi
        division = math.sqrt(1 - factor_ajuste)
        print(1/division)
        longitud = numerador/division
        print(longitud)
        delta_x /= 2 * math.pi
        print(delta_x)
        longitud_arco_paralelo = longitud * delta_x 
        return longitud_arco_paralelo