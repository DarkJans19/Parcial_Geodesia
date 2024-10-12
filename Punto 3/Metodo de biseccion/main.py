import math
import matplotlib.pyplot as plt
from Punto import Punto

def main():
    def calcular_direcciones(punto_a, dn, de, azimut):
        # Determinar si el punto P está más al Norte, Sur, Este o Oeste de A
        # Usamos el ángulo azimut y las diferencias de desplazamientos

        if 0 <= azimut < 45:
            # Primer cuadrante (Noreste): P está al Norte y al Este de A
            np = punto_a.y + dn
            ne = punto_a.x - de
        elif 90 <= azimut < 180:
            # Segundo cuadrante (NorOeste): P está al Norte y al Oeste de A
            np = punto_a.y + dn
            ne = punto_a.x - de
        elif 180 <= azimut < 270:
            # Tercer cuadrante (Suroeste): P está al Sur y al Oeste de A
            np = punto_a.y - dn
            ne = punto_a.x - de
        else:
            # Cuarto cuadrante (SurEste): P está al Norte y al Oeste de A
            np = punto_a.y - dn
            ne = punto_a.x + de

        return np, ne
    
    
    print("Punto A")
    # Ahora damos direcciones separadas para X y Y
    punto_a = Punto(101478.649, 101965.783, 'E', 'N', 63.25)
    print("Punto B")
    punto_b = Punto(101435.794, 101913.537, 'E', 'N', 90.0117)
    
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
    
    # Ajustar coordenadas de P según A y los desplazamientos (condicionales)
    np, ne = calcular_direcciones(punto_a, dn, de, AzAB)
    
    print("Norte de P:", np)
    print("Este de P:", ne)
    
    # Calcular los valores mínimos y máximos para los ejes X e Y
    fig, ax = plt.subplots()
    
    ax.ticklabel_format(style='plain', useOffset=False)
    
    # Establecemos los limites de la grafica
    ax.set_xlim([min(punto_a.x, punto_b.x, ne) - 20, max(punto_a.x, punto_b.x, ne) + 20])
    ax.set_ylim([min(punto_a.y, punto_b.y, np) - 20, max(punto_a.y, punto_b.y, np) + 20])

    # Graficamos los puntos
    ax.scatter(punto_a.x, punto_a.y, color='red', label='Punto A', zorder=5)
    ax.scatter(punto_b.x, punto_b.y, color='blue', label='Punto B', zorder=5)
    ax.scatter(ne, np, color='green', label='Punto P', zorder=5)

    # Aqui estamos colocando el nombre de los puntos
    ax.text(punto_a.x, punto_a.y, 'A', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='red')
    ax.text(punto_b.x, punto_b.y, 'B', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='blue')
    ax.text(ne, np, 'P', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='green')

    # Realizamos las lineas entre los puntos A y B y P
    ax.plot([punto_a.x, punto_b.x], [punto_a.y, punto_b.y], color='blue', label='Línea entre A y B')
    ax.plot([punto_a.x, ne], [punto_a.y, np], color='red', label='Línea entre A y P')
    ax.plot([punto_b.x, ne], [punto_b.y, np], color='black', label='Línea entre B y P')

    # Realizamos las lineas de proyeccion
    ax.plot([punto_a.x, punto_b.x], [punto_b.y, punto_b.y], color='orange', linestyle='--', label='Proyección horizontal AB')
    ax.plot([punto_a.x, punto_a.x], [punto_a.y, punto_b.y], color='orange', linestyle='--', label='Proyección vertical AB')
    ax.plot([punto_a.x, ne], [np, np], color='brown', linestyle='--', label='Proyección horizontal AP')
    ax.plot([punto_a.x, punto_a.x], [punto_a.y, np], color='brown', linestyle='--', label='Proyección vertical AP')

    # Nos encargamos de decorar un poco la grafica 
    ax.set_xlabel('Coordenada X')
    ax.set_ylabel('Coordenada Y')
    ax.set_title('Gráfica de Puntos A, B y P con Proyecciones')
    ax.legend()

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()