import requests
from bs4 import BeautifulSoup


def get_reddit_community_stats(url):
    try:
        # Realiza la solicitud HTTP al URL
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta excepción si ocurre un error en la solicitud

        # Parsear el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Número total de miembros
        total_members_span = soup.find('span', {'class': 'lowercase text-neutral-content-weak text-[12px]'})
        total_members = None
        if total_members_span:
            members_faceplate = total_members_span.find('faceplate-number', {'number': True})
            if members_faceplate:
                total_members = int(members_faceplate['number'])

        # Número de usuarios en línea
        online_users_span = soup.find_all('span', {'class': 'lowercase text-neutral-content-weak text-[12px]'})[-1]
        online_users = None
        if online_users_span:
            online_faceplate = online_users_span.find('faceplate-number', {'number': True})
            if online_faceplate:
                online_users = int(online_faceplate['number'])

        # Descripción de la comunidad
        description_div = soup.find('div', {'id': 'description'})
        description = description_div.get_text(strip=True) if description_div else "No description available"

        return total_members, online_users, description
    except Exception as e:
        print(f"Error al procesar {url}: {e}")
        return None, None, None
