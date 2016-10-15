import urllib.request
from bs4 import BeautifulSoup

WIKI_DOGS_URL = 'https://en.wikipedia.org/wiki/List_of_dog_breeds'


def parser_breeds():
    """
    Open the link and gets
    structured code page. Searches
    for all tags <tr> and gets titles all dog breeds.
    """
    response = urllib.request.urlopen(WIKI_DOGS_URL)
    html_doc = response.read()
    breeds = []
    soup = BeautifulSoup(html_doc, 'lxml')
    table = soup.find('table')
    for rows in table.find_all('tr')[1:-1]:
        column = rows.a.get('title')
        breeds.append(column)
    return breeds


def main():
    """
    Print result.
    """
    print(parser_breeds())


if __name__ == '__main__':
    main()
