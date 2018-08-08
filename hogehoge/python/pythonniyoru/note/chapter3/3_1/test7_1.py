# test7のコードに加え、以下の3つの規則を使い目的の項目リンクだけを抽出する
# ・divの中で、idがbodyContentに設定されている
# ・URLにコロンが含まれない
# ・URLが/wiki/で始まる

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$")):
# 上の行で3つの規則の条件定義を行っている
    if 'href' in link.attrs:
        print(link.attrs['href'])
