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
    
    """ 
    Tomando la formula del cuadrilatero suponiendo que 
    AD = BC
    Y que AB = CD = L
    """
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