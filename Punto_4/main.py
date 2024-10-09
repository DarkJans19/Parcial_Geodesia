from CoordenadaGMS import CoordenadaGMS
from Mercator import Mercator
from punto import Punto

def main():
    # Coordenadas del punto
    latitud = CoordenadaGMS(45, 0, 0, 'N')
    longitud = CoordenadaGMS(10, 0, 0, 'E')
    longitud_referencia = CoordenadaGMS(0, 0, 0, 'E')  # Meridiano central de referencia (Greenwich)

    # Método directo de Mercator: Convertimos de latitud/longitud a coordenadas planas (x, y)
    x, y = Mercator.metodo_directo(latitud, longitud, longitud_referencia)
    print(f"Coordenadas planas (x, y) calculadas: {x}, {y}")

    # Método inverso de Mercator: Convertir x, y de vuelta a latitud/longitud para comprobar el resultado 
    latitud_inv, longitud_inv = Mercator.metodo_inverso(x, y, longitud_referencia)
    print(f"Coordenadas geográficas inversas: Latitud: {latitud_inv}, Longitud: {longitud_inv}")

    # Prueba con valores de x, y introducidos por el usuario
    x_nuevo = 1.5  # Ejemplo de un valor de x proporcionado por el usuario
    y_nuevo = 0.8  # Ejemplo de un valor de y proporcionado por el usuario
    latitud_nueva, longitud_nueva = Mercator.metodo_inverso(x_nuevo, y_nuevo, longitud_referencia)
    print(f"Coordenadas geográficas desde (x={x_nuevo}, y={y_nuevo}): Latitud: {latitud_nueva}, Longitud: {longitud_nueva}")

if __name__ == "__main__":
    main()
