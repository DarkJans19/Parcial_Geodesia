import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from CoordenadaGMS import CoordenadaGMS
from Mercator_inverso import Mercator_inverso

def aplicar_mercator_inverso(x, y, longitud_referencia):
    # Aplicar el método inverso de Mercator (X/Y -> lat/long)
    latitud, longitud = Mercator_inverso.metodo_inverso(x, y, longitud_referencia)
    print(f"Proyección inversa (Mercator) -> X: {x}, Y: {y} -> Latitud: {latitud}, Longitud: {longitud}")
    return latitud, longitud


def main():
    # Cargar el shapefile del mapa de Colombia
    colombia = gpd.read_file(r"Punto_4\Depto.shp")

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

    # Longitud de referencia (Meridiano de Greenwich)
    longitud_referencia = CoordenadaGMS(0, 0, 0, 'E')

    # Ejemplo 1: Punto en la región Caribe (Santa Marta) con proyección inversa
    x_caribe = -8245446.239420424  # Coordenada X en la proyección Mercator
    y_caribe = 1245677.188028544  # Coordenada Y en la proyección Mercator
    lat_inverso_caribe, lon_inverso_caribe = aplicar_mercator_inverso(x_caribe, y_caribe, longitud_referencia)

    # Crear el punto de Santa Marta y graficarlo en el mapa (valores float ya son decimales)
    punto_caribe = Point(lon_inverso_caribe, lat_inverso_caribe)
    gdf_punto_caribe = gpd.GeoDataFrame(geometry=[punto_caribe], crs='EPSG:4326')
    gdf_punto_caribe.plot(ax=ax, marker='o', color='red', markersize=50, label="Santa Marta")

    # Ejemplo 2: Punto en la región Pacífico (Quibdó) con proyección inversa
    x_pacifico = -8514556.127084994  # Coordenada X en la proyección Mercator
    y_pacifico = 673756.0871334127  # Coordenada Y en la proyección Mercator
    lat_inverso_pacifico, lon_inverso_pacifico = aplicar_mercator_inverso(x_pacifico, y_pacifico, longitud_referencia)

    # Crear el punto de Quibdó y graficarlo en el mapa (valores float ya son decimales)
    punto_pacifico = Point(lon_inverso_pacifico, lat_inverso_pacifico)
    gdf_punto_pacifico = gpd.GeoDataFrame(geometry=[punto_pacifico], crs='EPSG:4326')
    gdf_punto_pacifico.plot(ax=ax, marker='o', color='green', markersize=50, label="Quibdó")

    # Añadir título y ajustar visualización
    ax.set_title("Mapa de Colombia: Regiones del Caribe y Pacífico con Puntos", fontsize=15)
    plt.show()


if __name__ == "__main__":
    main()
