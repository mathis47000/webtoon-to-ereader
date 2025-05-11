from services.webtoon_service import add_webtoon

if __name__ == "__main__":
    # ask the user for a webtoon link
    link = input("Entrez le lien du webtoon à ajouter : ")
    # add the webtoon to the list
    add_webtoon(link)
    print(f"Webtoon ajouté : {link}")
    
