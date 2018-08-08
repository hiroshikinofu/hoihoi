# Wikipedia項目のURLを/wiki/<Article_Name>という形式で受け取り、
# 同じ形式のすべてのリンクされた項目URLのリストを返す「関数getLinks」の追加

# ある項目を手始めにgetLinksを呼び出して、返されたリストからランダムに
# 項目リンクを選び、getLinksを再び呼び出すという手順を、プログラムが停止するか、
# 新しいページに項目リンクが見つからなくなるまで続ける。

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
