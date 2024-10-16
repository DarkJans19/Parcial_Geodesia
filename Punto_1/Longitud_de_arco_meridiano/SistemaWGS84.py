import math
import numpy as np
class SistemaWGS84:   
    # Constantes, al estar utilizando el sistema WSG84 utilizamos el semieje mayor y menor y calculamos la excentricidad
    a = 6378137
    b = 6356752.314245
    
    @staticmethod
    def calcular_excentricidad():
        return math.sqrt(1 - (SistemaWGS84.b**2 / SistemaWGS84.a**2))
    
    """
    Toda la formula es: 
    Tomando y como los angulos de los paralelos
    a(y1 - y2) - (1-e²)a/2 * sin(2(y1+y2)) * (y2-y1)
    """
    
    @staticmethod
    def calcular_longitud_arco_meridiano(delta_y: float, suma_y: float, x: float, e: float):
        parte_1 = SistemaWGS84.a * (delta_y)
        parte_2 = ((1 - e **2) * SistemaWGS84.a)/2
        arg_sen = 2 * suma_y
        parte_3 = math.sin(arg_sen)
        parte_4 = parte_2 * parte_3 * delta_y
        longitud_arco_meridiano = parte_1 - parte_4
        return longitud_arco_meridiano
    
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