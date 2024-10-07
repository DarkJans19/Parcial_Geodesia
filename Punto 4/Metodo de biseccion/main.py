import math
import matplotlib.pyplot as plt
from Punto import Punto

def main():
    print("Punto A")
    # En caso de que se quieran puntos en especifico se pueden reemplazar los valores de la siguiente manera
    # punto_a = Punto(float(input()), float(input()), float(input()))
    punto_a = Punto(101478.649, 101965.783, 63.25)
    print("Punto B")
    punto_b = Punto(101435.794, 101913.537, 90.0117)
    
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
    print("dn:", dn)
    de = distancia_ap * math.sin(math.radians(azimut))
    print("de", de)
    
    # Ajustar coordenadas según el cuadrante
    np = punto_a.y + dn 
    ne = punto_a.x - de
    
    print("Norte de P:", np)
    print("Este de P:", ne)
    
    # Calcular los valores mínimos y máximos para los ejes X e Y para que sea mas facil graficar en dado caso
    # Puede que los limites queden disparejos y la grafica se vea extremadamente rara
    x_min = min(punto_a.x, punto_b.x, np) - 50  # Restamos 50 para margen
    x_max = max(punto_a.x, punto_b.x, np) + 50  # Sumamos 50 para margen
    y_min = min(punto_a.y, punto_b.y, ne) - 50  # Restamos 50 para margen
    y_max = max(punto_a.y, punto_b.y, ne) + 50  # Sumamos 50 para margen

    # Graficamos todo
    plt.figure(figsize=(12, 8))

    # Línea entre A y B
    plt.plot([punto_a.x, punto_b.x], [punto_a.y, punto_b.y], marker='o', color='b', label='Línea entre A y B')

    # Línea entre A y P
    plt.plot([punto_a.x, np], [punto_a.y, ne], marker='o', color='r', label='Línea entre A y P')

    # Proyecciones verticales y horizontales para la línea entre A y B
    plt.plot([punto_a.x, punto_a.x], [punto_a.y, punto_b.y], linestyle='--', color='g', label='Proyección vertical AB')  # Vertical
    plt.plot([punto_a.x, punto_b.x], [punto_b.y, punto_b.y], linestyle='--', color='g', label='Proyección horizontal AB')  # Horizontal

    # Proyecciones verticales y horizontales para la línea entre A y P
    plt.plot([punto_a.x, punto_a.x], [punto_a.y, ne], linestyle='--', color='orange', label='Proyección vertical AP')  # Vertical
    plt.plot([punto_a.x, np], [ne, ne], linestyle='--', color='orange', label='Proyección horizontal AP')  # Horizontal

    # Etiquetas para los puntos
    plt.text(punto_a.x, punto_a.y, 'A', fontsize=12, ha='right')
    plt.text(punto_b.x, punto_b.y, 'B', fontsize=12, ha='right')
    plt.text(np, ne, 'P', fontsize=12, ha='right')

    # Ajustamos los limites a partir de lo que hicimos un poco mas arriba
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Esta parte solo hace que la grafica se vea un poco mas bonita
    plt.title('Gráfica de Puntos A, B y P con Proyecciones')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
