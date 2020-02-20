# importing the necessary packages
import requests
import re
from bs4 import BeautifulSoup


def scrape(url):
    r1 = requests.get(url)

    doc = {'url': url}

    content = r1.content

    soup = BeautifulSoup(content, 'html5lib')

    title = soup.find_all('h1', class_='story-body__h1')

    z = title[0].get_text()

    doc['title'] = z

    # intro = soup.find_all(class_='story-body__introduction')
    #
    # txt = intro[0].get_text()

    paragraphs = soup.find(class_='story-body__inner').find_all('p')
    txt = ''
    for el in paragraphs:
        my_txt = el.get_text()
        txt += my_txt

    doc['text'] = txt

    return doc


# doc = scrape('https://bbc.in/2TC7NaE')
# print(doc)
