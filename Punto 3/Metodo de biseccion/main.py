import math
import matplotlib.pyplot as plt
from Punto import Punto

def main():
    print("Punto A")
    # En caso de que se quieran puntos en especifico se pueden reemplazar los valores de la siguiente manera
    # punto_a = Punto(float(input()), float(input()), float(input()))
    punto_a = Punto(101478.649, 101965.783, 'N',63.25)
    print("Punto B")
    punto_b = Punto(101435.794, 101913.537, 'E', 90.0117)
    
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
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    
    # Desactivar notación científica para los ejes
    ax.ticklabel_format(style='plain', useOffset=False)

    # Ajustar los límites del gráfico
    ax.set_xlim([min(punto_a.x, punto_b.x, ne) - 20, max(punto_a.x, punto_b.x, ne) + 20])
    ax.set_ylim([min(punto_a.y, punto_b.y, np) - 20, max(punto_a.y, punto_b.y, np) + 20])

    # Graficar los puntos A, B y P
    ax.scatter(punto_a.x, punto_a.y, color='red', label='Punto A', zorder=5)
    ax.scatter(punto_b.x, punto_b.y, color='blue', label='Punto B', zorder=5)
    ax.scatter(ne, np, color='green', label='Punto P', zorder=5)

    # Añadir etiquetas a los puntos A, B y P
    ax.text(punto_a.x, punto_a.y, 'A', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='red')
    ax.text(punto_b.x, punto_b.y, 'B', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='blue')
    ax.text(ne, np, 'P', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='green')

    # Dibujar las líneas entre los puntos A y B, y A y P
    ax.plot([punto_a.x, punto_b.x], [punto_a.y, punto_b.y], color='blue', label='Línea entre A y B')
    ax.plot([punto_a.x, ne], [punto_a.y, np], color='red', label='Línea entre A y P')  
    ax.plot([punto_b.x, ne], [punto_b.y, np], color = 'black', label = 'Linea entre B y P')

    # Dibujar las proyecciones verticales y horizontales con colores diferentes
    ax.plot([punto_a.x, punto_b.x], [punto_b.y, punto_b.y], color='orange', linestyle='--', label='Proyección horizontal AB')
    ax.plot([punto_a.x, punto_a.x], [punto_a.y, punto_b.y], color='orange', linestyle='--', label='Proyección vertical AB')
    ax.plot([punto_a.x, ne], [np, np], color='brown', linestyle='--', label='Proyección horizontal AP')
    ax.plot([punto_a.x, punto_a.x], [punto_a.y, np], color='brown', linestyle='--', label='Proyección vertical AP')

    # Añadir etiquetas y leyenda
    ax.set_xlabel('Coordenada X')
    ax.set_ylabel('Coordenada Y')
    ax.set_title('Gráfica de Puntos A, B y P con Proyecciones')
    ax.legend()

    # Mostrar la gráfica con una cuadrícula
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()
