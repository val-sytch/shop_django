import os
from djog.services.services_config.serv_config import ITEM_PATH_BREEDS, WIKI_DOGS_URL
from urllib.request import urlopen
from xml.etree import ElementTree
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_django.settings")
from djog.models.model_dogs import Breeds


def parser_tree_breeds():
    """
    Sends a request to the site and
    gets response. Data from site decodes and written
    in the html.file. Searches for all tags in table and
    gets all title dog breeds in the form (str). Write
    this (str) in the list.
    :return: list of all dog breeds from Wikipedia
    """
    response = urlopen(WIKI_DOGS_URL)
    data = response.read()
    html_doc = open('wiki.html', 'w')
    html_doc.write(data.decode('utf-8'))
    html_doc.close()
    breeds = []
    tree = ElementTree.parse('wiki.html')
    root = tree.getroot()
    for table in root.find(ITEM_PATH_BREEDS)[1:-1]:
        table.findall('tr')
        for tr in table[:-9]:
            tr
            for a in tr:
                dogs = a.get('title')
            breeds.append(dogs)
    return breeds


def add_breeds():
    """
    Add breeds to database
    """
    breeds_list = parser_tree_breeds()
    for breed in breeds_list:
        dog_breed = Breeds(breed=breed)
        dog_breed.save()
        print(breed + 'was successfully added')


if __name__ == '__main__':
    add_breeds()
