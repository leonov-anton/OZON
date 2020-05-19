from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import datetime
import random

random.seed(datetime.datetime.now())
print(datetime.datetime.now())


def getLinks(articleURL):
    html = urlopen(f'https://en.wikipedia.org{articleURL}')
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Ozon.ru')
newArticle = links[random.randint(0, len(links)-1)].attrs['href']
print(newArticle)
print('https://wikipedia.org' + newArticle)

# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     print('https://wikipedia.org' + newArticle)
#     links = getLinks(newArticle)