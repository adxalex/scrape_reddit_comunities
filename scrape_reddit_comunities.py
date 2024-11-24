import time
from datetime import datetime
from get_reddit_community_stats import get_reddit_community_stats
from save_to_excel import save_to_excel


def scrape_reddit_communities(cycle_communities):
    while True:
        data = []
        for community_url in cycle_communities:
            # Extraer nombre de la comunidad del URL
            community_name = community_url.split('/r/')[1].split('/')[0]

            # Obtener estadísticas de la comunidad
            members, online_users, description = get_reddit_community_stats(community_url)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Agregar al listado de datos
            data.append([timestamp, community_name, members, online_users, description])

            # Imprimir resultados
            print(
                f"{timestamp} | Comunidad: {community_name} | Miembros: {members} | Online: {online_users} | Descripción: {description}")

            # Delay de 1 minuto entre consultas
            time.sleep(60)

        # Guardar datos en Excel después de cada ciclo completo
        save_to_excel(data)
