from Punto import Punto
from CoordenadaGMS import CoordenadaGMS
from Metodo_Gauss import MetodoGauss

def main():
    # Ejemplo de coordenadas iniciales en Grados, Minutos, Segundos (GMS)
    # Punto A (Latitud y Longitud)
    lat_inicial = CoordenadaGMS(40, 0, 0, 'N')   # 40°0'0" N
    lon_inicial = CoordenadaGMS(30, 0, 0, 'W')   # 30°0'0" W
    punto_inicial = Punto(lon_inicial, lat_inicial)

    # Crear una instancia de MetodoGauss
    metodo_gauss = MetodoGauss()

    # Definimos el segundo punto B
    lat_final = CoordenadaGMS(41, 0, 0, 'N')   # 41°0'0" N
    lon_final = CoordenadaGMS(31, 0, 0, 'W')  # 31°0'0" W
    punto_b = Punto(lon_final, lat_final)

    # Método inverso: Calcular azimut y distancia entre punto A y B
    azimut_inverso, distancia_inversa = metodo_gauss.metodo_inverso(punto_inicial, punto_b)
    print(f"Azimut (inverso): {azimut_inverso}°")
    print(f"Distancia (inverso): {distancia_inversa / 1000} km")  # Convertir metros a kilómetros

if __name__ == "__main__":
    main()
