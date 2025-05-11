# create file pour enregistrer la liste des webtoons déjà téléchargés
import os
import json
from datetime import datetime
from typing import List, Dict, Any
from get_last_episode import get_last_episode

# Define the path to the JSON file
LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), 'list.json')

def load_list() -> List[Dict[str, Any]]:
    if os.path.exists(LIST_FILE_PATH):
        with open(LIST_FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_list(webtoons: List[Dict[str, Any]]) -> None:
    with open(LIST_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(webtoons, file, ensure_ascii=False, indent=4)
        
def add_webtoon(link : str) -> None:
    webtoons = load_list()
    # https://www.webtoons.com/fr/romance/childhood-friend-complex/list?title_no=6708
    webtoon_id = str(link.split('title_no=')[1].split('&')[0])
    name = name = link.split('/')[5].replace('-', ' ').capitalize() + " - " + link.split('/')[2]
    new_webtoon = {
        'id': webtoon_id,
        'name': name,
        'link': link,
        'last_ep': [],
    }
    
    # add the new webtoon if it doesn't already exist
    if not any(webtoon['id'] == webtoon_id for webtoon in webtoons):
        last_ep = get_last_episode(link)
        new_webtoon['last_ep'] = last_ep
        webtoons.append(new_webtoon)
        save_list(webtoons)
    else:
        print(f"Webtoon with ID {webtoon_id} already exists in the list.")


    
def remove_webtoon(webtoon_id: str) -> None:
    webtoons = load_list()
    webtoons = [webtoon for webtoon in webtoons if webtoon['id'] != webtoon_id]
    save_list(webtoons)
    
def get_webtoon(webtoon_id: str) -> Dict[str, Any]:
    webtoons = load_list()
    for webtoon in webtoons:
        if webtoon['id'] == webtoon_id:
            return webtoon
    return None

# test
if __name__ == "__main__":
    add_webtoon("https://www.webtoons.com/fr/romance/childhood-friend-complex/list?title_no=6708")
    
    