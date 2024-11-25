import json
from scrape_reddit_comunities import scrape_reddit_communities

# Ruta al archivo .json con las comunidades
communities_file = "communities.json"

# Cargar la lista de comunidades desde el archivo .json
try:
    with open(communities_file, "r") as file:
        communities = json.load(file)
        print(f"Se cargarán las siguientes comunidades: {communities}")
except FileNotFoundError:
    print(f"El archivo {communities_file} no se encuentra. Por favor, crea un archivo .json con las comunidades.")
    communities = []
except json.JSONDecodeError:
    print(f"Error al leer el archivo {communities_file}. Asegúrate de que tenga un formato válido.")
    communities = []

# Verifica que hay comunidades antes de ejecutar
if communities:
    # Ejecutar el scraper
    scrape_reddit_communities(communities)
else:
    print("No hay comunidades para monitorear. El programa se detendrá.")
