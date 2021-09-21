import requests
import json
from bs4 import BeautifulSoup

req = requests.get("http://www.qigushi.com/yuyangushi/")
print(req.content)

soup = BeautifulSoup(req.content, 'html.parser')
main = soup.find('main')
articles = main.find_all('article')
articles_list = []

for article in articles:
    text = article.find('div', class_='zi1')
    image = article.find('figure').find('img')
    link = article.find('span', class_='readmore').find('a')

    src = image['src']
    url = requests.get(src)

    filename = src.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(url.content)

    articles_list.append(dict(
        text=text.string,
        image=filename,
        link=link['href']
    ))

with open('results.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(articles_list, indent=4, ensure_ascii=False))

