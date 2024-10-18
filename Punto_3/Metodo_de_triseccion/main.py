from Punto import Punto
from CoordenadaGMS import CoordenadaGMS
import matplotlib.pyplot as plt

def main():
    def graficar_puntos(punto_a, punto_b, punto_c, punto_p):
        # Extraemos las coordenadas de los puntos
        x_vals = [punto_a.x, punto_b.x, punto_c.x, punto_p[0]]  # Coordenadas x (ep)
        y_vals = [punto_a.y, punto_b.y, punto_c.y, punto_p[1]]  # Coordenadas y (ne)

        # Etiquetas para los puntos
        labels = ['A', 'B', 'C', 'P']
        
        # Graficamos los puntos
        plt.figure()
        plt.plot(x_vals, y_vals, 'bo')  # 'bo' significa puntos azules
        for i, label in enumerate(labels):
            plt.text(x_vals[i], y_vals[i], label, fontsize=12, ha='right')

        # Conectar los puntos con líneas
        plt.plot([punto_a.x, punto_b.x], [punto_a.y, punto_b.y], 'g--', label='Línea A-B')
        plt.plot([punto_b.x, punto_c.x], [punto_b.y, punto_c.y], 'g--', label='Línea B-C')
        plt.plot([punto_c.x, punto_a.x], [punto_c.y, punto_a.y], 'g--', label='Línea C-A')

        # Conectar el nuevo punto P con líneas
        plt.plot([punto_a.x, punto_p[0]], [punto_a.y, punto_p[1]], 'r-', label='Línea A-P')
        plt.plot([punto_b.x, punto_p[0]], [punto_b.y, punto_p[1]], 'b-', label='Línea B-P')
        plt.plot([punto_c.x, punto_p[0]], [punto_c.y, punto_p[1]], 'p-', label='Línea C-P')

        # Agregar detalles a la gráfica
        plt.xlabel('Coordenadas X')
        plt.ylabel('Coordenadas Y')
        plt.title('Gráfico de Puntos A, B, C y P calculado')
        plt.grid(True)
        plt.legend()
        plt.show()
        
    # Puntos
    print("Punto A")
    coord_gms_a = CoordenadaGMS(63, 15, 0)  # Ejemplo de un ángulo en GMS
    punto_a = Punto(101478.649, 101965.783, coord_gms_a, 'E', 'N')
    
    print("Punto B")
    coord_gms_b = CoordenadaGMS(90, 0, 42)  # Ejemplo de otro ángulo en GMS
    punto_b = Punto(101435.794, 101913.537, coord_gms_b, 'E', 'N')
    
    print("Punto C") 
    coord_gms_c = CoordenadaGMS(75, 30, 15)  # Ejemplo de otro ángulo en GMS
    punto_c = Punto(101400.000, 101900.000, coord_gms_c, 'E', 'N')

    # Puedes ahora usar el método de distancia o ángulo, por ejemplo:
    distancia = punto_a.distancia(punto_b)
    print("Distancia entre A y B:", distancia)

    x, y, z = punto_a.angulo(punto_b, punto_c)
    print("x:", x)
    print("y:", y)
    print("z:", z)
    
    k1 = punto_a.constantes(x)
    k2 = punto_b.constantes(y)
    k3 = punto_c.constantes(z)
    print("K1:", k1)
    print("k2", k2)
    print("k3", k3)

    # Calculamos coordenadas del punto P (ep, ne)
    ep, ne = punto_a.coordenadas(punto_b, punto_c, k1, k2, k3)
    print("Coordenadas de P: ep =", ep, ", ne =", ne)

    # Graficar los puntos
    graficar_puntos(punto_a, punto_b, punto_c, (ep, ne))

if __name__ == "__main__":
    main()