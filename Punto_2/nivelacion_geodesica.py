import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'D:\\Users\\Jan Sanchez\\Documents\\Repositorios\\Programacion\\Tarea heidy\\Punto_2\\Cartera Nivelacion formateada.xlsx', sheet_name = 'Hoja2')

# Esta función pide un valor al usuario para modificar la distancia
def solicitar_nueva_distancia(columna):
    while True:
        try:
            nuevo_valor = float(input(f"Ingrese un nuevo valor para la {columna}: "))
            return nuevo_valor
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

for i in range(len(df)):
    diferencia = abs(df.loc[i, 'Distancia1'] - df.loc[i, 'Distancia2'])
    if not (0.5 <= diferencia <= 7):
        print(f"\nFila {i}: La diferencia entre Distancia1 ({df.loc[i, 'Distancia1']}) y Distancia2 ({df.loc[i, 'Distancia2']}) es {diferencia}, fuera del rango permitido.")
        # Pedimos al usuario que elija qué distancia cambiar
        cambiar = input("¿Qué distancia desea cambiar? Ingrese 1 para Distancia1 o 2 para Distancia2: ")
        if cambiar == "1":
            df.loc[i, 'Distancia1'] = solicitar_nueva_distancia('Distancia1')
        elif cambiar == "2":
            df.loc[i, 'Distancia2'] = solicitar_nueva_distancia('Distancia2')
        else:
            print("Opción inválida, no se realizó ningún cambio.")

df['Distancia entre cambios'] = df['Distancia1'] + df['Distancia2']

for i in range(1, len(df)):
    df.loc[i, 'Distancia Absoluta'] = df.loc[i - 1, 'Distancia Absoluta'] + df.loc[i - 1, 'Distancia entre cambios']

df['resta'] = df['DATO V+'] - df['V-']

df['Sube'] = np.where(df['resta'] > 0, df['resta'], np.nan)
df['Baja'] = np.where(df['resta'] < 0, abs(df['resta']), np.nan)

df['Sube_shifted'] = df['Sube'].shift(1)
df['Baja_shifted'] = df['Baja'].shift(1)

# Este es un bucle que inicia desde la fila 1 (No inicia desde la fila 0 puesto que corrimos una fila hacia abajo para no modificar el valor de cota)
for i in range(1, len(df)):
    if not pd.isna(df.loc[i, 'Sube_shifted']):
        df.loc[i, 'Cota'] = df.loc[i-1, 'Cota'] + df.loc[i, 'Sube_shifted']
    elif not pd.isna(df.loc[i, 'Baja_shifted']):
        df.loc[i, 'Cota'] = df.loc[i-1, 'Cota'] - df.loc[i, 'Baja_shifted']

# Eliminar las columnas auxiliares
df = df.drop(columns=['Sube_shifted', 'Baja_shifted', 'resta'])

print(df)

"""
Segunda parte:
Altura instrumental
"""

# Ahora calculamos la altura instrumental
df2 = pd.read_excel(r'D:\\Users\\Jan Sanchez\\Documents\\Repositorios\\Programacion\\Tarea heidy\\Punto_2\\Cartera Nivelacion formateada.xlsx')

cambios_realizados = True
while cambios_realizados:
    cambios_realizados = False
    for i in range(len(df2)):
        if i == 0:
            df2.loc[i, 'ALTURA INSTRUMENTAL'] = df2.loc[i, 'COTA'] + df2.loc[i, 'DATO V+']
            continue
        cota_anterior = df2.loc[i - 1, 'COTA']
        altura_instrumental_anterior = df2.loc[i - 1, 'ALTURA INSTRUMENTAL']
        df2.loc[i, 'ALTURA INSTRUMENTAL'] = df2.loc[i, 'DATO V+'] + df2.loc[i, 'COTA']

df2['Distancia entre cambios'] = df2['Distancia1'] + df2['Distancia2']

for i in range(1, len(df2)):
    df2.loc[i, 'Distancia Absoluta'] = df2.loc[i - 1, 'Distancia Absoluta'] + df2.loc[i - 1, 'Distancia entre cambios']

vistas_intermedias = df[['PV', 'Baja']].dropna().reset_index(drop=True)
print(vistas_intermedias)

df['Altura instrumental'] = df2['ALTURA INSTRUMENTAL']
altura_instrumental = df.pop('Altura instrumental')
df.insert(8, 'Altura instrumental', altura_instrumental)

print(df2)
print(df)

# Graficar

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Distancia Absoluta'].round(2), df['Cota'], c=df['Cota'], cmap='viridis', s=100, marker='o')

for i in range(len(df)):
    plt.text(df['Distancia Absoluta'].round(2)[i], df['Cota'][i], 
             f'({df["Distancia Absoluta"].round(2)[i]}, {df["Cota"][i]:.2f})', 
             fontsize=9, ha='right', va='bottom')

plt.colorbar(scatter, label='Cota')
plt.title('Gráfica de Puntos: Distancia Absoluta vs Cota')
plt.xlabel('Distancia Absoluta')
plt.ylabel('Cota')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.xlim(df['Distancia Absoluta'].min() - 16, df['Distancia Absoluta'].max() + 10)
plt.ylim(df['Cota'].min() - 2, df['Cota'].max() + 2)
plt.show()
