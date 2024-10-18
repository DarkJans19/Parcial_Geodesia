import math
from CoordenadaGMS import CoordenadaGMS

class Mercator_inverso(CoordenadaGMS):
    @staticmethod
    def metodo_inverso(x: float, y: float, longitud_referencia: CoordenadaGMS):
        """
        Método inverso de Mercator para convertir coordenadas planas (x, y) a latitud y longitud geográficas.
        """
        # Limitar el valor de y dentro de un rango manejable para evitar overflow en math.exp(y)
        if y > 7000000:
            y = 7000000
        elif y < -7000000:
            y = -7000000

        # Convertir y de coordenadas planas a phi (latitud en radianes)
        phi = 2 * math.atan(math.exp(y / 6378137)) - math.pi / 2

        # Para la longitud, usamos x y el meridiano de referencia
        lam_0 = longitud_referencia.convertir_a_radianes()
        lam = x / 6378137 + lam_0

        # Convertir de radianes a grados decimales
        latitud = math.degrees(phi)
        longitud = math.degrees(lam)

        return latitud, longitud

