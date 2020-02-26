import requests
from bs4 import BeautifulSoup

#is actually the same as BBC world
def scrape(url):
    r1 = requests.get(url)

    doc = {'url': url}

    content = r1.content

    soup = BeautifulSoup(content, 'html5lib')

    title = soup.find_all('h1', class_='story-body__h1', limit=1)

    if len(title) > 0:
        z = title[0].get_text()
        doc['title'] = z

    # intro = soup.find_all(class_='story-body__introduction')
    #
    # txt = intro[0].get_text()

    paragraphs = soup.find(class_='story-body__inner').find_all('p')
    txt = ''
    for el in paragraphs:
        my_txt = el.get_text()
        txt += my_txt + " "

    doc['text'] = txt

    return doc


# doc = scrape('https://bbc.in/2jKEIdL')
# print(doc)