import pandas as pd
import os
def save_to_excel(data, filename="reddit_stats.xlsx"):
    # Obtener la ruta completa del archivo en el mismo directorio del script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, filename)

    # Cargar datos existentes si el archivo ya existe
    try:
        df_existing = pd.read_excel(file_path)
    except FileNotFoundError:
        df_existing = pd.DataFrame(columns=["Fecha", "Comunidad", "Miembros", "Online_users", "Descripción"])

    # Crear un DataFrame con los nuevos datos
    df_new = pd.DataFrame(data, columns=["Fecha", "Comunidad", "Miembros", "Online_users", "Descripción"])

    # Concatenar y guardar
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.to_excel(file_path, index=False)
    print(f"Datos guardados en {file_path}")
