import math
import numpy as np
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
        sen = math.sin(y)**2
        factor_ajuste = (e**2) * sen
        delta_x /= 2 * math.pi
        numerador = SistemaWGS84.a * cos * 2 * math.pi
        division = math.sqrt(1 - factor_ajuste)
        longitud = numerador/division
        longitud_arco_paralelo = longitud * delta_x 
        return longitud_arco_paralelo
    
    
    @staticmethod
    def graficar_elipsoide():
        # Crear una malla esférica para el elipsoide
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = SistemaWGS84.a * np.outer(np.cos(u), np.sin(v))
        y = SistemaWGS84.b * np.outer(np.sin(u), np.sin(v))
        z = SistemaWGS84.b * np.outer(np.ones(np.size(u)), np.cos(v))

        return x, y, z

    @staticmethod
    def graficar_puntos(ax, puntos):
        coord_puntos = []
        for punto in puntos:
            x = punto.x.convertir_a_radianes()
            y = punto.y.convertir_a_radianes()
            # Convertir a coordenadas cartesianas
            coord_x = SistemaWGS84.a * np.cos(y) * np.cos(x)
            coord_y = SistemaWGS84.b * np.cos(y) * np.sin(x)
            coord_z = SistemaWGS84.b * np.sin(y)
            ax.scatter(coord_x, coord_y, coord_z, s=100)  # Graficar el punto
            coord_puntos.append((coord_x, coord_y, coord_z))  # Guardar las coordenadas

        return coord_puntos  # Devolver las coordenadas de los puntos