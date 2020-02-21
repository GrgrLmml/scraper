# importing the necessary packages
import requests
import re
from bs4 import BeautifulSoup


def scrape(url):

    r1 = requests.get(url)

    doc = {'url': url}


    content = r1.content

    soup = BeautifulSoup(content, 'html5lib')

    title = soup.find_all('h1', class_='ArticleHeader_headline')

    if len(title) > 0:
        z = title[0].get_text()
        doc['title'] = z

    article = soup.find_all(class_='StandardArticleBody_body')

    if len(article) > 0:
        txt = article[0].get_text()
        doc['text'] = txt

    return doc

# doc = scrape('https://t.co/FjjrOCMixG')
# print(doc['title'])
