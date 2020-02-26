# importing the necessary packages
import requests
from bs4 import BeautifulSoup


def scrape(url):
    r1 = requests.get(url)

    doc = {'url': url}

    content = r1.content

    soup = BeautifulSoup(content, 'html5lib')

    title = soup.find_all('h1', class_='content__headline', limit=1)

    if len(title) > 0:
        z = title[0].get_text()
        doc['title'] = z

    headline_descr = soup.find_all(class_='content__standfirst')

    txt = ""
    for div in headline_descr:
        for p in div.find_all('p'):
            d = p.get_text()
            if len(d) > 0:
                txt += (d + ". ")

    paragraphs = soup.find(class_='content__article-body from-content-api js-article__body').find_all('p')
    # txt = ""
    for el in paragraphs:
        my_txt = el.get_text()
        txt += (my_txt + " ")

    doc['text'] = txt

    return doc


# doc = scrape('https://www.theguardian.com/sport/2019/sep/28/australia-circle-their-wagons-before-rugby-world-cup-showdown-with-wales?utm_term=Autofeed&CMP=twt_b-gdnnews&utm_medium=Social&utm_source=Twitter#Echobox=1569715281')
# print(doc)