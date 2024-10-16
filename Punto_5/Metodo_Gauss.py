from Punto import Punto
from CoordenadaGMS import CoordenadaGMS
import math

class MetodoGauss:
    def __init__(self, radio_tierra=6378137):
        self.radio_tierra = radio_tierra

    def metodo_directo(self, punto_inicial: Punto, azimut: float, distancia: float):
        lat1 = punto_inicial.y.convertir_a_radianes()
        lon1 = punto_inicial.x.convertir_a_radianes()

        lat_media = lat1

        delta_lat = distancia * math.cos(azimut) / self.radio_tierra
        lat2 = lat1 + delta_lat

        delta_lon = (distancia * math.sin(azimut)) / (self.radio_tierra * math.cos(lat_media))
        lon2 = lon1 + delta_lon

        nueva_latitud = self.convertir_a_gms(lat2, 'N' if lat2 >= 0 else 'S')
        nueva_longitud = self.convertir_a_gms(lon2, 'E' if lon2 >= 0 else 'W')
        
        return Punto(nueva_longitud, nueva_latitud)

    def metodo_inverso(self, punto_a: Punto, punto_b: Punto):
        lat1 = punto_a.y.convertir_a_radianes()
        lon1 = punto_a.x.convertir_a_radianes()
        lat2 = punto_b.y.convertir_a_radianes()
        lon2 = punto_b.x.convertir_a_radianes()

        lat_media = (lat1 + lat2) / 2

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        distancia = math.sqrt((delta_lat * self.radio_tierra)**2 + 
                              (delta_lon * self.radio_tierra * math.cos(lat_media))**2)
        
        azimut = math.atan2(delta_lon * math.cos(lat_media), delta_lat)
        
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

