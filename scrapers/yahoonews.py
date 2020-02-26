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
    title = soup.find(id="Lead-1-HeadComponentTitle")

    z = ""
    for h in title.find_all('h1'):
        z = h.text

    if len(z) > 0:
        z = title.get_text()
        doc['title'] = z


    # headline_descr = soup.find_all(class_='Article__Headline__Desc')
    #
    # txt = headline_descr[0].get_text()

    paragraphs = soup.find(class_="caas-body").find_all('p')
    txt = ""
    for el in paragraphs:
        my_txt = el.get_text()
        txt += (my_txt + " ")

    doc['text'] = txt

    return doc


# doc = scrape('https://news.yahoo.com/thousands-zealand-join-2nd-wave-023855432.html?ncid=twitter_yahoonewst_sjwumo1bpf4')
# print(doc)