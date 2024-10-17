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
    def calcular_valor_interno_area(latitud, e):
        ajuste_excentricidad = 1 - (pow(e, 2) * pow(math.sin(latitud), 2))
        sen_angulo = math.sin(latitud)
        print("Sen_angulo", sen_angulo)
        print("ajuste_excentricidad:", ajuste_excentricidad)
        parte_1 = sen_angulo/(2 * ajuste_excentricidad)
        print("parte_1", parte_1)
        
        # Parte 2
        parte_2_numerador = (e * sen_angulo) + 1
        print("parte_2_numerador: ", parte_2_numerador)
        parte_2_denominador = abs((e * sen_angulo) - 1)
        print("Parte_2_denominador:", parte_2_denominador) 
        parte_2 = parte_2_numerador/parte_2_denominador
        print("parte_2", parte_2)
        logaritmo = math.log(parte_2)
        print("logaritmo", logaritmo)
        parte_2 = logaritmo / (4 * e)
        print("parte_2:", parte_2)
        return parte_1 + parte_2
    
    @staticmethod
    def calcular_cuadrilatero(delta_x, area_1, area_2):
        parte_1 = pow(SistemaWGS84.b, 2) * delta_x    
        print(parte_1)
        area_total = area_1 - area_2
        print("area total: ", area_total)
        area_cuadrilatero = parte_1 * area_total
        return area_cuadrilatero
    
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