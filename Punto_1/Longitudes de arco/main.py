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
    punto_a_x = CoordenadaGMS(80,20, 0, 'E')
    punto_b_x = CoordenadaGMS(95, 15, 0, 'E')
    punto_c_x = CoordenadaGMS(80, 20, 0, 'E')
    punto_d_x = CoordenadaGMS(95, 15, 0, 'E')

    # Coordenadas y de ambos puntos
    punto_a_y = CoordenadaGMS(20, 30, 0, 'N')
    punto_b_y = CoordenadaGMS(20, 30, 0, 'N')
    punto_c_y = CoordenadaGMS(10, 25, 0, 'S')
    punto_d_y = CoordenadaGMS(10, 25, 0, 'S')
    
    # Juntamos todas las coordenadas 
    punto_1 = Punto(punto_a_x, punto_a_y)
    punto_2 = Punto(punto_b_x, punto_b_y)
    punto_3 = Punto(punto_c_x, punto_c_y)
    punto_4 = Punto(punto_d_x, punto_d_y)
    
    print(punto_1)
    print(punto_2)
    print(punto_3)
    print(punto_4)
    
    # Convertimos las coordenadas y de los puntos a radianes
    punto_a_x = punto_a_x.convertir_a_radianes()
    punto_a_y = punto_a_y.convertir_a_radianes()
    punto_b_x = punto_b_x.convertir_a_radianes()
    punto_b_y = punto_b_y.convertir_a_radianes()
    punto_c_x = punto_c_x.convertir_a_radianes()
    punto_c_y = punto_c_y.convertir_a_radianes()
    punto_d_x = punto_d_x.convertir_a_radianes()
    punto_d_y = punto_d_y.convertir_a_radianes()
    
    # Podemos convertir las coordenadas este oeste y las usamos para calcular el ejercicio
    latitud_1 = punto_a_y
    latitud_2 = punto_c_y
    
    longitud_1 = punto_a_x
    longitud_2 = punto_b_x
    
    # Calculamos la diferencia de coordenadas x entre los puntos
    # Para calcular la longitud del arco paralelo ir alternando entre el punto mayor y el punto menor
    print("latitud_1:", latitud_1)
    print("latitud_2:",latitud_2)
    print("longitud_1:", longitud_1)
    print("longitud_2:", longitud_2)
    
    delta_x = punto_4.x.diferencia_coordenada(punto_1.x)
    print("delta_x:", delta_x)
    
    delta_y = punto_1.y.diferencia_coordenada(punto_4.y)
    print("delta_y:",delta_y)
    
    suma_y = punto_1.y.suma_coordenada(punto_4.y)
    print("suma_y:",suma_y)
    
    # Podemos calcular la longitud del arco de paralelo y meridiano entre dos puntos
    longitud_arco_paralelo = SistemaWGS84.calcular_longitud_arco_paralelo(delta_x, latitud_1,e)
    print("Longitud arco paralelo:", longitud_arco_paralelo)
    longitud_arco_meridiano = SistemaWGS84.calcular_longitud_arco_meridiano(delta_y, suma_y, longitud_1, e)
    print("Longitud de arco meridiano:", longitud_arco_meridiano)
    
    # Calculamos el area del cuadrilatero
    area_1 = SistemaWGS84.calcular_valor_interno_area(abs(latitud_1), e)
    print("area 1:", area_1)
    area_2 = SistemaWGS84.calcular_valor_interno_area(abs(latitud_2), e)
    print("area_2:", area_2)
    area_cuadrilatero = SistemaWGS84.calcular_cuadrilatero(delta_x, area_1, area_2)
    print("Area del cuadrilátero:", area_cuadrilatero)
    
if __name__ == "__main__":
    main()