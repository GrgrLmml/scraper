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

    title = soup.find_all('h1', class_='ArticlePage-headline', limit=1)

    page_type = ""
    if len(title) > 0:
        z = title[0].get_text()
        doc['title'] = z
        page_type = "article"

    else:
        title = soup.find_all('h1', class_='ListiclePage-headline', limit=1)
        if len(title) > 0:
            z = title[0].get_text()
            doc['title'] = z
            page_type = "listicle"

    if page_type == "article":
        paragraphs = soup.find(class_='RichTextArticleBody-body RichTextBody').find_all('p')
        txt = ""
        for el in paragraphs:
            my_txt = el.get_text()
            txt += (my_txt + " ")

        doc['text'] = txt

    elif page_type == "listicle":
        text_div = soup.find(class_='ListiclePage-listicleBody RichTextBody')
        txt = text_div.get_text()
        doc['text'] = txt

    return doc


# doc = scrape('https://www.latimes.com/california/story/2019-09-28/former-uc-irvine-student-who-impersonated-a-doctor-pleads-guilty')
# print(doc)