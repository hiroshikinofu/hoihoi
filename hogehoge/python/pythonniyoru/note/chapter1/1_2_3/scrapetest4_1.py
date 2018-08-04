# scrapetest3.pyに「サーバに全く到達できなかった場合のチェックコートを
# 5～6行目に追加

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
# ページの表題を返す際に問題があれば「None」を返す

    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
        # 取り出すときに何か問題があれば「None」を返す

    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
