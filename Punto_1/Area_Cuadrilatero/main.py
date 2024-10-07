import math
from CoordenadaGMS import CoordenadaGMS
from punto import punto

def main():   
    # Constantes, al estar utilizando el sistema WSG84 utilizamos el semieje mayor y menor y calculamos la excentricidad
    a = 6378137
    b = 6356752.314245
    def excentricidad(semieje_mayor: float, semieje_menor):
        division = pow(semieje_mayor,2) / pow(semieje_menor,2)
        e = math.sqrt(pow(semieje_mayor,2) - division)
        return e
    
    # Coordenadas x de ambos puntos
    punto_a_x = CoordenadaGMS(80, 20, 0, 'E')
    punto_b_x = CoordenadaGMS(95, 15, 0, 'S')

    # Coordenadas y de ambos puntos
    punto_a_y = CoordenadaGMS(10, 25, 0, 'S')
    punto_b_y = CoordenadaGMS(10, 25, 0, 'S')
    
    # Pasamos todas las coordenadas a un array para que sea mas facil pasarlas a radianes y manejar los valores 
    # Juntamos ambas coordenadas 
    punto_1 = punto(punto_a_x, punto_a_y)
    punto_2 = punto(punto_b_x, punto_b_y)
    
    puntos = [punto_1, punto_2]
    for punto in puntos:
        punto.x.convertir_a_radianes()
if __name__ == "__main__":
    main()