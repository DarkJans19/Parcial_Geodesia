import math
from CoordenadaGMS import CoordenadaGMS
from punto import Punto
from SistemaWGS84 import SistemaWGS84

def main():   
    # Calcular la excentricidad
    e = SistemaWGS84.calcular_excentricidad()

    # Acceder a las constantes del sistema WGS84
    a = SistemaWGS84.a
    b = SistemaWGS84.b
    print(f"Las constantes del sistema son {a} y {b} y la excentricidad es {e}")
    
    # Coordenadas x de ambos puntos
    punto_a_x = CoordenadaGMS(80, 20, 0, 'E')
    punto_b_x = CoordenadaGMS(95, 15, 0, 'E')

    # Coordenadas y de ambos puntos
    punto_a_y = CoordenadaGMS(10, 25, 0, 'S')
    punto_b_y = CoordenadaGMS(10, 25, 0, 'S')
    
    # Juntamos ambas coordenadas 
    punto_1 = Punto(punto_a_x, punto_a_y)
    punto_2 = Punto(punto_b_x, punto_b_y)
    
    # Convertimos las coordenadas y de los puntos a radianes
    punto_a_y = punto_a_y.convertir_a_radianes()
    print("punto ay:", punto_a_y)
    
    # Calculamos la diferencia de coordenadas x entre los puntos
    delta_x = punto_2.x.diferencia_coordenada_x(punto_1.x)
    print("delta_x:", delta_x)

    longitud_arco_paralelo = SistemaWGS84.calcular_longitud_arco_paralelo(delta_x, punto_a_y,e)
    print("Longitud_arco_paralelo:", longitud_arco_paralelo)
if __name__ == "__main__":
    main()