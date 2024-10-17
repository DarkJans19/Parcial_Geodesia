import math
from Punto import Punto
from CoordenadaGMS import CoordenadaGMS

class MetodoGauss:
    def __init__(self, a=6378137.0, b=6356752.314245):  # Parámetros del elipsoide (WGS84)
        self.a = a  # Radio ecuatorial
        self.b = b  # Radio polar
        self.f = (a - b) / a  # Aplanamiento
        self.e2 = 1 - (b ** 2 / a ** 2)  # Excentricidad cuadrada

    def radio_curvatura_meridiana(self, lat):
        """Radio de curvatura en el meridiano en función de la latitud."""
        sin_lat = math.sin(lat)
        M = self.a * (1 - self.e2) / math.pow(1 - self.e2 * sin_lat ** 2, 1.5)
        return M

    def radio_curvatura_vertical(self, lat):
        """Radio de curvatura en la normal (dirección vertical) en función de la latitud."""
        N = self.a / math.sqrt(1 - self.e2 * math.sin(lat) ** 2)
        return N

    def metodo_inverso(self, punto_a: Punto, punto_b: Punto):
        # Obtener latitud y longitud en radianes de ambos puntos
        lat1 = punto_a.y.convertir_a_radianes()
        lon1 = punto_a.x.convertir_a_radianes()
        lat2 = punto_b.y.convertir_a_radianes()
        lon2 = punto_b.x.convertir_a_radianes()

        # Latitud media
        lat_media = (lat1 + lat2) / 2

        # Diferencias de coordenadas
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        # Radios de curvatura en la latitud media
        M = self.radio_curvatura_meridiana(lat_media)
        N = self.radio_curvatura_vertical(lat_media)

        # Cálculo de las componentes A y B
        A = delta_lat * M
        B = delta_lon * N * math.cos(lat_media)

        # Cálculo de la distancia usando la fórmula S = sqrt(A^2 + B^2)
        distancia = math.sqrt(A**2 + B**2)

        # Cálculo del azimut usando la fórmula α = arctan(B / A)
        azimut = math.atan2(B, A)

        # Convertir azimut a grados
        azimut_grados = math.degrees(azimut)
        if azimut_grados < 0:
            azimut_grados += 360  # Corregimos para mantener el azimut en el rango [0, 360)

        return azimut_grados, distancia

    def convertir_a_gms(self, radianes, direccion):
        grados_totales = math.degrees(radianes)
        grados = int(grados_totales)
        minutos_decimales = abs(grados_totales - grados) * 60
        minutos = int(minutos_decimales)
        segundos = round((minutos_decimales - minutos) * 60, 2)  # Redondeamos los segundos a dos decimales
        
        return CoordenadaGMS(grados, minutos, segundos, direccion)
