# Metodo_Gauss.py
import math
from Punto import Punto
from CoordenadaGMS import CoordenadaGMS

# Constantes elipsoidales (WGS84)
A = 6378137.0  # Semieje mayor en metros
B = 6356752.3142  # Semieje menor en metros
E2 = (A**2 - B**2) / A**2  # Excentricidad al cuadrado

def calcular_radio_efectivo(latitud):
    """Calcula el radio efectivo de la Tierra en función de la latitud"""
    lat_rad = math.radians(latitud)
    sin_lat = math.sin(lat_rad)
    
    # Radio efectivo basado en el modelo elipsoidal
    R_efectivo = A * (1 - E2) / ((1 - E2 * sin_lat ** 2) ** (3 / 2))
    
    return R_efectivo  # El radio ya está en metros

class MetodoGauss:
    def __init__(self):
        pass

    def metodo_directo(self, punto_inicial: Punto, azimut: float, distancia: float, max_iteraciones=10, tolerancia=1e-6):
        lat1 = punto_inicial.y.convertir_a_radianes()  # Convertir latitud a radianes
        lon1 = punto_inicial.x.convertir_a_radianes()  # Convertir longitud a radianes

        # Inicializamos las variables de iteración
        lat2 = lat1
        lon2 = lon1

        for i in range(max_iteraciones):
            lat_inicial_degrees = math.degrees(lat2)  # Convertimos a grados para calcular el radio efectivo
            radio_efectivo = calcular_radio_efectivo(lat_inicial_degrees)

            # Calcular cambios en latitud y longitud con base en las fórmulas de Gauss
            delta_lat = distancia * math.cos(azimut) / radio_efectivo
            lat2_nueva = lat1 + delta_lat

            delta_lon = (distancia * math.sin(azimut)) / (calcular_radio_efectivo(math.degrees(lat2_nueva)) * math.cos(lat2_nueva))
            lon2_nueva = lon1 + delta_lon

            # Comprobar si la diferencia es menor que la tolerancia para detener el bucle
            if abs(lat2_nueva - lat2) < tolerancia and abs(lon2_nueva - lon2) < tolerancia:
                lat2 = lat2_nueva
                lon2 = lon2_nueva
                break

            # Actualizar latitud y longitud para la siguiente iteración
            lat2 = lat2_nueva
            lon2 = lon2_nueva

        # Calcular el azimut inverso usando la fórmula correcta
        azimut_original_grados = math.degrees(azimut)  # Convertir azimut a grados
        azimut_inverso = (azimut_original_grados + 180) % 360

        # Convertir los resultados de radianes a GMS
        nueva_latitud = self.convertir_a_gms(lat2, 'N' if lat2 >= 0 else 'S')
        nueva_longitud = self.convertir_a_gms(lon2, 'E' if lon2 >= 0 else 'W')
        
        return Punto(nueva_longitud, nueva_latitud), azimut_inverso

    def convertir_a_gms(self, radianes, direccion):
        # Convertir radianes a grados
        grados_totales = math.degrees(radianes)
        grados = int(grados_totales)
        minutos_decimales = abs(grados_totales - grados) * 60
        minutos = int(minutos_decimales)
        segundos = round((minutos_decimales - minutos) * 60, 2)  # Redondear a 2 decimales
        
        return CoordenadaGMS(grados, minutos, segundos, direccion)
