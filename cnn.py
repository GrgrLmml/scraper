# importing the necessary packages
import requests
import re
from bs4 import BeautifulSoup


def scrape(url):

    r1 = requests.get(url)

    doc = {'url': url}


    content = r1.content

    soup = BeautifulSoup(content, 'html5lib')

    title = soup.find_all('h1', class_='pg-headline')

    if len(title) > 0:
        z = title[0].get_text()
        doc['title'] = z



    article = soup.find_all(class_='pg-rail-tall__body')

    if len(article) > 0:
        txt = article[0].get_text()
        doc['text'] = txt

    return doc

doc = scrape('https://edition.cnn.com/2020/01/22/us/homeless-veteran-burial-trnd/index.html?utm_source=twCNN&utm_content=2020-01-22T13%3A02%3A47&utm_term=link&utm_medium=social')
print(doc)
