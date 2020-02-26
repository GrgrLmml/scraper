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

    title = soup.find('h1', class_='headline__heading')

    if len(title) > 0:
        z = title.get_text()
        doc['title'] = z


    # headline_descr = soup.find_all(class_='Article__Headline__Desc')
    #
    # txt = headline_descr[0].get_text()

    paragraphs = soup.find(itemprop="articleBody").find_all('p')
    txt = ""
    for el in paragraphs:
        my_txt = el.get_text()
        txt += (my_txt + " ")

    doc['text'] = txt

    return doc

#
# doc = scrape('https://www.telegraph.co.uk/news/2019/02/20/exclusive-jihadi-bride-shamima-begums-baby-british-could-return/')
# print(doc)