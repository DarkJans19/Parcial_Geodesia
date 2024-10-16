import numpy as np
import matplotlib.pyplot as plt
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
    punto_a_y = CoordenadaGMS(20, 30, 0, 'N')
    punto_b_y = CoordenadaGMS(20, 30, 0, 'N')
    
    # Juntamos todas las coordenadas 
    punto_1 = Punto(punto_a_x, punto_a_y)
    punto_2 = Punto(punto_b_x, punto_b_y)
    
    print(punto_1)
    print(punto_2)

    
    # Convertimos las coordenadas y de los puntos a radianes
    punto_a_x = punto_a_x.convertir_a_radianes()
    punto_a_y = punto_a_y.convertir_a_radianes()
    punto_b_x = punto_b_x.convertir_a_radianes()
    punto_b_y = punto_b_y.convertir_a_radianes()
    
    # Podemos convertir las coordenadas este oeste y las usamos para calcular el ejercicio
    latitud_1 = punto_a_y
    
    longitud_1 = punto_a_x
    longitud_2 = punto_b_x
    
    # Calculamos la diferencia de coordenadas x entre los puntos
    print("latitud_1:", latitud_1)
    print("longitud_1:", longitud_1)
    print("longitud_2:", longitud_2)
    
    delta_x = punto_2.x.diferencia_coordenada(punto_1.x)
    print("delta_x:", delta_x)
    
    # Podemos calcular la longitud del arco de paralelo y meridiano entre dos puntos
    longitud_arco_paralelo = SistemaWGS84.calcular_longitud_arco_paralelo(delta_x, latitud_1, e)
    print("Longitud arco paralelo:", longitud_arco_paralelo)
    
    # Grafica
    puntos = [punto_1, punto_2]

    # Graficar el elipsoide
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x, y, z = SistemaWGS84.graficar_elipsoide()  # Llamar con a y b
    ax.plot_surface(x, y, z, color='b', alpha=0.3)
    
    # Graficar los puntos y obtener sus coordenadas cartesianas
    coord_puntos = SistemaWGS84.graficar_puntos(ax, puntos)

    # Etiquetar los puntos con letras A, B, C, D
    labels = ['A', 'B', 'C', 'D']  # Etiquetas para los puntos
    
    for i, label in enumerate(labels):
        ax.text(coord_puntos[i][0], coord_puntos[i][1], coord_puntos[i][2], label, color='black', fontsize=12)

    for i, label in enumerate(labels):
        ax.text(coord_puntos[i][0], coord_puntos[i][1], coord_puntos[i][2], label, color='black', fontsize=12)

    
    # Unir los puntos para formar un cuadrilátero
    indices = [0, 1, 3, 2, 0]  # Asegúrate de que los puntos están en el orden correcto

    for i in range(len(indices) - 1):
        x_values = [coord_puntos[indices[i]][0], coord_puntos[indices[i + 1]][0]]
        y_values = [coord_puntos[indices[i]][1], coord_puntos[indices[i + 1]][1]]
        z_values = [coord_puntos[indices[i]][2], coord_puntos[indices[i + 1]][2]]
        ax.plot(x_values, y_values, z_values, color='r', linewidth=2)
    
    # Etiquetas
    ax.set_xlabel('X (Eje E-O)')
    ax.set_ylabel('Y (Eje N-S)')
    ax.set_zlabel('Z (Altura)')
    ax.set_title('Elipsoide de la Tierra con puntos y líneas conectadas')
    plt.show()
    
if __name__ == "__main__":
    main()
