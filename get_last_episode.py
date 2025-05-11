import requests
from bs4 import BeautifulSoup

def get_last_episode(url: str):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.content, "html.parser")

    episode_list = soup.select("ul#_listUl li._episodeItem")
    link_tag = episode_list[0].select_one("a")
    title_tag = episode_list[0].select_one("span.subj span")
    number_tag = episode_list[0].select_one("span.tx")


    return {
                "title": title_tag.text.strip(),
                "number": number_tag.text.strip().replace('#', ''),
                "url": link_tag["href"]
            }
