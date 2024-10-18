import numpy as np
import matplotlib.pyplot as plt
from CoordenadaGMS import CoordenadaGMS
from Punto import Punto
from SistemaWGS84 import SistemaWGS84

def main():   
    # Calcular la excentricidad
    e = SistemaWGS84.calcular_excentricidad()

    # Acceder a las constantes del sistema WGS84
    a = SistemaWGS84.a
    b = SistemaWGS84.b
    print(f"Las constantes del sistema son {a} y {b} y la excentricidad es {e}")
    
    # Coordenadas x de ambos puntos
    punto_a_x = CoordenadaGMS(3.21666, 0, 0, 'E')
    punto_b_x = CoordenadaGMS(3.21666, 0, 0, 'E')

    # Coordenadas en grados, minutos y segundos
    punto_a_y = CoordenadaGMS(51, 12, 0, 'N')  # Latitud 51.2°
    punto_b_y = CoordenadaGMS(50, 15, 0, 'N')  # Latitud 50.25°
    
    # Juntamos todas las coordenadas 
    punto_1 = Punto(punto_a_x, punto_a_y)
    punto_2 = Punto(punto_b_x, punto_b_y)
    
    print(punto_1)
    print(punto_2)

    # Convertir las coordenadas a radianes
    latitud_1 = punto_a_y.convertir_a_radianes()
    latitud_2 = punto_b_y.convertir_a_radianes()
    
    # Calcular la diferencia de coordenadas
    delta_y = latitud_1 - latitud_2
    
    # Calcular la longitud del arco de meridiano
    longitud_arco_meridiano = SistemaWGS84.calcular_longitud_arco_meridiano(delta_y, latitud_1, latitud_2, e)
    print(f"Longitud de arco de meridiano: {longitud_arco_meridiano:.2f} metros")
    
    # Graficar
    puntos = [punto_1, punto_2]

    # Graficar el elipsoide
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar el elipsoide
    x, y, z = SistemaWGS84.graficar_elipsoide()  # Llamar con a y b
    ax.plot_surface(x, y, z, color='b', alpha=0.3)
    
    # Graficar los puntos y obtener sus coordenadas cartesianas
    coord_puntos = SistemaWGS84.graficar_puntos(ax, puntos)

    # Etiquetar los puntos con letras A, B
    labels = ['A', 'B']  # Etiquetas para los puntos
    for i, label in enumerate(labels):
        ax.text(coord_puntos[i][0], coord_puntos[i][1], coord_puntos[i][2], label, color='black', fontsize=12)

    # Conectar los puntos con una línea
    ax.plot([coord_puntos[0][0], coord_puntos[1][0]], 
            [coord_puntos[0][1], coord_puntos[1][1]], 
            [coord_puntos[0][2], coord_puntos[1][2]], color='r', linewidth=2)
    
    # Configuración de etiquetas
    ax.set_xlabel('X (Eje E-O)')
    ax.set_ylabel('Y (Eje N-S)')
    ax.set_zlabel('Z (Altura)')
    ax.set_title('Elipsoide de la Tierra con puntos y línea conectada')

    # Ajustar límites de los ejes para hacer los puntos más visibles
    ax.set_xlim([-6500000, 6500000])  # Limites en el eje X
    ax.set_ylim([-6500000, 6500000])  # Limites en el eje Y
    ax.set_zlim([-6500000, 6500000])  # Limites en el eje Z
    
    plt.show()
    
if __name__ == "__main__":
    main()
