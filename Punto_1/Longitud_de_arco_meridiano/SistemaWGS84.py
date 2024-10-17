import math
import numpy as np
import matplotlib.pyplot as plt

class SistemaWGS84:   
    # Constantes del sistema WGS84
    a = 6378137  # Semi-eje mayor (metros)
    b = 6356752.314245  # Semi-eje menor (metros)
    
    @staticmethod
    def calcular_excentricidad():
        return math.sqrt(1 - (SistemaWGS84.b**2 / SistemaWGS84.a**2))
    
    @staticmethod
    def calcular_coeficientes(e):
        # Coeficientes hasta F, según la fórmula
        coeficientes = {
            'A': 1 + (3 / 4) * e**2 + (45 / 64) * e**4 + (175 / 256) * e**6 + (11025 / 16384) * e**8 + (43659 / 65536) * e**10,
            'B': (3 / 4) * e**2 + (15 / 16) * e**4 + (525 / 512) * e**6 + (2205 / 2048) * e**8 + (72765 / 65536) * e**10,
            'C': (15 / 64) * e**4 + (105 / 256) * e**6 + (2205 / 4096) * e**8 + (10395 / 16384) * e**10,
            'D': (35 / 512) * e**6 + (315 / 2048) * e**8 + (31185 / 131072) * e**10,
            'E': (315 / 16384) * e**8 + (3465 / 65536) * e**10,
            'F': (693 / 131072) * e**10
        }
        return coeficientes
    
    @staticmethod
    def calcular_longitud_arco_meridiano(delta_y: float, latitud_1: float, latitud_2: float, e: float):
        coeficientes = SistemaWGS84.calcular_coeficientes(e)
        
        resultado = coeficientes['A'] * delta_y
        potencias = [2, 4, 6, 8, 10]  # Las potencias que usamos en los senos

        for i, coef in enumerate(['B', 'C', 'D', 'E', 'F']):
            pot = potencias[i]
            termino_sin = math.sin(pot * latitud_2) - math.sin(pot * latitud_1)
            resultado -= (coeficientes[coef] / pot) * termino_sin
        
        s_AB = SistemaWGS84.a * (1 - e**2) * resultado
        return s_AB
    
    @staticmethod
    def graficar_elipsoide():
        # Generamos un conjunto de puntos para representar el elipsoide
        u = np.linspace(0, 2 * np.pi, 100)  # Ángulo azimutal
        v = np.linspace(0, np.pi, 100)      # Ángulo polar

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
            coord_y = SistemaWGS84.a * np.cos(y) * np.sin(x)
            coord_z = SistemaWGS84.b * np.sin(y)
            ax.scatter(coord_x, coord_y, coord_z, s=100)  # Graficar el punto
            coord_puntos.append((coord_x, coord_y, coord_z))  # Guardar las coordenadas

        return coord_puntos  # Devolver las coordenadas de los puntos
