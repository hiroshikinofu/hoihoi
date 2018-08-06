# 先頭が「../img/gifts/img」かつ、末尾が「.jpg」となっている画像のパスを表示しろ
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\./img\/gifts/img.*\.jpg")})
# 上の行で正規表現を用いて『先頭「../img/gifts/img」＆末尾「.jpg」画像』の条件を定義している
for image in images:
    print(image["src"])
