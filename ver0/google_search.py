from bs4 import BeautifulSoup
import os
from urllib.parse import parse_qsl
from urllib.parse import urlparse
from requests import get as GET
def google_search(word):
    htmlfile = GET("https://www.google.co.jp/search?q="+word).text
    soup = BeautifulSoup(htmlfile, "lxml")
    pages = soup.find_all("h3",class_="r")
    title = [pages[i].a.text for i in range(3)]
    link = [pages[i].a.get("href")for i in range(3)]
    [print("----------------------\n\r["+title[i]+"]\n\r["+link[i]+"]") for i in range(3)]
