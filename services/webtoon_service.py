from typing import Dict, Any
from models.webtoon import Webtoon
from services.storage import load_json, save_json
from services.scraper import get_last_episode

def add_webtoon(link: str) -> None:
    webtoons = load_json()
    title_no = link.split("title_no=")[1].split("&")[0]
    if any(w['id'] == title_no for w in webtoons):
        print(f"Webtoon {title_no} déjà existant.")
        return

    name = link.split('/')[5].replace('-', ' ').capitalize() + " - " + link.split('/')[2]
    last_ep = get_last_episode(link)
    webtoon = Webtoon(id=title_no, name=name, link=link, last_ep=last_ep)
    webtoons.append(webtoon.__dict__)
    save_json(webtoons)
