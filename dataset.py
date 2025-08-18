# Instala pandas en la termina
#python -m pip install pandas


# Instala matplotlib 
#python -m pip install matplotlib


#O para instalar ambas bibliotecas al mismo tiempo usar:

#python -m pip install pandas matplotlib

# Instala Numpy 
# pip install numpy

###################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuración de gráficos
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 6)

# Cargar datos
file_id = '1g2zV414Sz4hSnKsPPZnetWTRNkEVMbHm'
download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
df = pd.read_csv(download_url)

# Procesamiento de datos
grouped = df.groupby('Year')['Individuals using the Internet (% of population)'].agg(['mean', 'std'])
grouped = grouped.reset_index()  # Convertir el índice 'Year' en columna

# Gráfico de barras con desviación estándar
plt.figure(figsize=(12, 6))
bars = plt.bar(
    x=grouped['Year'],
    height=grouped['mean'],
    color='tab:purple',
    alpha=0.7,
    label='Media'
)

# Añadir barras de error (desviación estándar)
plt.errorbar(
    x=grouped['Year'],
    y=grouped['mean'],
    yerr=grouped['std'],
    fmt='none',  # Sin línea conectora
    ecolor='black',
    capsize=5,
    label='±1 Desviación Estándar'
)

# Personalización
plt.title('Evolución del Uso de Internet (% Población) por Año', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de población (%)', fontsize=12)
plt.xticks(grouped['Year'], rotation=45)  # Asegurar que todos los años se muestren
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()

# Visualización exploratoria básica
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

# Verificación rápida de los datos
print("="*80)
print("PRIMERAS FILAS DEL DATASET".center(80))
print("="*80)
print(df.head())  # Mostrar las primeras 5 filas

# Definir columnas clave (ajustar según el dataset real)
year_col = 'Year'
internet_col = 'Individuals using the Internet (% of population)'

# Calcular estadísticas por año
stats_by_year = df.groupby(year_col)[internet_col].agg(
    Media='mean',
    Mediana='median',
    Desviación_Estándar='std',
    Mínimo='min',
    Máximo='max',
    Q1=lambda x: np.percentile(x, 25),  # Percentil 25% (Cuartil 1)
    Q3=lambda x: np.percentile(x, 75)   # Percentil 75% (Cuartil 3)
)

print("\n" + "="*80)
print("ESTADÍSTICAS POR AÑO".center(80))
print("="*80)
print(stats_by_year)

# Calcular correlación
correlation = np.corrcoef(df[year_col], df[internet_col])[0, 1]

print("\n" + "="*80)
print("CORRELACIÓN AÑO vs INTERNET".center(80))
print("="*80)
print(f"Coeficiente de correlación (r): {correlation:.3f}")

plt.figure()
plt.plot(stats_by_year.index, stats_by_year['Media'], 
         label='Media', color='royalblue', marker='o', linewidth=2)
plt.fill_between(
    stats_by_year.index,
    stats_by_year['Media'] - stats_by_year['Desviación_Estándar'],
    stats_by_year['Media'] + stats_by_year['Desviación_Estándar'],
    color='royalblue', alpha=0.2, label='±1 Desviación Estándar'
)
plt.title('Evolución del Uso de Internet (% Población) por Año', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('% de Población', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Secciónde desviación estándar
plt.figure()
plt.plot(stats_by_year.index, stats_by_year['Media'], 
         label='Media', color='royalblue', marker='o', linewidth=2)
plt.fill_between(
    stats_by_year.index,
    stats_by_year['Media'] - stats_by_year['Desviación_Estándar'],
    stats_by_year['Media'] + stats_by_year['Desviación_Estándar'],
    color='royalblue', alpha=0.2, label='±1 Desviación Estándar'
)
plt.title('Evolución del Uso de Internet (% Población) por Año', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('% de Población', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Dispersión y línea de tendencia
plt.figure()
plt.scatter(df[year_col], df[internet_col], 
            alpha=0.5, color='purple', label='Datos por país')

# Añadir línea de regresión
coefficients = np.polyfit(df[year_col], df[internet_col], 1)
trend_line = np.poly1d(coefficients)
plt.plot(df[year_col], trend_line(df[year_col]), '--', 
         color='red', label=f'Tendencia (r = {correlation:.2f})')

plt.title('Correlación: Año vs Uso de Internet', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('% de Población', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Crear grupos de 5 años
df['Year_Group'] = pd.cut(df[year_col], bins=range(1990, 2026, 5))

plt.figure()
boxplot_data = []
labels = []
for group in sorted(df['Year_Group'].unique()):
    if pd.notna(group):
        boxplot_data.append(df[df['Year_Group'] == group][internet_col].dropna())
        labels.append(f"{int(group.left)}-{int(group.right)-1}")

plt.boxplot(boxplot_data, labels=labels)
plt.title('Distribución del Uso de Internet por Periodos', fontsize=14)
plt.xlabel('Años', fontsize=12)
plt.ylabel('% de Población', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()