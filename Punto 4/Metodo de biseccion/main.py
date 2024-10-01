import math
import matplotlib.pyplot as plt
from Punto import Punto

def main():
    print("Punto A")
    punto_a = Punto(101965.783, 101478.649, 63.25)
    print("Punto B")
    punto_b = Punto(101913.537, 101435.794, 90.0117)
    
    distancia = punto_a.distancia(punto_b)
    print("Distancia entre dos puntos: ", distancia)
    AzAB = punto_a.calcular_AzAB(punto_b)
    print("Ángulo entre A y B", AzAB)
    azimut = punto_a.calcular_azimut(punto_b)
    print("Azimut entre A y la recta AB", azimut)
    gamma = punto_a.calcular_gamma(punto_b)
    print("Gamma de P es: ", gamma)
    
    # Hallamos los valores del punto P
    distancia_ap = punto_a.distancia_punto_P(punto_b, gamma)
    print("Distancia AP", distancia_ap)
    
    # Cálculo de Norte (dn) y Este (de) de P
    dn = distancia_ap * math.cos(math.radians(azimut))
    de = distancia_ap * math.sin(math.radians(azimut))
    
    # Ajustar coordenadas según el cuadrante
    np = punto_a.y + dn 
    ne = punto_a.x - de
    
    print("Norte de P:", np)
    print("Este de P:", ne)
    
    # Graficar
    plt.figure(figsize=(12, 8))  # Aumenta el tamaño de la figura
    plt.plot([punto_a.x, punto_b.x], [punto_a.y, punto_b.y], marker='o', color='b', label='Línea entre A y B')
    plt.plot([punto_a.x, np], [punto_a.y, ne], marker='o', color='r', label='Línea entre A y P')  # Línea de A a P
    plt.text(punto_a.x, punto_a.y, 'A', fontsize=12, ha='right')
    plt.text(punto_b.x, punto_b.y, 'B', fontsize=12, ha='right')
    plt.text(np, ne, 'P', fontsize=12, ha='right')  # Etiqueta para P

    # Ajustar límites de los ejes
    plt.xlim(101900, 102000)  # Ajusta según tus datos
    plt.ylim(101400, 101500)  # Ajusta según tus datos

    plt.title('Gráfica de Puntos A, B y P')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
