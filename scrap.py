import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep

# Constantes
base_url = "https://www.webtoons.com/fr/fantasy/estatedeveloper/ep-{ep}/viewer?title_no=5188&episode_no={ep}"
base_folder = "Estate_Developer"
headers_base = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

# Crée le dossier principal
os.makedirs(base_folder, exist_ok=True)

# Parcourt les épisodes de 1 à 100
for ep_num in range(50, 93):
    print(f"📥 Épisode {ep_num}...")
    ep_str = f"{ep_num:03}"
    url = base_url.format(ep=ep_num)
    headers = headers_base.copy()
    headers["Referer"] = url  # Referer spécifique à l’épisode

    # Création du dossier de l’épisode
    ep_folder = os.path.join(base_folder, f"ep_{ep_str}")
    os.makedirs(ep_folder, exist_ok=True)

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        images = soup.select("#_imageList img")

        if not images:
            print(f"⚠️ Aucun contenu trouvé pour l’épisode {ep_num}.")
            continue

        for idx, img in enumerate(images):
            img_url = img.get("data-url") or img.get("src")
            if not img_url:
                continue

            img_data = requests.get(img_url, headers=headers).content
            filename = os.path.join(ep_folder, f"img_{idx+1:03}.jpg")
            with open(filename, "wb") as f:
                f.write(img_data)

        print(f"✅ Épisode {ep_num} téléchargé ({len(images)} images)")
    except Exception as e:
        print(f"❌ Erreur épisode {ep_num} : {e}")

    sleep(1)  # pause pour éviter d’être bloqué par le serveur

print("\n🎉 Téléchargement terminé.")
