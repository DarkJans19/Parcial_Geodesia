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

    def metodo_directo(self, punto_inicial: Punto, azimut: float, distancia: float):
        # Convertir las coordenadas iniciales a radianes
        lat1 = punto_inicial.y.convertir_a_radianes()  # Latitud en radianes
        lon1 = punto_inicial.x.convertir_a_radianes()  # Longitud en radianes

        # Calcular el radio efectivo de la Tierra basado en la latitud inicial
        radio_efectivo = calcular_radio_efectivo(math.degrees(lat1))

        # Calcular el cambio en latitud y longitud
        delta_lat = distancia * math.cos(azimut) / radio_efectivo
        lat2 = lat1 + delta_lat

        delta_lon = (distancia * math.sin(azimut)) / (calcular_radio_efectivo(math.degrees(lat2)) * math.cos(lat2))
        lon2 = lon1 + delta_lon

        # Forzar la longitud según la dirección original
        if punto_inicial.x.direccion == 'W':
            lon2 = -abs(lon2)  # Asegurarse de que sea negativo
        elif punto_inicial.x.direccion == 'E':
            lon2 = abs(lon2)   # Asegurarse de que sea positivo
        
        # Calcular el azimut inverso (en grados)
        azimut_inverso = (math.degrees(azimut) + 180) % 360

        # Convertir los resultados de radianes a GMS (Grados, Minutos, Segundos)
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
