# importing the necessary packages
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def scrape(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    r1 = requests.get(url, headers=headers)

    doc = {'url': url}

    content = r1.content
    soup = BeautifulSoup(content, 'html5lib')
    title = soup.find(class_="page-title_title spec_article_title")

    z = title.get_text()

    if len(z) > 0:
        doc['title'] = z


    # headline_descr = soup.find_all(class_='Article__Headline__Desc')
    #
    # txt = headline_descr[0].get_text()

    paragraphs = soup.find(class_="cb-widget spec_text_widget").find_all('p')
    txt = ""
    for el in paragraphs:
        my_txt = el.get_text()
        txt += (my_txt + " ")

    doc['text'] = txt

    return doc


# doc = scrape('https://www.emarketer.com/content/more-consumers-will-continue-to-drop-pay-tv-because-of-price-hikes?ECID=SOC1001')
# print(doc)