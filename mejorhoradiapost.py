import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel (reemplaza 'reddit_stats2.xlsx' por el nombre correcto)
df = pd.read_excel('reddit_stats2.xlsx')

# Convertir la columna Fecha a formato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Extraer día y hora
df['Día'] = df['Fecha'].dt.day_name()
df['Hora'] = df['Fecha'].dt.hour

# Agrupar por hora para obtener el promedio de usuarios online
hora_promedio = df.groupby('Hora')['Online_users'].mean().reset_index()

# Agrupar por día para obtener el promedio de usuarios online
dia_promedio = df.groupby('Día')['Online_users'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
).reset_index()

# Gráfico de actividad promedio por hora
plt.figure(figsize=(10, 6))
plt.plot(hora_promedio['Hora'], hora_promedio['Online_users'], marker='o')
plt.title('Promedio de Usuarios Online por Hora')
plt.xlabel('Hora del Día')
plt.ylabel('Usuarios Online (Promedio)')
plt.grid()
plt.show()

# Gráfico de actividad promedio por día
plt.figure(figsize=(10, 6))
plt.bar(dia_promedio['Día'], dia_promedio['Online_users'], color='skyblue')
plt.title('Promedio de Usuarios Online por Día')
plt.xlabel('Día de la Semana')
plt.ylabel('Usuarios Online (Promedio)')
plt.xticks(rotation=45)
plt.show()

# Identificar la mejor hora para publicar
mejor_hora = hora_promedio.loc[hora_promedio['Online_users'].idxmax()]
mejor_dia = dia_promedio.loc[dia_promedio['Online_users'].idxmax()]

print(f"La mejor hora para publicar es a las {mejor_hora['Hora']} hrs.")
print(f"El mejor día para publicar es {mejor_dia['Día']}.")