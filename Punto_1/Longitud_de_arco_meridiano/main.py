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


    # Podemos convertir las coordenadas este oeste y las usamos para calcular el ejercicio
    latitud_1 = punto_a_y.convertir_a_radianes()
    latitud_2 = punto_b_y.convertir_a_radianes()
    
    longitud_1 = punto_a_x.convertir_a_radianes()
    
    # Calculamos la diferencia de coordenadas x entre los puntos
    print("latitud_1:", latitud_1)
    print("latitud_2:", latitud_2)
    print("longitud_1:", longitud_1)
    
    # Calcular delta_y (la diferencia de latitudes)
    delta_y = latitud_1 - latitud_2
    
    # Calcular la longitud del arco de meridiano
    longitud_arco_meridiano = SistemaWGS84.calcular_longitud_arco_meridiano(delta_y, latitud_1, latitud_2, e)
    
    print(f"Longitud de arco de meridiano: {longitud_arco_meridiano:.2f} metros")
    
    """
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
    labels = ['A', 'B']  # Etiquetas para los puntos
    
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
    """
    
if __name__ == "__main__":
    main()
