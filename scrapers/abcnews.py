# importing the necessary packages
import requests
from bs4 import BeautifulSoup


def scrape(url):
    r1 = requests.get(url)

    doc = {'url': url}

    content = r1.content

    soup = BeautifulSoup(content, 'html5lib')

    title = soup.find_all(class_='Article__Headline__Title', limit=1)

    if len(title) > 0:
        z = title[0].get_text()
        doc['title'] = z

    headline_descr = soup.find_all(class_='Article__Headline__Desc')

    txt = headline_descr[0].get_text()

    paragraphs = soup.find(class_='Article__Content story').find_all('p')
    for el in paragraphs:
        my_txt = el.get_text()
        txt += (my_txt + " ")

    doc['text'] = txt

    return doc


# doc = scrape('https://abcn.ws/2maPawm')
# print(doc)