# Instala pandas en la termina
#python -m pip install pandas


# Instala matplotlib si también la necesitas para las gráficas en la terminal
#python -m pip install matplotlib


#O para instalar ambas bibliotecas al mismo tiempo usar:

#python -m pip install pandas matplotlib


###################################

import pandas as pd
import matplotlib.pyplot as plt

# Construir la URL de descarga directa de Google Drive
file_id = '1g2zV414Sz4hSnKsPPZnetWTRNkEVMbHm'
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

# 1. Carga del dataset desde la URL
df = pd.read_csv(download_url)


# 2. Información básica del dataset
print("Información general del Dataset:")
df.info()
print("\nDescripción estadística de las columnas numéricas:")
print(df.describe())
print("\nDimensiones del Dataset (filas, columnas):", df.shape)

# 3. Identificación de valores nulos
print("\nConteo de valores nulos por columna:")
print(df.isnull().sum())

# 4. Mostrar las primeras 10 filas
print("\nPrimeras 10 filas del DataFrame:")
print(df.head(10))

# 5. Identificar tipos de datos por columna
print("\nTipos de datos por columna:")
print(df.dtypes)

# 6. Visualización exploratoria básica
# Suponemos que las columnas incluyen 'year' para el año y 'internet_users_share' para el porcentaje
# Ajusta el nombre de la columna según el contenido real del CSV.
mean_by_year = df.groupby('Year')['Individuals using the Internet (% of population)'].mean()

plt.figure(figsize=(10, 5))
plt.plot(mean_by_year.index, mean_by_year.values, color='tab:purple')
plt.title('Promedio mundial del uso de Internet por año')
plt.xlabel('Año')
plt.ylabel('Porcentaje de población que usa Internet')
plt.grid(True)
plt.tight_layout()
plt.show()

print(df.columns)