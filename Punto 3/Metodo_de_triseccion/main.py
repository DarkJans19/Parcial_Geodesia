from Punto import Punto
from CoordenadaGMS import CoordenadaGMS

def main():
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

    ep, ne = punto_a.coordenadas(punto_b, punto_c, k1, k2, k3)
    print("ep", ep)
    print("ne", ne)

if __name__ == "__main__":
    main()