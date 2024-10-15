import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from CoordenadaGMS import CoordenadaGMS
from Mercator import Mercator

def aplicar_mercator_directo(latitud, longitud, longitud_referencia):
    # Aplicar la proyección de Mercator (directo: lat/long -> X/Y)
    x, y = Mercator.metodo_directo(latitud, longitud, longitud_referencia)
    print(f"Proyección directa (Mercator) -> Latitud: {latitud.to_decimal()}, Longitud: {longitud.to_decimal()} -> X: {x}, Y: {y}")
    return x, y

def aplicar_mercator_inverso(x, y, longitud_referencia):
    # Aplicar el método inverso de Mercator (X/Y -> lat/long)
    latitud, longitud = Mercator.metodo_inverso(x, y, longitud_referencia)
    print(f"Proyección inversa (Mercator) -> X: {x}, Y: {y} -> Latitud: {latitud}, Longitud: {longitud}")
    return latitud, longitud

def main():
    # Cargar el shapefile del mapa de Colombia
    colombia = gpd.read_file(r"D:\Users\Jan Sanchez\Documents\Repositorios\Programacion\Tarea heidy\Punto_4\Depto.shp")

    # Verificar y establecer el CRS del shapefile
    if colombia.crs is None:
        colombia.set_crs(epsg=4326, inplace=True)  # Asignar CRS si no tiene
    else:
        colombia = colombia.to_crs(epsg=4326)  # Convertir al CRS WGS84

    # Definir los departamentos que pertenecen a la región Caribe y Pacífico
    caribe = ['La Guajira', 'Cesar', 'Magdalena', 'Atlántico', 'Bolívar', 'Sucre', 'Córdoba', 'San Andrés']
    pacifico = ['Chocó', 'Valle del Cauca', 'Cauca', 'Nariño']

    # Crear una nueva columna 'Region' en el GeoDataFrame para identificar Caribe y Pacífico
    colombia['Region'] = 'Interior'  # Inicializar como "Interior"
    colombia.loc[colombia['DeNombre'].isin(caribe), 'Region'] = 'Caribe'
    colombia.loc[colombia['DeNombre'].isin(pacifico), 'Region'] = 'Pacífico'

    # Definir colores para cada región
    colores = {'Caribe': 'yellow', 'Pacífico': 'blue', 'Interior': 'lightgray'}

    # Crear el gráfico
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    colombia.plot(column='Region', ax=ax, legend=True, color=colombia['Region'].map(colores))

    # Ejemplo 1: Punto en la región Caribe (Santa Marta)
    latitud_caribe = CoordenadaGMS(11, 14, 40, 'N')  # Latitud de Santa Marta
    longitud_caribe = CoordenadaGMS(74, 12, 6, 'W')  # Longitud de Santa Marta
    longitud_referencia = CoordenadaGMS(0, 0, 0, 'E')  # Meridiano de Greenwich como referencia

    # Proyección directa (lat/long -> X/Y)
    x_caribe, y_caribe = aplicar_mercator_directo(latitud_caribe, longitud_caribe, longitud_referencia)

    # Proyección inversa (X/Y -> lat/long)
    lat_inverso_caribe, lon_inverso_caribe = aplicar_mercator_inverso(x_caribe, y_caribe, longitud_referencia)

    # Convertir los puntos al mismo CRS que el shapefile
    punto_caribe = Point(longitud_caribe.to_decimal(), latitud_caribe.to_decimal())  # Latitud/Longitud de Santa Marta
    gdf_punto_caribe = gpd.GeoDataFrame(geometry=[punto_caribe], crs='EPSG:4326')  # Definir el CRS

    # Mostrar el punto en el mapa
    gdf_punto_caribe.plot(ax=ax, marker='o', color='red', markersize=50)

    # Ejemplo 2: Punto en la región Pacífico (Quibdó)
    latitud_pacifico = CoordenadaGMS(5, 41, 39, 'N')  # Latitud de Quibdó
    longitud_pacifico = CoordenadaGMS(76, 39, 54, 'W')  # Longitud de Quibdó

    # Proyección directa (lat/long -> X/Y)
    x_pacifico, y_pacifico = aplicar_mercator_directo(latitud_pacifico, longitud_pacifico, longitud_referencia)

    # Proyección inversa (X/Y -> lat/long)
    lat_inverso_pacifico, lon_inverso_pacifico = aplicar_mercator_inverso(x_pacifico, y_pacifico, longitud_referencia)

    # Convertir los puntos al mismo CRS que el shapefile
    punto_pacifico = Point(longitud_pacifico.to_decimal(), latitud_pacifico.to_decimal())  # Latitud/Longitud de Quibdó
    gdf_punto_pacifico = gpd.GeoDataFrame(geometry=[punto_pacifico], crs='EPSG:4326')  # Definir el CRS

    # Mostrar el punto en el mapa
    gdf_punto_pacifico.plot(ax=ax, marker='o', color='green', markersize=50)

    # Añadir título y ajustar visualización
    ax.set_title("Mapa de Colombia: Regiones del Caribe y Pacífico con Puntos", fontsize=15)
    plt.show()

if __name__ == "__main__":
    main()
