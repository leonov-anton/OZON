from bs4 import BeautifulSoup
import requests

payload = {'text': 'ozon', 'il': 225}
resolt = requests.get("https://yandex.ru/search/", params=payload).text
# print(resolt)

soup = BeautifulSoup(resolt, 'html.parser')
# print(soup.prettify())

referals = open("referals.txt", 'a')
for link in soup.find_all('a'):
    referals.write(link.get('href') + '\n')