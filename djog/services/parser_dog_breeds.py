import os
from bs4 import BeautifulSoup
from djog.services.services_config.serv_config import WIKI_DOGS_URL
from urllib.request import urlopen
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_django.settings")
from djog.models.model_dogs import Breeds


def parser_breeds():
    """
    Open the link and gets
    structured code page. Searches
    for all tags <tr> and gets titles all dog breeds.
    """
    response = urlopen(WIKI_DOGS_URL)
    html_doc = response.read()
    breeds = []
    soup = BeautifulSoup(html_doc, 'lxml')
    table = soup.find('table')
    for rows in table.find_all('tr')[1:-1]:
        column = rows.a.get('title')
        breeds.append(column)
    return breeds


def add_breeds():
    """
    Add breeds to database
    """
    breeds_list = parser_breeds()
    for breed in breeds_list:
        dog_breed = Breeds(breed=breed)
        dog_breed.save()
        print(breed + 'was successfully added')


if __name__ == '__main__':
    add_breeds()
