import math
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
    if 0 <= azimut < 180:  # Movimiento hacia el norte
        np = punto_a.y + dn  # Sumar dn
    else:  # Movimiento hacia el sur
        np = punto_a.y - dn  # Restar dn

    if 0 <= azimut < 90 or 270 < azimut < 360:  # Movimiento hacia el este
        ne = punto_a.x + de  # Sumar de
    else:  # Movimiento hacia el oeste
        ne = punto_a.x - de  # Restar de

    print("Norte de P:", np)
    print("Este de P:", ne)

if __name__ == "__main__":
    main()
