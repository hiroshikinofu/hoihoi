from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random



# このサイトで見つかったすべての外部URLのリストを集める
allExtLinks = set()
allIntLinks = set()
getInternalLinks = set()
getAllExternalLinks = set()



def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj, domain)
    externalLinks = getInternalLinks(bsObj, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

allIntLinks.add("http://oreilly.com")
getAllExternalLinks("http://oreilly.com")
