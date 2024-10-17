import math
from Punto import Punto
from CoordenadaGMS import CoordenadaGMS
from Metodo_Gauss import MetodoGauss

def main():
    # Coordenadas iniciales en Grados, Minutos, Segundos (GMS)
    lat_inicial = CoordenadaGMS(40, 0, 0, 'N')   # 40° 0' 0" N
    lon_inicial = CoordenadaGMS(30, 0, 0, 'W')   # 30° 0' 0" W
    punto_inicial = Punto(lon_inicial, lat_inicial)

    # Distancia y azimut
    distancia = 100000  # Distancia en metros (100 km)
    azimut = math.radians(90)  # Azimut en radianes (90°)

    # Crear una instancia de MetodoGauss
    metodo_gauss = MetodoGauss()

    # Método directo: Calcular el punto final
    punto_final, azimut_inverso = metodo_gauss.metodo_directo(punto_inicial, azimut, distancia)

    # Imprimir resultados
    print(f"Punto final (directo): {punto_final}")
    print(f"Azimut inverso: {azimut_inverso}°")  # El azimut ya está en grados, no hace falta convertirlo


if __name__ == "__main__":
    main()