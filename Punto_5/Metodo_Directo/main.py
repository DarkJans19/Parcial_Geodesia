import math
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from Punto import Punto
from CoordenadaGMS import CoordenadaGMS
from Metodo_Gauss import MetodoGauss

# Función para convertir CoordenadaGMS a grados decimales y manejar correctamente el signo
def convertir_a_decimales(coordenada_gms):
    # Convertir GMS a grados decimales
    grados = coordenada_gms.grados + coordenada_gms.minutos / 60 + coordenada_gms.segundos / 3600

    # Solo corregir el signo si es necesario, dependiendo de la dirección
    if coordenada_gms.direccion in ['S', 'W'] and grados > 0:
        grados = -grados

    return grados


def graficar_mapa_colombia(punto_inicial, punto_final, ruta_shapefile):
    # Cargar el shapefile del mapa de Colombia utilizando geopandas
    colombia = gpd.read_file(ruta_shapefile)

    # Asegurarse de que el shapefile esté en WGS84 (EPSG:4326)
    if colombia.crs != "EPSG:4326":
        colombia = colombia.to_crs("EPSG:4326")

    # Verificar las coordenadas decimales antes de crear el punto geométrico
    x_inicial = convertir_a_decimales(punto_inicial.x)
    y_inicial = convertir_a_decimales(punto_inicial.y)
    x_final = convertir_a_decimales(punto_final.x)
    y_final = convertir_a_decimales(punto_final.y)

    print(f"Coordenadas iniciales (decimales): Longitud: {x_inicial}, Latitud: {y_inicial}")
    print(f"Coordenadas finales (decimales): Longitud: {x_final}, Latitud: {y_final}")

    # Crear un GeoDataFrame con los puntos inicial y final
    punto_inicial_geom = Point(x_inicial, y_inicial)
    punto_final_geom = Point(x_final, y_final)

    puntos_gdf = gpd.GeoDataFrame(geometry=[punto_inicial_geom, punto_final_geom], crs="EPSG:4326")

    # Crear la gráfica
    fig, ax = plt.subplots(figsize=(8, 8))
    colombia.plot(ax=ax, color='lightgreen', edgecolor='black')  # Graficar el mapa desde el shapefile
    puntos_gdf.plot(ax=ax, color='red', marker='o', markersize=50)  # Graficar los puntos

    # Etiquetas de los puntos
    for x, y, label in zip(puntos_gdf.geometry.x, puntos_gdf.geometry.y, ['Inicial', 'Final']):
        ax.text(x, y, label, fontsize=12, ha='right')

    plt.title('Puntos calculados en el mapa de Colombia (Sistema WGS84)')
    plt.show()

def main():
    # Coordenadas iniciales en Grados, Minutos, Segundos (GMS)
    lat_inicial = CoordenadaGMS(4, 35, 56, 'N')   # Ejemplo: Bogotá
    lon_inicial = CoordenadaGMS(74, 4, 51, 'W')   # Ejemplo: Bogotá
    punto_inicial = Punto(lon_inicial, lat_inicial)

    # Distancia y azimut
    distancia = 50000  # Distancia en metros (50 km)
    azimut = math.radians(45)  # Azimut en radianes (45°)

    # Crear una instancia de MetodoGauss
    metodo_gauss = MetodoGauss()

    # Método directo: Calcular el punto final
    punto_final, azimut_inverso = metodo_gauss.metodo_directo(punto_inicial, azimut, distancia)

    # Ruta a tu shapefile
    ruta_shapefile = r'Punto_4\Depto.shp'  # Reemplaza con la ruta correcta

    # Graficar el mapa con los puntos
    graficar_mapa_colombia(punto_inicial, punto_final, ruta_shapefile)

    # Imprimir resultados
    print(f"Punto final (directo): {punto_final}")
    print(f"Azimut inverso: {azimut_inverso}°")  # El azimut ya está en grados


if __name__ == "__main__":
    main()
