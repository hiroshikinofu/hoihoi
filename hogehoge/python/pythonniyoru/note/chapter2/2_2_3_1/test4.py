# giftListの表の題目行と製品のリストを印刷
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
