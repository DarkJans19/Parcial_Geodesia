import math
from CoordenadaGMS import CoordenadaGMS

class Mercator(CoordenadaGMS):
    @staticmethod
    def metodo_directo(latitud: CoordenadaGMS, longitud: CoordenadaGMS, longitud_referencia: CoordenadaGMS):
        """
        Método directo de Mercator para convertir latitud y longitud en coordenadas planas x e y.
        longitud_referencia es el meridiano central.
        """
        # Obtener latitud y longitud en radianes
        phi = latitud.convertir_a_radianes()
        lam = longitud.convertir_a_radianes()
        lam_0 = longitud_referencia.convertir_a_radianes()

        # Fórmulas de Mercator (simplificadas)
        x = lam - lam_0
        y = math.log(math.tan(math.pi / 4 + phi / 2))

        return x, y

    @staticmethod
    def metodo_inverso(x: float, y: float, longitud_referencia: CoordenadaGMS):
        """
        Método inverso de Mercator para convertir coordenadas planas (x, y) a latitud y longitud geográficas.
        Permite trabajar con cualquier par de x e y y un meridiano de referencia.
        """
        # Convertir y de coordenadas planas a phi (latitud en radianes)
        phi = 2 * math.atan(math.exp(y)) - math.pi / 2

        # Para la longitud, usamos x y el meridiano de referencia
        lam_0 = longitud_referencia.convertir_a_radianes()
        lam = x + lam_0

        # Convertir de radianes a grados decimales
        latitud = math.degrees(phi)
        longitud = math.degrees(lam)

        return latitud, longitud
