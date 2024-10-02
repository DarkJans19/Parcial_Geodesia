import pandas as pd

# Ahora calculamos la altura instrumental a partir de la primera hoja para comparar los resultados
df2 = pd.read_excel(r'Punto_2\Cartera Nivelacion formateada.xlsx')

# Iterar sobre el DataFrame para calcular ALTURA INSTRUMENTAL y COTA
for i in range(len(df2)):
    if i == 0:
        # Para la primera fila, ya tenemos la COTA y ALTURA INSTRUMENTAL
        continue
    
    # Obtener COTA anterior
    cota_anterior = df2.loc[i - 1, 'COTA']
    
    # Calcular ALTURA INSTRUMENTAL
    df2.loc[i, 'ALTURA INSTRUMENTAL'] = df2.loc[i, 'DATO V+'] + cota_anterior
    
    # Calcular COTA
    altura_instrumental_anterior = df2.loc[i, 'ALTURA INSTRUMENTAL']
    v_minus = df2.loc[i - 1, 'V-'] if df2.loc[i - 1, 'V-'] is not None else 0  # Asegúrate de manejar valores nulos
    df2.loc[i, 'COTA'] = altura_instrumental_anterior - v_minus
        
print(df2)