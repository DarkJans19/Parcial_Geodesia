from Punto import Punto
from CoordenadaGMS import CoordenadaGMS
from Metodo_Gauss import MetodoGauss
import math

def main():
    # Ejemplo de coordenadas iniciales en Grados, Minutos, Segundos (GMS)
    # Punto inicial (Latitud y Longitud)
    lat_inicial = CoordenadaGMS(4, 35, 0, 'N')   # 4°35'0" N
    lon_inicial = CoordenadaGMS(74, 4, 0, 'W')   # 74°4'0" W
    punto_inicial = Punto(lon_inicial, lat_inicial)

    # Distancia y azimut
    distancia = 5000  # Distancia en metros (5 km)
    azimut = math.radians(45)  # Azimut en radianes (45°)

    # Crear una instancia de MetodoGauss
    metodo_gauss = MetodoGauss()

    # Método directo: Calcular el punto final
    punto_final = metodo_gauss.metodo_directo(punto_inicial, azimut, distancia)
    print(f"Punto final (directo): {punto_final}")

    # Ahora realizamos el método inverso
    # Definimos un segundo punto para calcular azimut y distancia
    lat_final = CoordenadaGMS(4, 37, 0, 'N')   # 4°37'0" N
    lon_final = CoordenadaGMS(74, 5, 30, 'W')  # 74°5'30" W
    punto_b = Punto(lon_final, lat_final)

    # Método inverso: Calcular azimut y distancia entre punto A y B
    azimut_inverso, distancia_inversa = metodo_gauss.metodo_inverso(punto_inicial, punto_b)
    print(f"Azimut (inverso): {azimut_inverso}°")
    print(f"Distancia (inverso): {distancia_inversa} metros")

if __name__ == "__main__":
    main()
